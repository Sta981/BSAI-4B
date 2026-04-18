from flask import Flask, jsonify
import requests

app = Flask(__name__)

# This handles http://127.0.0.1:5000/
@app.route('/')
def home():
    return jsonify({"message": "Back-end is LIVE! Use /search/songname to get data."})

# This handles http://127.0.0.1:5000/search/something
@app.route('/search/<query>')
def search(query):
    # Using iTunes API because it's free and won't give you a 401 error
    url = f"https://itunes.apple.com/search?term={query}&entity=song&limit=1"
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)