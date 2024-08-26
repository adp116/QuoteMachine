from flask import Flask, request, jsonify, render_template
import requests
import os
import markovify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Constants
API_URL = "https://api.quotable.io/quotes?limit=100"
QUOTES_FILE = 'quotes.txt'
MAX_LINES = 300
TRUNCATE_LINES = 100

def fetch_and_save_quotes():
    quotes = []
    url = API_URL
    while len(quotes) < 100:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            quotes.extend([f'{quote["content"]} - {quote["author"]}' for quote in data['results']])
            if len(data['results']) < 100:
                break
        else:
            print(f"Failed to fetch quotes. Status code: {response.status_code}")
            break

    # Avoid appending duplicates
    existing_quotes = set(load_quotes())
    new_quotes = set(quotes) - existing_quotes

    with open(QUOTES_FILE, 'a') as file:
        for quote in new_quotes:
            file.write(quote + '\n')

def load_quotes(filename=QUOTES_FILE):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        return file.readlines()

def truncate_file(filename=QUOTES_FILE, max_lines=MAX_LINES, truncate_lines=TRUNCATE_LINES):
    if not os.path.exists(filename):
        return

    with open(filename, 'r') as file:
        lines = file.readlines()

    if len(lines) > max_lines:
        with open(filename, 'w') as file:
            file.writelines(lines[truncate_lines:])

def find_best_quote(user_input, quotes):
    if not quotes:
        return "No quotes available."

    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([user_input] + quotes)
    similarity_matrix = cosine_similarity(vectors[0:1], vectors[1:])
    best_match_index = similarity_matrix.argmax()
    return quotes[best_match_index].strip()

def generate_markov_quote(quotes):
    text = ' '.join(quotes)
    text_model = markovify.Text(text)
    return text_model.make_sentence() or "No quotes available."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_quotes', methods=['POST'])
def fetch_quotes():
    try:
        fetch_and_save_quotes()
        truncate_file()
        return jsonify({"message": "Quotes fetched, saved, and truncated if necessary."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/generate_quote', methods=['POST'])
def generate_quote():
    try:
        user_input = request.json.get('user_input', '')
        quotes = load_quotes()
        if quotes:
            best_quote = find_best_quote(user_input, quotes)
            return jsonify({"quote": best_quote})
        else:
            return jsonify({"quote": "No quotes available."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/generate_markov_quote', methods=['POST'])
def generate_markov_quote_route():
    try:
        quotes = load_quotes()
        markov_quote = generate_markov_quote(quotes)
        return jsonify({"quote": markov_quote})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
