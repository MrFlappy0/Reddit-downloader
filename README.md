<!DOCTYPE html>
<html>
  <head>
      </head>
  <body>
    <h1>Reddit Image Downloader</h1>
    <p>This program uses the Reddit API to download images from a specified subreddit.</p>
    <h2>How to Use</h2>
    <ol>
      <li>Enter the name of the subreddit you want to download images from</li>
      <li>The program will create a download folder in the current directory with the subreddit name</li>
      <li>The images will be downloaded to this folder</li>
    </ol>
    <h2>Dependencies</h2>
    <ul>
      <li>praw</li>
      <li>requests</li>
    </ul>
    <h2>Notes</h2>
    <p>You must have a valid client_id and client_secret to use the Reddit API (or use my api which is already present)</p>
    <h2>Example</h2>
        <pre>
subreddit_name = input("Enter the subreddit name: ")
download_path = f'./downloads/reddit/{subreddit_name}'
download_images(subreddit_name, download_path)
        </pre>
    <h2>Languages</h2>
    <ul>
      <li><a href="https://github.com/MrFlappy0/Reddit-downloader/blob/2f834ca7246d20400327d04a0840bd988435ee64/Readme%20language/Readme.FR.md">Francais</a></li>
      <li><a href="https://github.com/MrFlappy0/Reddit-downloader/blob/2f834ca7246d20400327d04a0840bd988435ee64/Readme%20language/Readme.RU.md">Русский </a></li>
    </ul>
  </body>
</html>

