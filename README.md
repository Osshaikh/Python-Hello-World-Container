# 🐍 Python Hello World Container

A simple Python Flask "Hello World" application demonstrating how to:
- Run locally with Python
- Containerize with Docker
- Deploy to Azure Container Apps

Perfect for learning containerization and Azure deployment! 🚀

---

## 📁 Project Structure

```
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container configuration
├── .dockerignore       # Files to exclude from Docker image
├── .gitignore          # Files to exclude from Git
└── README.md           # This file
```

---

## 🏃 Option 1: Run Locally with Python

### Prerequisites
- Python 3.11+ installed
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Osshaikh/Python-Hello-World-Container.git
   cd Python-Hello-World-Container
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   ```
   http://localhost:8000
   ```

You should see: **"Hello, World! Welcome to my Azure App Service application!"**

---

## 🐳 Option 2: Run Locally with Docker

### Prerequisites
- Docker Desktop installed and running

### Steps

1. **Clone the repository** (if not already done)
   ```bash
   git clone https://github.com/Osshaikh/Python-Hello-World-Container.git
   cd Python-Hello-World-Container
   ```

2. **Build the Docker image**
   ```bash
   docker build -t helloworld-app .
   ```

3. **Run the container**
   ```bash
   docker run -p 8000:8000 helloworld-app
   ```

4. **Open in browser**
   ```
   http://localhost:8000
   ```

### Useful Docker Commands

| Command | Description |
|---------|-------------|
| `docker images` | List all images |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker stop <container_id>` | Stop a container |
| `docker rm <container_id>` | Remove a container |
| `docker rmi helloworld-app` | Remove the image |

---

## ☁️ Option 3: Deploy to Azure Container Apps

### Prerequisites
- Azure CLI installed (`az --version`)
- Azure subscription
- Docker Desktop running

### Step 1: Login to Azure

```bash
az login
```

### Step 2: Create a Resource Group (if needed)

```bash
az group create --name myResourceGroup --location eastus
```

### Step 3: Create Azure Container Registry (ACR)

```bash
az acr create --name <your-acr-name> --resource-group myResourceGroup --sku Basic --admin-enabled true
```

> **Note:** Replace `<your-acr-name>` with a globally unique name (e.g., `myaboracr123`)

### Step 4: Login to ACR

```bash
az acr login --name <your-acr-name>
```

### Step 5: Build and Tag the Image for ACR

```bash
docker build -t <your-acr-name>.azurecr.io/helloworld-app:v1 .
```

### Step 6: Push Image to ACR

```bash
docker push <your-acr-name>.azurecr.io/helloworld-app:v1
```

### Step 7: Deploy to Azure Container Apps

**Option A: Single Command (Quickest)**
```bash
az containerapp up \
  --name helloworld-app \
  --resource-group myResourceGroup \
  --image <your-acr-name>.azurecr.io/helloworld-app:v1 \
  --ingress external \
  --target-port 8000
```

**Option B: Step by Step**

1. Create Container Apps Environment:
   ```bash
   az containerapp env create \
     --name myContainerAppEnv \
     --resource-group myResourceGroup \
     --location eastus
   ```

2. Get ACR credentials:
   ```bash
   az acr credential show --name <your-acr-name>
   ```

3. Create Container App:
   ```bash
   az containerapp create \
     --name helloworld-app \
     --resource-group myResourceGroup \
     --environment myContainerAppEnv \
     --image <your-acr-name>.azurecr.io/helloworld-app:v1 \
     --registry-server <your-acr-name>.azurecr.io \
     --registry-username <your-acr-name> \
     --registry-password <password-from-step-2> \
     --target-port 8000 \
     --ingress external
   ```

### Step 8: Access Your App

After deployment, you'll get a URL like:
```
https://helloworld-app.<random>.azurecontainerapps.io
```

---

## 📊 Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                         DEVELOPMENT                              │
├─────────────────────────────────────────────────────────────────┤
│  Local Machine                                                   │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │  Python      │    │   Docker     │    │   Azure CLI  │      │
│  │  Flask App   │    │   Container  │    │              │      │
│  │  Port 8000   │    │   Port 8000  │    │              │      │
│  └──────────────┘    └──────────────┘    └──────────────┘      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                           AZURE                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────┐         ┌─────────────────────────┐       │
│  │ Azure Container │  push   │   Azure Container Apps   │       │
│  │ Registry (ACR)  │ ──────► │                         │       │
│  │                 │         │   ┌─────────────────┐   │       │
│  │ helloworld-app  │         │   │  helloworld-app │   │       │
│  │ :v1             │         │   │  Container      │   │       │
│  └─────────────────┘         │   └─────────────────┘   │       │
│                              │                         │       │
│                              │   URL: https://...      │       │
│                              │   .azurecontainerapps.io│       │
│                              └─────────────────────────┘       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Returns "Hello, World!" message |
| `/health` | GET | Health check endpoint |

---

## 💰 Cost Considerations

- **Azure Container Registry (Basic)**: ~$5/month
- **Azure Container Apps**: Pay per use (very cost-effective for demos)
  - Free tier: 180,000 vCPU-seconds/month
  - Free tier: 360,000 GiB-seconds/month

---

## 🧹 Cleanup Resources

To avoid charges, delete resources when done:

```bash
# Delete the Container App
az containerapp delete --name helloworld-app --resource-group myResourceGroup

# Delete the ACR
az acr delete --name <your-acr-name> --resource-group myResourceGroup

# Delete the entire Resource Group (deletes everything inside)
az group delete --name myResourceGroup
```

---

## 📚 Learn More

- [Azure Container Apps Documentation](https://learn.microsoft.com/en-us/azure/container-apps/)
- [Azure Container Registry Documentation](https://learn.microsoft.com/en-us/azure/container-registry/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)

---

## 🤝 Contributing

Feel free to submit issues and pull requests!

---

## 📄 License

MIT License - feel free to use this for learning and projects!

---

**Happy Coding! 🎉**

*Created for IIT Bombay Workshop - December 2025*
