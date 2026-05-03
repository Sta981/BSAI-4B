from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")
    
    dummy_reply = f"I received your message saying '{user_input}'. Flask backend is connected properly!"
    
    return jsonify({"answer": dummy_reply})

if __name__ == "__main__":
    app.run(debug=True, port=5000)