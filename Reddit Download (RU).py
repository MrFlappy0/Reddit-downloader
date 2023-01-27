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

def télécharger_les_images(subreddit_name, download_path):
  reddit = praw.Reddit(client_id='hbyiQuZxTMQvlPyjtXFFow', 
  client_secret='3jlCkMdtLYI9vFAK1B0zlQDUXNsGdg', 
  user_agent='mybot/1.0') 
  subreddit = reddit.subreddit(subreddit_name) 
  if not os.path.exists(download_path):
    os.makedirs(download_path) 
  for soumission in subreddit.hot(limit=None): 
    if soumission.url.endswith(('.jpg', '.png')): 
      try: 
        response = requests.get(soumission.url) 
        filename = f'{soumission.id}.jpg' 
        filepath = os.path.join(download_path, filename) 
        open(filepath, 'wb').write(response.content) 
        print(f'Изображение {filename} успешно загружено') 
      except Exception as e: 
        print(f'Ошибка при загрузке изображения: {soumission.url}') 
        print(e) 
subreddit_name = input("Введите название сабреддита: ") 
download_path = f'./downloads/reddit/{subreddit_name}' 
télécharger_les_images(subreddit_name, download_path)