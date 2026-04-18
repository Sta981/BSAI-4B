from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# Route to serve the Front-end
@app.route('/')
def index():
    return render_template('index.html')

# API Route to fetch data dynamically
@app.route('/api/search/<query>')
def search(query):
    # Using the free iTunes API (No keys needed)
    url = f"https://itunes.apple.com/search?term={query}&entity=song&limit=5"
    try:
        response = requests.get(url)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)