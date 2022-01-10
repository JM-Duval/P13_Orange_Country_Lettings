## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Développement local

*****récapitulatif haut niveau du fonctionnement du déploiement*****

  Pour le déploiement de ce projet, nous utiliserons CircleCi (qui est une intégration continue permettant
  de créer, tester, et déployer notre application plus facilement et plus rapidement). Une fois paramétré, CircleCi va:
	1 - Tester les fonctionnalités et de la syntaxe du code source. 
	2 - Créer une image de notre programme composée de plusieurs couches empaquetant toutes les installations, 
	  dépendances, bibliothèques, processus et codes d’application nécessaires pour creer un 
	  conteneur de cette même image (un conteneur Docker est une instance d’image Docker exécutée 
	  sur un microservice individuel).
	  Nota: Après avoir écrit le Dockerfile, on invoque l’utilitaire ” build “ pour créer une image 
	  basée sur ce fichier. Cette image se présente comme un fichier portable indiquant quels 
	  composants logiciels le conteneur exécutera et de quelle façon.
	3 - Partager l'image (après avoir renommé l'image =>tag) sur le registre DockerHub.
	4 - Déployer l'application sur le Cloud avec Heroku (a la façon dont un hébergeur web propose d’héberger 
	  un site web sur ses propres serveurs, cette solution permet de déployer l'application 
	  sur le Cloud pour permettre aux internautes de l’utiliser).
	
	 
	
*****la configuration requise pour un bon déploiement*****
	Avoir cloné et pushé le projet ci dessous sur votre compte git hub:
		- https://github.com/JM-Duval/P13_Orange_Country_Lettings.git
	Avoir un compte :
		- CircleCi
		- DockerHub
		- Heroku
		


*****les étapes nécessaires pour effectuer le déploiement*****	
	2 - CircleCi
	Connecter vous à CircleCi
	Puis accéder à la page de configuration du projet: https://app.circleci.com/projects/
	Une fois sur la page Projet, sélectionnez le projet que vous utilisez (dans notre cas P13_Orange_Country_Lettings).
	Sélectionnez l'option d'utilisation du modèle proposé dans le repo nommé config.yml, puis cliquez sur Configurer le projet .
	Sur la page d'acceuil 'Projects', selectionnez le projet en question puis les paramètres du projet en haut à droite (Project Settings).
	Dirigez vous vers la partie "Environment Variables". Ici, nous créerons 3 environnements de variables:
   	  a - DOCKERHUB_TOKEN -> Mot de passe pour se connecter à Dockerhub
	  b - DOCKERHUB_USERNAME -> Nom d'utilisateur pour se connecter à Dockerhub
	  c - HEROKU_API_KEY -> Token contenant les identifiants de Heroku 	

 	  a - DOCKERHUB_TOKEN
	    Connectez vous à votre compte DockerHub puis dirigez vous vers les paramètres de votre compte (Account Settings).
	    Cliquez sur l'onglet sécurité (Security) puis sur "New Access Token".
	    Renseignez le nom de la description et copier le token proposé par docker hub, puis valider.
	    Revenez dans CircleCi dans l'onglet Environment Variables puis cliquez sur "Add Environmennt Variable".
	    Pour "Name*", inscrivez DOCKERHUB_TOKEN
	    Pour "Value*", copiez le TOKEN 	
	    Cliquez ensuite sur "Add Environment Variable"
		
	  b - DOCKERHUB_USERNAME
 	    Cliquez à nouveau sur "Add Environment Variable"
	    Pour "Name*", inscrivez DOCKERHUB_USERNAME
	    Pour "Value*", renseignez votre nom d'identifiant Docker Hub
	    Cliquez ensuite sur "Add Environment Variable"

	  c - HEROKU_API_KEY
	    Sur votre terminal tapez: "heroku login"
	    Renseignez vos identifiants Heroku
	    Tapez la commande suivante: "heroku authorizations:create"
	    Copiez le Token proposé.
	    Revenez dans CircleCi dans l'onglet Environment Variables puis cliquez sur "Add Environmennt Variable".
	    Pour "Name*", inscrivez HEROKU_API_KEY
	    Pour "Value*", copiez le TOKEN 	
	    Cliquez ensuite sur "Add Environment Variable"

	3 - Heroku
	  Afin de créer une app sur Heroku, sur votre terminal tapez: "heroku create <nom-de-votre-app>"
	  Puis sur le fichier config.yml, dans la partie "deploy", remplacer:
		- le nom de l'ancienne application "oc-lettings-jmd-1"
		- par le nom de votre application. 
	
	Voila! La configuration est établie pour le déploiement ;-), vous n'avez plus qu'à réaliser un push sur Git
	du projet pour que le déploiement se fasse en automatique. 
	










