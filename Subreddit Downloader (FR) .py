import subprocess
import datetime

# Ajout de la liste des modules à installer
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


import os
import requests
import datetime
import praw

def télécharger_fichiers(nom_subreddit, chemin_téléchargement, durée, nombre_max_téléchargements):
    """
    Cette fonction télécharge les fichiers depuis le subreddit donné dans le répertoire spécifié pendant la durée donnée et le nombre maximum de téléchargement.
    """
    # Gestion des erreurs
    try:
        reddit = praw.Reddit(client_id='hbyiQuZxTMQvlPyjtXFFow',
                            client_secret='3jlCkMdtLYI9vFAK1B0zlQDUXNsGdg',
                            user_agent='mybot/1.0')
        subreddit = reddit.subreddit(nom_subreddit)
        if not os.path.exists(chemin_téléchargement):
            os.makedirs(chemin_téléchargement)
        # Ajout des extensions de fichiers à télécharger
        extensions = ['.mp4']
        compteur_succès = 0
        compteur_échecs = 0
        for soumission in subreddit.new(limit=None):
            if soumission.created_utc > (datetime.datetime.now().timestamp() - durée):
                if any(soumission.url.endswith(ext) for ext in extensions):
                    if compteur_succès < nombre_max_téléchargements:
                        try:
                            # Vérifier si le fichier a déjà été téléchargé
                            nom_fichier = f'{soumission.id}{os.path.splitext(soumission.url)[-1]}'
                            chemin_fichier = os.path.join(chemin_téléchargement, nom_fichier)
                            if not os.path.exists(chemin_fichier):
                                # Télécharger le fichier
                                réponse = requests.get(soumission.url)
                                open(chemin_fichier, 'wb').write(réponse.content)
                                compteur_succès += 1
                                # Afficher un message d'avancement
                                print(f'Fichier {nom_fichier} téléchargé avec succès. {nombre_max_téléchargements - compteur_succès} fichiers restants')
                        except Exception as e:
                            compteur_échecs += 1
                            print(f'Erreur lors du téléchargement du fichier: {soumission.url}')
                            print(e)
                    else:
                        break
        print(f'{compteur_succès} fichiers téléchargés avec succès, {compteur_échecs} fichiers échoués')
    except Exception as e:
        # Retourner un code d'erreur
        print("Une erreur s'est produite:")
        print(e)
        return -1

# Demander le nom du subreddit
nom_subreddit = input("Entrez le nom du subreddit: ")
chemin_téléchargement = f'./downloads/reddit/{nom_subreddit}'

# Ajout de la demande de durée souhaitée
while True:
    print("Entrez la période pendant laquelle vous souhaitez télécharger les fichiers (personnalisée en secondes):")
    print("1. 1 an (31 536 000 secondes)")
    print("2. 6 mois (15 552 000 secondes)")
    print("3. 1 mois (2 592 000 secondes)")
    print("4. 1 semaine (604 800 secondes)")
    print("5. 24 heures (86 400 secondes)")
    print("6. Autre")
    option = input("Entrez une option (1-6): ")
    if option == '1':
        durée = 31536000
        break
    elif option == '2':
        durée = 15552000
        break
    elif option == '3':
        durée = 25920000
        break
    elif option == '4':
        durée = 604800
        break
    elif option == '5':
        durée = 86400
        break
    elif option == '6':
        durée = int(input("Entrez la durée en secondes: "))
        break
    else:
        print("Option invalide.")

# Demander le nombre maximum de téléchargements
while True:
    try:
        nombre_max_téléchargements = int(input("Entrez le nombre maximum de téléchargements: "))
        break
    except ValueError:
        print("Option invalide.")

# Afficher un indicateur de progression
print(f'Démarrage des téléchargements. {nombre_max_téléchargements} fichiers à télécharger.')
télécharger_fichiers(nom_subreddit, chemin_téléchargement, durée, nombre_max_téléchargements)