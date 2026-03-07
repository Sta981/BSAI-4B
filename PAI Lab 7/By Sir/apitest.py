import requests
from flask import Flask, render_template

app = Flask(__name__)

datadict = {
    "Name" : "Syed Tahir",
    "age" : 20
}

@app.route('/<date>')
def specific_date(date):  #localhost:5000/data
    response = requests.get(url+"&date="+date)
    if response.status_code==200:
        nasa_data =response.json()
    return render_template("index.html",data=nasa_data)

api_key = "HjCiC7ZT7ydPJjJqry1CIgCJ8JGLyRcHdAkWx0BF"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
@app.route('/')
def main():
    response = requests.get(url)
    if response.status_code==200:
        nasa_data =response.json()
    return render_template("index.html",data=nasa_data)
if __name__ == "__main__":
    app.run(debug=True)



