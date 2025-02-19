import time
import requests
import datetime
import sqlite3


def get_weather_data(city):
    app_id = "88716c89a36e56e4398e8249f2ad0225"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},&appid={app_id}'
    weather_url = requests.get(url)
    response = weather_url.json()
    return response


# get temp, humidity, city from json
def process_data(json_file):
    temp = json_file['main']['temp']
    celsius_temp = round(temp - 273.15, 2)
    humidity = json_file['main']['humidity']
    city = json_file['name']
    return f'{city},{celsius_temp},{humidity} '


# get time, sunset and sunrise from json, and convert to time with use datetime module,
# because these times are timestamp format.
def process_time(json_file):
    time = json_file['dt']
    date_time = datetime.datetime.fromtimestamp(time)
    sunrise = json_file['sys']['sunrise']
    sunrise_time = datetime.datetime.fromtimestamp(sunrise).time()
    sunset = json_file['sys']['sunset']
    sunset_time = datetime.datetime.fromtimestamp(sunset).time()
    return f'{date_time.date()}, {date_time.time()}, {sunrise_time}, {sunset_time}'


def create_connector_cursor(path):
    connector = sqlite3.connect(path)
    cursor = connector.cursor()
    return connector, cursor


def create_table(connector, cursor):
    query = "CREATE TABLE IF NOT EXISTS weather_information(city TEXT, temp REAL, humidity REAL, date TEXT, time TEXT,"\
            "sunrise TEXT, sunset TEXT)"
    cursor.execute(query)
    connector.commit()


def insert_into_database(connector, cursor, data):
    query = "INSERT INTO weather_information(city, temp, humidity, date, time, sunrise, sunset) VALUES (?,?,?,?,?,?,?)"
    cursor.execute(query, data)
    connector.commit()


while True:
    input_city = input('enter your city:')
    if get_weather_data(input_city)['cod'] == 200:
        city_data = process_data(get_weather_data(input_city)).split(',') + \
                    (process_time(get_weather_data(input_city)).split())
        con, cur = create_connector_cursor('mydb.db')  # create object of connector and cursor
        create_table(con, cur)
        insert_into_database(con, cur, city_data)
        break
    else:
        print('please enter the correct city')
        continue
