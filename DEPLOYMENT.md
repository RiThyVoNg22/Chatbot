# 🚀 Deployment Guide

Quick guide to deploy your Grab chatbot to various platforms.

## 🎯 Quick Deploy Options

### 1️⃣ Railway (Easiest - 5 minutes)

**Steps:**
1. Go to [railway.app](https://railway.app) and sign up
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository: `RiThyVoNg22/Chatbot`
5. Click "Add Environment Variable"
   - Name: `BOT_TOKEN`
   - Value: Your bot token (get from @BotFather)
6. Railway will auto-deploy! 🎉

**Done!** Your bot is now live 24/7.

---

### 2️⃣ Render (Free - Spins down after inactivity)

**Steps:**
1. Go to [render.com](https://render.com) and sign up
2. Click "New +" → "Background Worker"
3. Connect your GitHub account
4. Select repository: `RiThyVoNg22/Chatbot`
5. Configure:
   - **Name**: `grab-chatbot`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`
6. Add Environment Variable:
   - Key: `BOT_TOKEN`
   - Value: Your bot token
7. Click "Create Background Worker"

**Done!** Bot will start automatically.

---

### 3️⃣ Heroku (Requires Credit Card)

**Via CLI:**
```bash
# Install Heroku CLI first: https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Create app
heroku create your-bot-name

# Set token
heroku config:set BOT_TOKEN=your_token_here

# Deploy
git push heroku main
```

**Via Dashboard:**
1. Go to [heroku.com](https://heroku.com)
2. New → Create new app
3. Connect GitHub
4. Enable automatic deploys
5. Go to Settings → Config Vars
6. Add `BOT_TOKEN`
7. Deploy!

---

### 4️⃣ Docker (Any Platform)

**Build & Run Locally:**
```bash
docker build -t grab-chatbot .
docker run -d --name bot -e BOT_TOKEN=your_token grab-chatbot
```

**Deploy to:**
- AWS ECS/Fargate
- Google Cloud Run
- Azure Container Instances
- DigitalOcean App Platform
- Fly.io

---

### 5️⃣ VPS (Full Control)

**Prerequisites:** Linux server (Ubuntu/Debian recommended)

```bash
# SSH into your server
ssh user@your-server-ip

# Clone repo
git clone https://github.com/RiThyVoNg22/Chatbot.git
cd Chatbot

# Install Python & pip
sudo apt update
sudo apt install python3 python3-pip -y

# Install dependencies
pip3 install -r requirements.txt

# Set environment variable
export BOT_TOKEN=your_token_here

# Run with PM2 (install Node.js first)
npm install -g pm2
pm2 start bot.py --name grab-bot --interpreter python3
pm2 save
pm2 startup
```

**Or use screen (simpler):**
```bash
screen -S bot
export BOT_TOKEN=your_token_here
python3 bot.py
# Press Ctrl+A then D to detach
```

---

## ✅ Verification

After deployment, test your bot:

1. Open Telegram
2. Find your bot
3. Send `/start`
4. If it responds, it's working! 🎉

---

## 🔍 Troubleshooting

### Bot doesn't respond
- ✅ Check bot is running (view logs on your platform)
- ✅ Verify `BOT_TOKEN` is set correctly
- ✅ Check internet connection on server
- ✅ Look for errors in logs

### Platform-specific issues

**Railway:**
- Check "Deployments" tab for logs
- Verify environment variables are set

**Render:**
- Check "Logs" tab
- Ensure it's not sleeping (free tier spins down)

**Heroku:**
- Run `heroku logs --tail` to see logs
- Check dyno is running: `heroku ps`

**VPS:**
- Check if process is running: `pm2 list` or `ps aux | grep bot.py`
- View logs: `pm2 logs grab-bot`

---

## 💡 Pro Tips

1. **Always use environment variables** - Never hardcode tokens
2. **Monitor logs** - Set up alerts for crashes
3. **Backup data** - If using database, set up backups
4. **Update regularly** - Keep dependencies updated
5. **Test before deploy** - Test locally first

---

## 📊 Platform Comparison

| Platform | Free Tier | Ease of Use | 24/7 Uptime | Best For |
|----------|-----------|-------------|-------------|----------|
| Railway  | ✅ $5/mo credit | ⭐⭐⭐⭐⭐ | ✅ | Beginners |
| Render   | ✅ (sleeps) | ⭐⭐⭐⭐ | ⚠️ | Testing |
| Heroku   | ❌ Paid only | ⭐⭐⭐⭐ | ✅ | Production |
| VPS      | ❌ | ⭐⭐ | ✅ | Full control |
| Docker   | Depends | ⭐⭐⭐ | Depends | Scalability |

---

**Need help?** Check the main README.md for more details!

