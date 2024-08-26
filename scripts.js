document.getElementById('fetchQuotes').addEventListener('click', function() {
    fetch('/fetch_quotes', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    });
});

document.getElementById('generateQuote').addEventListener('click', function() {
    const userInput = document.getElementById('userInput').value;

    fetch('/generate_quote', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_input: userInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = data.quote;
    });
});
