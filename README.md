# Behavioral cloning

Ce répertoire contient le travail effectué dans le cadre du laboratoire d' intelligence artificielle.

##Description des fichiers

drive.py est un serveur socketIO qui écoute le port 4567 pour recevoir les évènements du simulateur et y envoyer les commandes de conduite.

model.py est le fichier qui crée, entraine et enregistre le modèle, en utilisant des fonctions fournies dans le fichier utils.py.

environment.yml est le fichier qui permet d'installer les librairies nécéssaires au fonctionnement du modèle.

behavioral-cloning-model.h5 est le modèle de conduite autonome que nous avons entraînné.

## Libraries and Dépendances

Voici les librairies et dépendances nécéssaires au fonctionnement du modèle.

- Keras, Tensorflow, scikit-learn
- openCV, PIL
- pandas, numpy, matplotlib, base64, io
- socketio, eventlet

## Contributeurs

- Christelle Kabemba 14250
- Alexandre Lenaerts 13055
- Steven Garofalo 
