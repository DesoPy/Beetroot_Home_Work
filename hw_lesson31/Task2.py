import aiohttp
import asyncio
import json


"""
Task 2
Requests using concurrent and multiprocessing libraries

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/

As a result, store all comments in chronological order in JSON and dump it to a file.
For this task use concurrent and multiprocessing libraries for making requests to Reddit API.
"""


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def fetch_comments(session, subreddit, after):
    url = f'https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}&sort=asc&size=10&after={after}'
    return await fetch(session, url)


async def download_content(url, filename):
    content = {'data': []}
    after = None
    async with aiohttp.ClientSession() as session:
        while True:
            data = await fetch_comments(session, url, after)
            if not data.get('data'):
                break
            for key in data['data']:
                author = key['author']
                body = key['body']
                subreddit = key['subreddit']
                content['data'].append({'Author': author, 'Comment': body, 'Subreddit': subreddit})
            after = data['data'][-1]['created_utc']
    with open(filename, 'w') as file:
        json.dump(content, file, indent=4)


async def create_task(url, filename):
    await download_content(url, filename)


async def main():
    url = f'https://api.pushshift.io/reddit/comment/search/?subreddit=python'
    filename = f'python.json'
    await create_task(url, filename)

asyncio.run(main())
