import requests


"""
Task 1

Robots.txt

Download and save to file robots.txt from wikipedia, twitter websites etc.
"""


url = 'https://en.wikipedia.org/robots.txt'
response = requests.get(url)
with open('Robots_wiki.txt', 'w') as file:
    file.write(response.text)
