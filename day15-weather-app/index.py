from flask import Flask, request, jsonify, render_template, redirect
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather', methods=['GET'])
def get_weather():
    api_key = "ce017dxMJ2kEvP9snCbZvNsRZYMRCW1h5kx71"
    location = request.args.get('location')

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = json.loads(response.text)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
