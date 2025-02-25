from flask import request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def add_numbers(a, b):
    return a + b


##Gets the cities from the weather API based on the user input
@app.route("/get_cities")
def get_cities():
    query = request.args.get("q", "")
    if not query:
        return jsonify([])

    api_url = f"https://api.weatherapi.com/v1/search.json?key={WEATHER_API_KEY}&q={query}"
    response = requests.get(api_url)

    if response.status_code == 200:
        cities = response.json()
        suggestions = [{"name": city["name"], "country": city["country"]} for city in cities]
        return jsonify(suggestions)
    
    return jsonify([]), 500  # Return empty list on failure