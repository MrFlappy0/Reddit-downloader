import subprocess

modules_to_install = ['praw']

def check_and_install_modules():
    for module in modules_to_install:
        try:
            __import__(module)
        except ImportError:
            subprocess.call(['pip', 'install', module])

check_and_install_modules()

import praw
import os
import requests

def download_images(subreddit_name, download_path):
    reddit = praw.Reddit(client_id='hbyiQuZxTMQvlPyjtXFFow',
                     client_secret='3jlCkMdtLYI9vFAK1B0zlQDUXNsGdg',
                     user_agent='mybot/1.0')
    subreddit = reddit.subreddit(subreddit_name)
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    for submission in subreddit.hot(limit=None):
        if submission.url.endswith(('.jpg', '.png')):
            try:
                response = requests.get(submission.url)
                filename = f'{submission.id}.jpg'
                filepath = os.path.join(download_path, filename)
                open(filepath, 'wb').write(response.content)
                print(f'Image {filename} successfully downloaded')
            except Exception as e:
                print(f'Error downloading image: {submission.url}')
                print(e)
subreddit_name = input("Enter the name of the subreddit : ")
download_path = f'./downloads/reddit/{subreddit_name}'
download_images(subreddit_name, download_path)