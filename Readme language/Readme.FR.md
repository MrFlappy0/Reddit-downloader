<h1>Introduction</h1>
<p>Ce code Python est la version 2 de mon programme de téléchargement de fichiers à partir de subreddits Reddit. Il utilise les bibliothèques <code>praw</code> et <code>requests</code> pour accomplir cette tâche.</p>
<h2>Modules requis</h2>
<p>Avant de commencer à utiliser ce programme, assurez-vous d'avoir installé les modules suivants : <code>praw</code> et <code>requests</code>.</p>
<p>Si ces modules ne sont pas déjà installés sur votre ordinateur, le programme les installe automatiquement pour vous à l'aide de la fonction <code>check_and_install_modules()</code>.</p>
<h2>Téléchargement de fichiers</h2>
<p>La fonction <code>download_files()</code> est utilisée pour télécharger des fichiers à partir du subreddit spécifié dans le répertoire indiqué pour la durée et le nombre maximum de téléchargements spécifiés.</p>
<p>Le programme vous demandera de saisir le nom du subreddit, la durée de téléchargement désirée et le nombre maximum de téléchargements souhaité.</p>
<h2>Extensions de fichiers acceptées</h2>
<p>Actuellement, le programme n'accepte que les fichiers de type <code>.mp4</code> pour le téléchargement.</p>
<h2>Chemin de téléchargement</h2>
<p>Les fichiers téléchargés seront enregistrés dans le répertoire <code>./downloads/reddit/[nom_du_subreddit]</code>.</p>
<h2>Indicateur de progression</h2>
<p>Le programme affiche un message de progression indiquant le nombre de fichiers téléchargés avec succès et le nombre de fichiers qui ont échoué à télécharger.</p>
<h2>Erreurs</h2>
<p>En cas d'erreur lors du téléchargement, le programme affiche un message d'erreur décrivant le problème rencontré et retourne un code d'erreur -1.</p>
