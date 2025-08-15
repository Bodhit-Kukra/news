from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
from flask_cors import CORS
import requests
import os

load_dotenv()

key = os.getenv("NEWS_API_KEY")
if not key:
    raise ValueError("NEWS_API_KEY is not set in the environment.")

app = Flask(__name__)
CORS(app, origins="https://bodhit-kukra.github.io")

@app.route("/api/app", methods=["GET"])
def get_news():
    # Construct the URL for the external API call
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={key}"
    
    try:
        # Make the request to the NewsAPI
        response = requests.get(url)
        # This is a robust way to check for HTTP errors (like 4xx or 5xx)
        response.raise_for_status()
        
        # If the request was successful, return the JSON data
        news_data = response.json()
        return jsonify(news_data)

    except requests.exceptions.RequestException as e:
        # If there was a network error or a bad status code, return a proper error
        print(f"Error calling NewsAPI: {e}")
        return jsonify({"error": "Failed to retrieve news data"}), 500

# The 'if __name__ == "__main__"' block is not needed for Vercel
# Vercel uses a WSGI server to run your 'app' object directly.