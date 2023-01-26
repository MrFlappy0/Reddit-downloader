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
                print(f'Image {filename} téléchargée avec succès')
            except Exception as e:
                print(f'Error downloading image: {submission.url}')
                print(e)
subreddit_name = input("Entrez le nom du subreddit : ")
download_path = f'./downloads/reddit/{subreddit_name}'
download_images(subreddit_name, download_path)