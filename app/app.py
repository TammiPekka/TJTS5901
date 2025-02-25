from flask import Flask
from flask import render_template, request, jsonify
import requests
import jinja2
import os
from test_weather_api import get_weather_data
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
OPEN_W_API_KEY = os.getenv("OPEN_W_API_KEY")

url_weather = "http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
url_open = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

@app.route("/")
def home():
    nimi = "Jukka"
    temperature_weather = get_weather_data(WEATHER_API_KEY, url_weather, "Helsinki")
    temperature_open = get_weather_data(OPEN_W_API_KEY, url_open, "Helsinki")
    return render_template("home.html", nimi=nimi, temperature_weather=temperature_weather, temperature_open=temperature_open)

@app.route("/home")
def health():
    return "OK"

@app.route("/testing")
def tester():
    return "testing endpoint, aasd,asdf,asd, test"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)