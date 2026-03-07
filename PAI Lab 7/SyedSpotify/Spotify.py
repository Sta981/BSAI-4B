from flask import Flask, jsonify, render_template
import requests
import base64

app = Flask(__name__)

CLIENT_ID = '3c18e89dfa64470e89f4ec1815ac5cb5'
CLIENT_SECRET = '0e49549138c14be79c8c6f6236bc1127'

def get_access_token():
    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_base64 = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")
    
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    
    response = requests.post(url, headers=headers, data=data)
    return response.json().get("access_token") if response.status_code == 200 else None

@app.route('/')
def index():
    """Renders the HTML Front-End [cite: 136]"""
    return render_template('index.html')

@app.route('/search/<query>')
def search(query):
    """Retrieves JSON Knowledge Frame using GET method [cite: 107, 123]"""
    token = get_access_token()
    if not token:
        return jsonify({"error": "Authentication failed"}), 401

    url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=1"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "API Error", "status": response.status_code}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)