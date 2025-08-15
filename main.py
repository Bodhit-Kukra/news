from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
from flask_cors import CORS
import requests
import os

load_dotenv()

key = os.getenv("NEWS_API_KEY")
if not key:
    raise KeyError("Key not Found")

app = Flask(__name__)
CORS(app)

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={key}"
    try:
        response = requests.get(url)
        if(response.status_code == 200):
            data = response.json()
            return data
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
    except KeyError as e:
        print(f"Key not found {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/api/get_news", methods = ["POST"])
def call_get_news():
    result = get_news()
    return jsonify(result)

if(__name__ == '__main__'):
    app.run(debug=True)