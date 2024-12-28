# Construire image Docker  

    docker build -t flask-deep-learning-gpu .

#  Lancer le conteneur avec gpu 

    docker run --gpus all -p 5000:5000 flask-deep-learning-gpu

# Prérequis 

1. Docker : Assurez-vous que Docker est installé sur votre machine. 
2. GPU NVIDIA (optionnel) : Si vous prévoyez d'utiliser un GPU, vérifier que votre système possède un GPU NVIDIA configuré et reconnu. 

- Pour vérifier :

        nvidia-smi

- Si  la commande retourne des informations sur votre GPU, tout est en ordre.

3. NVIDIA Container Toolkit : Si vous utilisez un GPU, installez cet outil en suivant les instructions ci-dessous.

# Installer NVIDIA Container Toolkit 

### Vérifier votre distribution

    distribution=$(. /etc/os-release;echo $ID$VERSION_ID)

### Ajouter le dépôt NVIDIA Docker 

    curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -

    curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

### Mettre à jour et installer le toolkit

    sudo apt update

    sudo apt install -y nvidia-container-toolkit

### Redémarrer Docker

    sudo systemctl restart docker


# Vérification du GPU dans le conteneur

    docker exec -it <container_id_or_name> nvidia-smi


# Fichiers et répertoires importants

### Voici la structure du projet et l'utilité de chaque fichier :

- app.py : Fichier principal qui contient l'application Flask.

- monModel.h5 : Modèle de deep learning pré-entrané.

- tokenizer.pkl : Tokenizer sauvegardé pour le pré-traitement des textes.

- requirements.txt : Liste des dépendances Python nécessaires.

- static/ : Dossier contenant les fichiers CSS, JavaScript et images pour l'interface utilisateur.

- templates/ : Dossier contenant les fichiers HTML pour l'interface utilisateur.

# Tester l'application Flask

1. Après avoir lancé le conteneur avec la commande docker run : 
    
    Ouvrez votre navigateur à l'adresse suivante : http://localhost:5000.

2. Entrez un texte dans le champ prévu et cliquez sur "Vérifier" pour voir si le texte est humain ou généré par une IA.

# En cas de problèmes

1. Afficher les logs du conteneur :

        docker logs <container_id_or_name>

2. Vérifier que TensorFlow utilise le GPU :
Si vous pensez que le GPU n'est pas utilisé correctement, vérifiez avec la commande nvidia-smi dans le conteneur (voir section ci-dessus).

# Utilisation sans GPU

Si vous ne souhaitez pas utiliser le GPU, modifiez la ligne suivante dans le Dockerfile :

    FROM tensorflow/tensorflow:2.13.0-gpu

Par :

    FROM tensorflow/tensorflow:2.13.0
