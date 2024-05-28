Projet de Machine Learning
Ce projet inclut un serveur de prédiction basé sur FastAPI et un script client pour interagir avec ce serveur. Le serveur charge un modèle de machine learning pré-entraîné et offre une API pour faire des prédictions.

Installation
Pour utiliser ce projet, vous aurez besoin de Python 3.6+ et des packages suivants :

fastapi
uvicorn (pour exécuter le serveur)
joblib
pandas
requests
Vous pouvez installer ces dépendances en utilisant pip :

pip install fastapi uvicorn joblib pandas requests



Serveur de prédiction (serveur.py)
Fonctionnalités
Le serveur FastAPI offre deux routes :

Une route GET à la racine (/) qui retourne un simple message de bienvenue.
Une route POST (/score) qui accepte des données JSON, effectue une prédiction en utilisant un modèle de machine learning chargé, et retourne la prédiction.

Déploiement
Assurez-vous que le modèle de machine learning (.pkl) est bien placé dans le répertoire attendu ou spécifiez son chemin via la variable d'environnement MODEL_PATH.
Démarrez le serveur en utilisant uvicorn :

uvicorn serveur:app --reload



Script Client (client.py)
Fonctionnalités
Le script client envoie une requête POST au serveur de prédiction avec des données JSON et affiche la réponse.

Utilisation
Exécutez le script client pour envoyer des données au serveur et recevoir une prédiction :

Copy code
python client.py
Sécurité et Configuration
Sécurité : Ce projet est destiné à des fins de démonstration et ne comprend pas de mécanismes de sécurité (authentification, chiffrement, etc.). Pour une utilisation en production, il est crucial d'implémenter ces aspects.
Configuration : Le chemin du modèle de machine learning peut être configuré via une variable d'environnement pour faciliter le déploiement dans différents environnements.
Contribution


Les contributions à ce projet sont bienvenues. Veuillez suivre les bonnes pratiques de développement et de documentation.

