import subprocess
import datetime

# Add the list of modules to install
modules_to_install = ['praw', 'requests']

def check_and_install_modules():
    """
    This function checks if the required modules are installed. If not, it automatically installs them.
    """
    for module in modules_to_install:
        try:
            __import__(module)
        except ImportError:
            subprocess.call(['pip', 'install', module])

check_and_install_modules()

import praw
import os
import requests
import datetime

def download_files(user_name, download_path, duration, max_downloads):
    """
    This function downloads the files from the given account in the specified directory for the given duration and maximum downloads.
    """
    # Error handling
    try:
        reddit = praw.Reddit(client_id='hbyiQuZxTMQvlPyjtXFFow',
                            client_secret='3jlCkMdtLYI9vFAK1B0zlQDUXNsGdg',
                            user_agent='mybot/1.0')
        user = reddit.redditor(user_name)
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        # Add file extensions to download
        extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv', '.3gp', '.webp']
        count_success = 0
        count_failure = 0
        for submission in user.submissions.new(limit=None):
            if submission.created_utc > (datetime.datetime.now().timestamp() - duration):
                if any(submission.url.endswith(ext) for ext in extensions):
                    if count_success < max_downloads:
                        try:
                            # Check if file has already been downloaded
                            filename = f'{submission.id}{os.path.splitext(submission.url)[-1]}'
                            filepath = os.path.join(download_path, filename)
                            if not os.path.exists(filepath):
                                # Download the file
                                response = requests.get(submission.url)
                                open(filepath, 'wb').write(response.content)
                                count_success += 1
                                # Show a progress message
                                print(f'File {filename} downloaded successfully. {max_downloads - count_success} files remaining')
                        except Exception as e:
                            count_failure += 1
                            print(f'Error downloading file: {submission.url}')
                            print(e)
                    else:
                        break
        print(f'Downloaded {count_success} files successfully, {count_failure} files failed')
    except Exception as e:
        # Return an error code
        print("An error occured:")
        print(e)
        return -1

# Ask for the user name
user_name = input("Enter the user name: ")
download_path = f'./downloads/reddit/{user_name}'

# Add the request for desired duration
while True:
    print("Enter the duration you want to download files for (in seconds):")
    print("1. 1 year (31,536,000 seconds)")
    print("2. 6 months (15,552,000 seconds)")
    print("3. 1 month (2,592,000 seconds)")
    print("4. 1 week (604,800 seconds)")
    print("5. 24 hours (86,400 seconds)")
    print("6. Other")
    option = input("Enter an option (1-6): ")
    if option == '1':
        duration = 31536000
        break
    elif option == '2':
        duration = 15552000
        break
    elif option == '3':
        duration = 25920000
        break
    elif option == '4':
        duration = 604800
        break
    elif option == '5':
        duration = 86400
        break
    elif option == '6':
        duration = int(input("Enter duration in seconds: "))
        break
    else:
        print("Invalid option.")

# Ask for the maximum number of downloads
while True:
    try:
        max_downloads = int(input("Enter the maximum number of downloads: "))
        break
    except ValueError:
        print("Invalid option.")

# Show a progress indicator
print(f'Starting downloads. {max_downloads} files to download.')
download_files(user_name, download_path, duration, max_downloads)