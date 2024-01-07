import threading
import requests
import json


"""
Task 3

Requests using multiprocessing

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/

As a result, store all comments in chronological order in JSON and dump it to a file.
For this task use Threads for making requests to reddit API.
"""


def download_content(url, filename):
    response = requests.get(url)
    if response.ok:
        resp_jason = response.json()
        content = {'data': []}
        for key in resp_jason['data']:
            author = key['author']
            body = key['body']
            subreddit = key['subreddit']
            content['data'].append({'Author': author, 'Comment': body, 'Subreddit': subreddit})
        with open(filename, 'w') as file:
            json.dump(content, file, indent=4)
            file.close()


def create_thread(url, filename):
    download_thread = threading.Thread(target=download_content, args=(url, filename))
    download_thread.start()


url = f'https://api.pushshift.io/reddit/comment/search/?subreddit=python'
filename = f'python.json'
create_thread(url, filename)
