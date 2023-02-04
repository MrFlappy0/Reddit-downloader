import subprocess
import datetime

# Added the list of modules to install
modules_to_install = ['praw', 'requests']

def check_and_install_modules():
    """
    Cette fonction vérifie si les modules requis sont installés. Si ce n'est pas le cas, il les installe automatiquement.
    """
    for module in modules_to_install:
        try:
            __import__(module)
        except ImportError:
            subprocess.call(['pip', 'install', module])

check_and_install_modules()

#-------------------------------------------------------------------------------------------------------------------------------

import os
import requests
import datetime
import praw

def скачать_файлы(имя_подраздела, путь_скачивания, продолжительность, максимальное_количество_скачиваний):
    """
    Эта функция загружает файлы из данного подраздела в указанный каталог в течение указанного периода и максимального количества загрузок.
    """
    # Обработка ошибок
    try:
        reddit = praw.Reddit(client_id='hbyiQuZxTMQvlPyjtXFFow',
                            client_secret='3jlCkMdtLYI9vFAK1B0zlQDUXNsGdg',
                            user_agent='mybot/1.0')
        subreddit = reddit.subreddit(имя_подраздела)
        if not os.path.exists(путь_скачивания):
            os.makedirs(путь_скачивания)
        # Добавление расширений файлов для загрузки
        расширения = ['.mp4']
        количество_успехов = 0
        количество_ошибок = 0
        for представление в подразделе.new(limit=None):
            if представление.created_utc > (datetime.datetime.now().timestamp() - продолжительность):
                if any(представление.url.endswith(ext) for ext in расширения):
                    if количество_успехов < максимальное_количество_скачиваний:
                        try:
                            # Проверить, был ли файл уже загружен
                            имя_файла = f'{представление.id}{os.path.splitext(представление.url)[-1]}'
                            путь_файла = os.path.join(путь_скачивания, имя_файла)
                            if not os.path.exists(путь_файла):
                                # Загрузить файл
                                ответ = requests.get(представление.url)
                                open(путь_файла, 'wb').write(ответ.content)
                                количество_успехов += 1
                                # Вывести сообщение о ходе выполнения
                                print(f'File {имя_файла} успешно загружен. Осталось {максимальное_количество_скачиваний - количество_успехов} файлов')
                        except Exception as e:
                            количество_ошибок += 1
                            print(f'Error downloading file: {представление.url}')
                            print(e)
                    else:
                        break
        print(f'Downloaded {количество_успехов} files successfully, {количество_ошибок} files failed')
    except Exception as e:
        # Возврат кода ошибки
        print("Произошла ошибка:")
        print(e)
        return -1

# Запрос имени подраздела
имя_подраздела = input("Введите имя подраздела: ")
путь_скачивания = f'./downloads/reddit/{имя_подраздела}'

# Добавление запроса желаемой продолжительности
while True:
    print("Введите период, в течение которого вы хотите загрузить файлы (пользовательские в секундах):")
    print("1. 1 год (31 536 000 секунд)")
    print("2. 6 месяцев (15 552 000 секунд)")
    print("3. 1 месяц (2 592 000 секунд)")
    print("4. 1 неделя (604 800 секунд)")
    print("5. 24 часа (86 400 секунд)")
    print("6. Другое")
    параметр = input("Введите параметр (1-6): ")
    if параметр == '1':
        продолжительность = 31536000
        break
    elif параметр == '2':
        продолжительность = 15552000
        break
    elif параметр == '3':
        продолжительность = 25920000
        break
    elif параметр == '4':
        продолжительность = 604800
        break
    elif параметр == '5':
        продолжительность = 86400
        break
    elif параметр == '6':
        продолжительность = int(input("Введите продолжительность в секундах: "))
        break
    else:
        print("Недопустимый параметр.")

# Запрос максимального количества загрузок
while True:
    try:
        максимальное_количество_скачиваний = int(input("Введите максимальное количество загрузок: "))
        break
    except ValueError:
        print("Недопустимый параметр.")

# Вывести индикатор прогресса
print(f'Starting downloads. {максимальное_количество_скачиваний} files to download.')
скачать_файлы(имя_подраздела, путь_скачивания, продолжительность, максимальное_количество_скачиваний)