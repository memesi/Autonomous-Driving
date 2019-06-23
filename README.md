# Behavioral cloning

Ce répertoire contient le travail effectué dans le cadre du laboratoire d' intelligence artificielle.

## Description des fichiers

drive.py est un serveur socketIO qui écoute le port 4567 pour recevoir les évènements du simulateur et y envoyer les commandes de conduite.

model.py est le fichier qui crée, entraine et enregistre le modèle, en utilisant des fonctions fournies dans le fichier utils.py.

utils.py contient les fonctions utilisée pour le préprocessing et augmentation des données.

environment.yml est le fichier qui permet d'installer les librairies nécéssaires au fonctionnement du modèle.

behavioral-cloning-model.h5 est le modèle de conduite autonome que nous avons entraînné.

## Libraries et dépendances

Voici les librairies et dépendances nécéssaires au fonctionnement du modèle.

- Python, Keras, Tensorflow
- Scikit-learn, Scikit-image 
- openCV, PIL
- pandas, numpy, matplotlib, base64, io
- socketio, eventlet

### Installation 

Afin d'installer les librairies et dépendances:

- Installer Anaconda
- Ouvrir l'invite de commande
- Lancer l'instruction suivantes:

conda env create -f environments.yml

## Lancer la simulation

1. Cloner ce répertoire : `git clone https://github.com/julienkessels/udacity-self-driving-car`
2.`cd behavioral cloning`
3. `python drive.py`
4. Run the Udacity simulator in the autonomous mode

## Contributeurs

- Christelle Kabemba 14250
- Alexandre Lenaerts 13055
- Steven Garofalo 
