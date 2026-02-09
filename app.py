from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_KEY = "5165502b1e792c76f6264db61e28aba1"

indian_states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = {}
    if request.method == "POST":
        city = request.form.get("city")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        data = requests.get(url).json()

        if data.get("weather"):
            weather_data = {
                "weather": data["weather"][0]["main"],
                "description": data["weather"][0]["description"],
                "temperature": f"{int(data['main']['temp'] - 273.15)} °C",
                "pressure": f"{data['main']['pressure']} hPa",
                "city": city
            }
        else:
            weather_data = {
                "error": "Invalid city name. Please try again.",
                "city": city
            }

    return render_template("index.html", states=indian_states, data=weather_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
