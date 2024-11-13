function translateText() {
    const text = document.getElementById('inputText').value;
    const language = document.getElementById('languageSelect').value;

    fetch('/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text, language: language }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('translatedText').innerText = data.translated_text;
    })
    .catch(error => console.error('Error:', error));
}

function recordSpeech() {
    fetch('/speech-to-text', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (data.text) {
            document.getElementById('inputText').value = data.text;
        } else {
            alert("Speech recognition error: " + data.error);
        }
    })
    .catch(error => console.error('Error:', error));
}
