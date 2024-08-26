Quote Recommendation and Generation Web App
This project is a Flask-based web application that allows users to fetch quotes from an external API, generate quote recommendations based on user input, and create random quotes using a Markov chain model. The application integrates a modern, responsive UI built with HTML, CSS, and JavaScript.

Features
Fetch Quotes: Retrieve a set of quotes from the Quotable API and save them locally.
Quote Recommendation: Provide personalized quote recommendations using TF-IDF and cosine similarity.
Markov Chain Quote Generation: Generate new, random quotes using a Markov chain model.
Technologies Used
Backend: Flask, Python, scikit-learn, markovify
Frontend: HTML, CSS, JavaScript
APIs: Quotable API for fetching quotes
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/quote-webapp.git
cd quote-webapp
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Run the Flask app:

bash
Copy code
python app.py
The app will run on http://127.0.0.1:5000/ by default.

Usage
Fetching Quotes: Click the "Fetch Quotes" button to load new quotes from the API.
Getting Recommendations: Enter a phrase or text to receive a relevant quote based on your input.
Generating Random Quotes: Generate a random quote based on the Markov chain model.
Project Structure
app.py: Contains the main Flask application and backend logic.
templates/index.html: The main HTML file for the user interface.
static/css/styles.css: Styles for the UI.
static/js/main.js: Handles frontend logic and interactions.
quotes.txt: Stores fetched quotes locally.
How It Works
Backend (Flask)
Fetching Quotes: The app retrieves quotes from the Quotable API and saves them locally in a text file. The quotes are stored to prevent duplicates and to ensure the app can function offline.
Recommendation System: The app uses TF-IDF (Term Frequency-Inverse Document Frequency) to vectorize the user input and stored quotes. Cosine similarity is then calculated to find the quote that best matches the user's input.
Markov Chain Model: A Markov chain model is trained on the stored quotes to generate new, random quotes that mimic the style and content of the existing quotes.
Frontend (UI)
HTML Structure: The HTML file defines the structure of the page, including input fields, buttons, and areas for displaying results.
Styling with CSS: The CSS file provides a modern, responsive design with gradients, rounded corners, and animations to enhance the user experience.
JavaScript Interactions: JavaScript handles the communication between the UI and the Flask backend. It listens for user actions, sends requests to the Flask API, and updates the UI based on the responses.
Acknowledgments
Quotable API: For providing the quotes used in this project.
OpenAI and scikit-learn: For the tools and libraries used to build the recommendation and generation systems.
