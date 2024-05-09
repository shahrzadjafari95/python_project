import requests
import datetime
def get_weather_data():
    city = input('enter your city:')
    app_id = "88716c89a36e56e4398e8249f2ad0225"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},&appid={app_id}'
    weather_url = requests.get(url)
    response = weather_url.json()
    return response


# show temp, humidity, city from json
def process_data(json_file):
    temp = json_file['main']['temp']
    celsius_temp = round(temp - 273.15, 2)
    humidity = json_file['main']['humidity']
    city = json_file['name']
    return f'city:{city}, temp:{celsius_temp}, city:{city}, humidity:{humidity}'


def process_time(json_file):
    time = json_file['dt']
    date_time = datetime.datetime.fromtimestamp(time)
    sunrise = json_file['sys']['sunrise']
    sunrise_time = datetime.datetime.fromtimestamp(sunrise).time()
    sunset = json_file['sys']['sunset']
    sunset_time = datetime.datetime.fromtimestamp(sunset).time()
    return f'date: {date_time.date()}, time: {date_time.time()}, sunrise: {sunrise_time}, sunset: {sunset_time}'


