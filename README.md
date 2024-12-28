## Construire image Docker : 

    docker build -t flask-deep-learning-gpu .

## Lancer le conteneur avec gpu : 

    docker run --gpus all -p 5000:5000 flask-deep-learning-gpu


## Installer NVIDIA Container Toolkit (si tu as pas): 

- distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
- && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
- && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
- sudo apt update
- sudo apt install -y nvidia-container-toolkit
- sudo systemctl restart docker

## Vérification que TensorFlow utilise bien le GPU : 

    docker exec -it <container_id_or_name> nvidia-smi
