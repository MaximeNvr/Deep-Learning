# Image de base TensorFlow avec support GPU
FROM tensorflow/tensorflow:2.13.0-gpu

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet dans le conteneur
COPY . .

# Exposer le port Flask
EXPOSE 5000

# Commande pour exécuter l'application
CMD ["python", "app.py"]
