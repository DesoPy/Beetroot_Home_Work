import datetime
import requests


"""
The Weather app

Write a console application which takes as an input a city name and returns current weather
in the format of your choice.
For the current task, you can choose any weather API or website or use openweathermap.org
"""


API_key = '32d6c2d58679ba4c7348e8f8f8abb065'

url = 'https://api.openweathermap.org/data/2.5/weather'

params = {'q': 'Dnipro', 'appid': API_key, 'units': 'metric'}

response = requests.get(url, params)
data = response.json()

main = data['weather'][0]['main']
description = data['weather'][0]['description']
temp = data['main']['temp']
pressure = data['main']['pressure']
humidity = data['main']['humidity']
wind = data['wind']['speed']
sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
sunset = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')

output = f'''The weather in Dnipro:
{main}, {description}
Temperature - {temp}°C
Humidity    - {humidity}%
Wind        - {wind} m/s
Sunrise     - {sunrise}
Sunset      - {sunset}'''

print(output)
