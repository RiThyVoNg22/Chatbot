# 🚂 Deploy to Railway (FREE) - Step by Step

Railway offers **$5 free credit per month** which is perfect for hosting your bot 24/7!

## ✅ Pre-requisites

- ✅ Your GitHub repository: `RiThyVoNg22/Chatbot` (already done!)
- ✅ Your bot token from @BotFather
- ✅ A GitHub account

## 📝 Step-by-Step Instructions

### Step 1: Sign Up for Railway

1. **Open your browser** and go to: **https://railway.app**
2. Click **"Start a New Project"** or **"Login"**
3. Click **"Login with GitHub"**
4. Authorize Railway to access your GitHub account
5. You'll be redirected to Railway dashboard

### Step 2: Create New Project

1. In Railway dashboard, click **"New Project"** button
2. Select **"Deploy from GitHub repo"**
3. You'll see a list of your GitHub repositories
4. Find and click on **"Chatbot"** (RiThyVoNg22/Chatbot)
5. Railway will start importing your repository

### Step 3: Configure Deployment

Railway will automatically detect your project. It should show:
- **Build Command**: (auto-detected)
- **Start Command**: `python bot.py`

**If it doesn't auto-detect, set:**
- **Start Command**: `python bot.py`

### Step 4: Add Bot Token (IMPORTANT!)

1. In your Railway project, click on your service
2. Go to the **"Variables"** tab
3. Click **"+ New Variable"**
4. Add:
   - **Key**: `BOT_TOKEN`
   - **Value**: Your bot token (from @BotFather)
   - Click **"Add"**

⚠️ **Important**: Get your token from:
- Open Telegram
- Search for @BotFather
- Send `/token` or check your bot settings
- Copy the token (looks like: `8267818381:AAGzaVAAQ_qpI4pLsU16BiExP8i0BhWhub8`)

### Step 5: Deploy!

1. Railway will automatically start deploying
2. Wait for the build to complete (1-2 minutes)
3. Check the **"Deployments"** tab to see progress
4. Once status shows **"Active"** or **"Success"**, your bot is live! 🎉

### Step 6: Verify Bot is Working

1. Open Telegram
2. Find your bot
3. Send `/start`
4. If bot responds, **SUCCESS!** ✅

## 🔍 Troubleshooting

### Bot not responding?

1. **Check Deployments Tab**
   - Go to your Railway project
   - Click "Deployments"
   - Check latest deployment logs
   - Look for any errors

2. **Check Environment Variables**
   - Go to "Variables" tab
   - Make sure `BOT_TOKEN` is set correctly
   - No extra spaces or quotes

3. **Check Logs**
   - In Railway, click on your service
   - Go to "Logs" tab
   - Look for error messages

### Common Errors:

**"BOT_TOKEN environment variable is not set!"**
- ✅ Solution: Add `BOT_TOKEN` in Variables tab

**Deployment fails**
- ✅ Check logs in Deployments tab
- ✅ Make sure `requirements.txt` is in repository
- ✅ Verify Python version compatibility

## 💰 Free Tier Limits

- **$5 credit per month** (FREE)
- Your bot uses minimal resources (~$0.50-1.00/month)
- **Enough for 24/7 operation!**

## 🔄 Automatic Deployments

Railway automatically deploys when you push to GitHub:
- Push code to GitHub → Railway auto-deploys
- No manual steps needed after initial setup!

## 📊 Monitor Your Bot

- **Dashboard**: View all your services
- **Logs**: Real-time bot logs
- **Metrics**: CPU, Memory usage
- **Deployments**: Deployment history

## 🎉 You're Done!

Your bot is now running 24/7 on Railway! 

**Need to update?** Just push to GitHub and Railway will auto-deploy.

---

**Next Steps:**
- ✅ Test your bot in Telegram
- ✅ Share your bot with friends
- ✅ Monitor usage in Railway dashboard

**Questions?** Check Railway docs: https://docs.railway.app

