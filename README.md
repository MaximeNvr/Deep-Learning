# Build Docker Image  

    docker build -t flask-deep-learning-gpu .

# Run the Container with GPU 

    docker run --gpus all -p 5000:5000 flask-deep-learning-gpu

# Prerequisites 

1. **Docker**: Ensure Docker is installed on your machine.  
2. **NVIDIA GPU (optional)**: If you plan to use a GPU, verify that your system has a properly configured and recognized NVIDIA GPU.  

- To verify:

        nvidia-smi

- If the command returns information about your GPU, everything is set up correctly.

3. **NVIDIA Container Toolkit**: If you are using a GPU, install this tool by following the instructions below.

# Install NVIDIA Container Toolkit 

### Check your distribution

    distribution=$(. /etc/os-release;echo $ID$VERSION_ID)

### Add NVIDIA Docker repository  

    curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -

    curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

### Update and install the toolkit

    sudo apt update

    sudo apt install -y nvidia-container-toolkit

### Restart Docker

    sudo systemctl restart docker


# Verify GPU in the Container

    docker exec -it <container_id_or_name> nvidia-smi


# Important Files and Directories

### Here is the project structure and the purpose of each file:

- **app.py**: Main file containing the Flask application.

- **monModel.h5**: Pre-trained deep learning model.

- **tokenizer.pkl**: Saved tokenizer for text preprocessing.

- **requirements.txt**: List of required Python dependencies.

- **static/**: Directory containing CSS, JavaScript, and images for the user interface.

- **templates/**: Directory containing HTML files for the user interface.

# Test the Flask Application

1. After starting the container with the `docker run` command: 
    
    Open your browser at the following address: [http://localhost:5000](http://localhost:5000).

2. Enter a text in the provided field and click "Verify" to see if the text is human or AI-generated.

# Troubleshooting

1. Show container logs:

        docker logs <container_id_or_name>

2. Verify TensorFlow is using the GPU:  
If you believe the GPU is not being used properly, check with the `nvidia-smi` command inside the container (see section above).

# Use Without GPU

If you do not wish to use the GPU, modify the following line in the Dockerfile:

    FROM tensorflow/tensorflow:2.13.0-gpu

Replace with:

    FROM tensorflow/tensorflow:2.13.0
