# Behavioral cloning

Ce répertoire contient le travail effectué dans le cadre du laboratoire d' intelligence artificielle.

## Modèle


On effectue un pré-processing sur l’image avant de la donner en entrée du réseau de neurone: Premièrement on va couper la partie supérieure de l’image parce qu’elle n’apporte que peu d’informations concernant la route.

Ensuite, on fait un resizing de manière à ce que les dimensions de l’image restent les mêmes que l’image originale malgré le cropping qui a eu lieu.

Dernièrement on passe de coordonées RGB à des coordonées YUV afin de réduire la bande passante des images. 

  ![](./images/architecture.png)

Voici l’architecture que nous avons utilisée pour le clonage de comportement. C’est une architecture inspirée de [celle proposée par des chercheurs de NVIDIA pour la simulation de conduite](https://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf).

SI on regarde de quoi cette architecture est composée, on voit que l’image d’entrée passe par une couche de normalisation des valeurs de cette images. Cela signifie que toutes les valeurs de pixels ne seront plus entre [0 et 256 ] mais entre [-1 et 1].

Suite à celà, un convolution en 2D, avec un pas de 2 et un kernel de taille 3x3 est appliquée.

Ensuite vient une couche de MaxPooling, dont l'objectif est de sous-échantillonner l’image en réduisant ses dimensions.

Puis on a une couche dropout qui va faire en sorte que les poids des nœuds appris durant la rétropropagation deviennent moins sensibles aux poids des autres nœuds et apprennent à décider du résultat indépendamment des autres neurones.

La couche flatten transforme matrice multidimensionnelle en un vecteur (1 ligne)

Dernièrement la couche Dense ou aussi appelée fully connected layer va effectuer une opération linéaire sur son vecteur d’entrée et générer l’output final à une dimension, qui sera l’angle de rotation à envoyer à la simulation.




## Description des fichiers

[`drive.py`](drive.py) est un serveur socketIO qui écoute le port 4567 pour recevoir les évènements du simulateur et y envoyer les commandes de conduite.

[`model.py`](model.py) est le fichier qui crée, entraine et enregistre le modèle, en utilisant des fonctions fournies dans le fichier utils.py.

[`utils.py`](utils.py) contient les fonctions utilisée pour le préprocessing et augmentation des données.

environments.yml est le fichier qui permet d`installer les librairies nécéssaires au fonctionnement du modèle.

behavioral-cloning-model.h5 est le modèle de conduite autonome que nous avons entraînné.

## Libraries et dépendances

Voici les librairies et dépendances nécéssaires au fonctionnement du modèle.

- Python, Keras, Tensorflow
- Scikit-learn, Scikit-image 
- openCV, PIL
- pandas, numpy, matplotlib, base64, io
- socketio, eventlet

### Installation 

Afin d`installer les librairies et dépendances:

- Installer Anaconda
- Ouvrir l'invite de commande
- `conda env create -f environments.yml`

## Lancer la simulation

1. Cloner ce répertoire : `git clone https://github.com/memesi/Autonomous-Driving`
2. Changer le répertoire courant : `cd autonomous-driving`
3. Lancer le serveur : `python drive.py`
4. Lancer le simulateur Udacity en mode autonome

## Contributeurs

- Christelle Kabemba 14250
- Alexandre Lenaerts 13055
- Steven Garofalo 16260
