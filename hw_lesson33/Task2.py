import requests
import datetime
import json


"""
Task 2

Load data

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/
As a result, store all comments in chronological order in JSON and dump it to a file.
"""


url = 'https://api.pushshift.io/reddit/comment/search/'
response = requests.get(url)

if response.status_code != 200:
    print(f'Request failed with status code {response.status_code}')
    print(response.json())
    exit()

comments = {}

for num, comment in enumerate(response.json()['data'], start=1):
    body = comment['body']
    time_posted = datetime.datetime.fromtimestamp(comment['created_utc']).strftime('%Y-%m-%d %H:%M')
    comments[num] = body, time_posted


with open('comments.json', 'w') as file:
    json.dump(comments, file, indent=4)
