<!DOCTYPE html>
  </head>
  <body>
    <h1>Téléchargement d'images Reddit</h1>
    <p>Ce programme utilise l'API de Reddit pour télécharger des images d'un subreddit spécifié.</p>
    <h2>Comment utiliser</h2>
    <ol>
      <li>Entrez le nom du subreddit que vous souhaitez télécharger des images</li>
      <li>Le programme créera un dossier de téléchargement dans le répertoire courant avec le nom du subreddit</li>
      <li>Les images seront téléchargées dans ce dossier</li>
    </ol>
    <h2>Dépendances</h2>
    <ul>
      <li>praw</li>
      <li>requests</li>
    </ul>
    <h2>Remarques</h2>
    <p>Vous devez avoir un client_id et un client_secret valides pour utiliser l'API de Reddit (ou utiliser mon api qui est déja présente) </p>
    <h2>Exemple</h2>
        <pre>
subreddit_name = input("Entrez le nom du subreddit : ")
download_path = f'./downloads/reddit/{subreddit_name}'
download_images(subreddit_name, download_path)
        </pre>
    </main>
</body>
</html>
  </body>
</html>
