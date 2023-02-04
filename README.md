<h1>Reddit Downloader - Version 2</h1>
<p>This program downloads files from a specified subreddit and saves them in a designated directory. The user has the ability to set the duration for which they would like to download files, as well as the maximum number of files to download.</p>
<h2>Installation of Required Modules</h2>
<p>Before using the program, the required modules must be installed. The program checks if the necessary modules are installed and if not, installs them automatically. The required modules are:</p>
<ul>
    <li>praw</li>
    <li>requests</li>
</ul>
<h2>Setting the Subreddit and Download Details</h2>
<p>The user must enter the name of the subreddit they would like to download files from. They must also set the duration for which they would like to download files, which can either be selected from pre-defined options or entered as a custom value in seconds. Lastly, the user must set the maximum number of files they would like to download.</p>
<h2>Starting the Downloads</h2>
<p>Once all the necessary details have been entered, the program begins the download process. The progress of the downloads is displayed, indicating the number of files remaining to be downloaded. If there are any errors during the download process, the program returns an error code and displays the error message.</p>
<h2>File Types and File Names</h2>
<p>The program currently only downloads files with the '.mp4' file extension. The file names are in the format of the subreddit post id followed by the file extension (e.g. '123456.mp4').</p>
<h2>File Destination</h2>
<p>The downloaded files are saved in a directory located at './downloads/reddit/[subreddit_name]'. If the directory does not exist, it will be created automatically.</p>
    <h2>Languages</h2>
    <ul>
      <li><a href="https://github.com/MrFlappy0/Reddit-downloader/blob/2f834ca7246d20400327d04a0840bd988435ee64/Readme%20language/Readme.FR.md">Francais</a></li>
      <li><a href="https://github.com/MrFlappy0/Reddit-downloader/blob/2f834ca7246d20400327d04a0840bd988435ee64/Readme%20language/Readme.RU.md">Русский </a></li>
    </ul>
  </body>
</html>

