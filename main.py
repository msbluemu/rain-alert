import requests
import os
from twilio.rest import Client


account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
api_key = os.environ.get("OWM_API_KEY")

MY_LAT = -33.718300
MY_LONG = 151.116806

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
weather_params ={
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()


will_rain = False
for weather_id in range(12):
    if weather_data["hourly"][weather_id]["weather"][0]["id"] < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️️",
        from_='+12542805318',
        to='+61420477182'
    )
    print(message.status)