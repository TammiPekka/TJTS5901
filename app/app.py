from flask import Flask
from flask import render_template, request, jsonify
import requests
import jinja2
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

OPEN_W_API_KEY = os.getenv("OPEN_W_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/")
def home():
    nimi = "Jukka"
    temperature_weather = "10"
    temperature_open = "20"
    return render_template("home.html", nimi=nimi, temperature_weather=temperature_weather)

@app.route("/home")
def health():
    return "OK"

@app.route("/testing")
def tester():
    return "testing endpoint, aasd,asdf,asd, test"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)