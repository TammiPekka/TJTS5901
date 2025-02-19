from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "YOUR_API_KEY"  # Change this to your own API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

#Function that gets temperature uses given city, API_KEY and BASE_URL
@app.route('/get_temperature', methods=['POST'])
def get_temperature():
    city = request.form.get("city")  #Get name of the city from the request
    if not city:
        return jsonify({"error": "City is required"}), 400  #Return error message if city is not given
    
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        return jsonify({"temperature1": data["main"]["temp"]})  #Return temperature of the city in json format
    else:
        return jsonify({"error": data.get("message", "Unknown error")}), response.status_code

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)  #Turn on the server
