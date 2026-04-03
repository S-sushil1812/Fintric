# Quick Deployment Guide - FINTRIC

Choose your deployment platform and follow the steps below.

---

## 🚀 OPTION 1: Streamlit Cloud (Recommended for Quick Start)

**Time**: 5-10 minutes  
**Cost**: Free tier available  
**Difficulty**: ⭐ (Easiest)

### Prerequisites
- GitHub account with code pushed
- Streamlit account (free)

### Steps

1. **Push code to GitHub**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to https://streamlit.io/cloud
   - Click "New app"
   - Select your GitHub repo
   - Select main branch
   - Click Deploy

3. **Configure Secrets**
   - In Streamlit Cloud dashboard: Settings → Secrets
   - Add your environment variables:
   ```
   GOOGLE_API_KEY = "your_api_key_here"
   GOOGLE_CLIENT_ID = "your_client_id_here"
   GOOGLE_CLIENT_SECRET = "your_client_secret_here"
   GOOGLE_REDIRECT_URI = "https://your-app.streamlit.app"
   ```

4. **Access Your App**
   - Your app is live at: `https://your-app.streamlit.app`

✅ **Done!** Your app is deployed and auto-updates with each push to GitHub.

---

## 🐳 OPTION 2: Docker (Recommended for Production)

**Time**: 30 minutes  
**Cost**: Depends on hosting (AWS, Azure, GCP, etc.)  
**Difficulty**: ⭐⭐ (Medium)

### Prerequisites
- Docker installed locally
- Cloud platform account (AWS, Azure, GCP, or Heroku)
- Docker Hub account (optional)

### Local Testing

```bash
# Build the image
docker build -t fintric:latest .

# Run locally
docker run -p 8501:8501 \
  -e GOOGLE_API_KEY="your_key" \
  -e GOOGLE_CLIENT_ID="your_id" \
  -e GOOGLE_CLIENT_SECRET="your_secret" \
  -e GOOGLE_REDIRECT_URI="http://localhost:8501" \
  fintric:latest

# Access at http://localhost:8501
```

### Deploy to Cloud

**AWS (ECS)**
```bash
# Tag image for ECR
docker tag fintric:latest your_account.dkr.ecr.region.amazonaws.com/fintric:latest

# Push to ECR
aws ecr get-login-password --region region | docker login --username AWS --password-stdin your_account.dkr.ecr.region.amazonaws.com
docker push your_account.dkr.ecr.region.amazonaws.com/fintric:latest

# Create ECS task and service
# (Use AWS Console or AWS CLI)
```

**Azure Container Instances**
```bash
# Push to Azure Container Registry
az acr login --name your_registry
docker tag fintric:latest your_registry.azurecr.io/fintric:latest
docker push your_registry.azurecr.io/fintric:latest

# Deploy
az container create \
  --resource-group your_group \
  --name fintric \
  --image your_registry.azurecr.io/fintric:latest \
  --cpu 1 --memory 1 \
  --environment-variables \
    GOOGLE_API_KEY="your_key" \
  --ports 8501 \
  --dns-name-label fintric
```

**Google Cloud Run**
```bash
# Configure gcloud
gcloud config set project your-project-id

# Build and deploy
gcloud run deploy fintric \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_API_KEY="your_key"
```

---

## 🎯 OPTION 3: Heroku (Simple & Free)

**Time**: 15 minutes  
**Cost**: Free tier available  
**Difficulty**: ⭐⭐ (Medium)

### Prerequisites
- Heroku account (free)
- Heroku CLI installed
- Git configured

### Steps

1. **Install Heroku CLI**
   ```bash
   # Windows
   choco install heroku-cli

   # macOS
   brew tap heroku/brew && brew install heroku

   # Linux
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku App**
   ```bash
   heroku create your-app-name
   ```

4. **Set Environment Variables**
   ```bash
   heroku config:set GOOGLE_API_KEY="your_key"
   heroku config:set GOOGLE_CLIENT_ID="your_id"
   heroku config:set GOOGLE_CLIENT_SECRET="your_secret"
   heroku config:set GOOGLE_REDIRECT_URI="https://your-app-name.herokuapp.com"
   ```

5. **Deploy**
   ```bash
   git push heroku main
   ```

6. **View Your App**
   ```bash
   heroku open
   # App opens at: https://your-app-name.herokuapp.com
   ```

✅ **Done!** Use `git push heroku main` for future updates.

---

## 🐳 OPTION 4: Docker Compose (Local Development or Self-Hosted)

**Time**: 20 minutes  
**Cost**: Only hosting costs  
**Difficulty**: ⭐⭐ (Medium)

### Prerequisites
- Docker & Docker Compose installed
- Self-hosted server or VPS

### Steps

1. **Prepare Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your actual credentials
   nano .env
   ```

2. **Start Services**
   ```bash
   docker-compose up -d
   ```

3. **Verify Services**
   ```bash
   docker-compose logs -f
   # or
   docker-compose ps
   ```

4. **Access Application**
   - App: http://localhost:8501
   - Database: postgres://localhost:5432/fintric

5. **Stop Services**
   ```bash
   docker-compose down
   ```

✅ Includes PostgreSQL for production-ready database!

---

## ✅ Pre-Deployment Checklist

Before deploying anywhere, complete these steps:

```bash
# 1. Validate project
python deployment_validation.py

# 2. Test locally
pip install -r requirements.txt
streamlit run app.py

# 3. Initialize database
python -c "from db import init_db; init_db()"

# 4. Verify .env setup
cp .env.example .env
# Edit .env with your keys

# 5. Run tests
python deployment_validation.py
```

---

## 🔐 Security Checklist

- ✅ NEVER commit .env file
- ✅ Use .env for local development only
- ✅ Use platform secrets for production
- ✅ Keep API keys secret and rotate regularly
- ✅ Enable HTTPS on production
- ✅ Use strong database passwords
- ✅ Set up monitoring and alerts

---

## 📊 Platform Comparison

| Platform | Cost | Effort | Best For | Auto-Scale |
|----------|------|--------|----------|-----------|
| **Streamlit Cloud** | Free tier | ⭐ | Quick MVP | Yes |
| **Heroku** | Free tier | ⭐⭐ | Small projects | Yes |
| **Docker + AWS** | Pay-as-you-go | ⭐⭐⭐ | Enterprise | Yes |
| **Docker Compose** | Only hosting | ⭐⭐ | Self-hosted | Manual |
| **Google Cloud Run** | Free tier | ⭐⭐ | Serverless | Yes |

---

## 🆘 Troubleshooting

### App won't start
```bash
# Check logs
docker logs fintric
heroku logs --tail
streamlit logs
```

### Database connection issues
```bash
# Verify database is running
docker-compose ps
# Restart services
docker-compose restart
```

### Environment variables not loaded
```bash
# Verify variables are set
docker inspect fintric
# For Heroku:
heroku config
# For local .env:
python -c "import os; print(os.getenv('GOOGLE_API_KEY'))"
```

### Port already in use
```bash
# Change port in docker-compose.yml
# Or kill process
lsof -i :8501
kill -9 <PID>
```

---

## 📞 Support

For detailed setup instructions, see:
- [ENV_SETUP_GUIDE.md](./ENV_SETUP_GUIDE.md) - Environment variables
- [DEPLOYMENT_CHECKLIST.md](./DEPLOYMENT_CHECKLIST.md) - Full checklist
- [README.md](./README.md) - Project overview

Good luck! 🚀
