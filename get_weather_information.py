import requests


def get_weather_data(city='Tehran'):
    city = input('enter your city:')
    app_id = "88716c89a36e56e4398e8249f2ad0225"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},&appid={app_id}'
    weather_url = requests.get(url)
    response = weather_url.json()
    # temp = response['main']['temp']
    # print(response)
    return response


def show_temp_humidity(json_file):
    temp = json_file['main']['temp']



get_weather_data()