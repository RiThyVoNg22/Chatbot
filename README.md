# Grab Telegram Bot 🤖

A comprehensive Telegram chatbot that mimics Grab's super-app functionality, including ride-hailing, food delivery, wallet management, and customer support.

## 🚀 Features

### Core Services

- **🚗 Ride Booking** - Book GrabCar or GrabBike with pickup and destination
- **🍔 Food Delivery** - Browse restaurants and order food
- **📦 Order Tracking** - Track your rides and food orders in real-time
- **💳 GrabPay Wallet** - Manage your wallet balance, top-up, and view transactions
- **🎁 Promotions** - View current deals and promo codes
- **📞 Customer Support** - Get help with any issues
- **⚙️ Settings** - Configure your preferences

### User Experience

- ✅ Beautiful inline keyboards for easy navigation
- ✅ Conversation flows for multi-step processes
- ✅ Real-time order tracking with status updates
- ✅ Professional Grab-branded interface
- ✅ Error handling and logging
- ✅ Context-aware responses

## 📋 Requirements

- Python 3.8 or higher
- A Telegram account
- A bot token from [@BotFather](https://t.me/BotFather)

## 🔧 Installation

### 1. Clone or Download

```bash
cd ChatBot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or using a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Bot Token

1. Create a `.env` file:
   ```bash
   cp .env.example .env
   ```

2. Get your bot token:
   - Open Telegram and search for [@BotFather](https://t.me/BotFather)
   - Send `/newbot` and follow instructions
   - Copy the token you receive

3. Add your token to `.env`:
   ```
   BOT_TOKEN=your_bot_token_here
   ```

### 4. Run the Bot

```bash
python3 bot.py
```

You should see:
```
Starting Grab bot...
Bot is now listening for messages...
```

## 🎯 Usage

### Starting the Bot

1. Open Telegram and find your bot
2. Send `/start` or `/menu` to see the main menu
3. Use the inline buttons to navigate

### Main Features

#### 🚗 Book a Ride
1. Click "🚗 Book a Ride"
2. Share your pickup location
3. Enter your destination
4. Get confirmation with driver details

#### 🍔 Order Food
1. Click "🍔 Order Food"
2. Select a restaurant
3. Choose an item from the menu
4. Receive order confirmation with tracking

#### 📦 Track Order
- View active orders
- Check order status and ETA
- Refresh for updates

#### 💳 My Wallet
- View current balance
- Top up your wallet
- Check transaction history

#### 🎁 Promotions
- Browse current deals
- Get promo codes
- See special offers

#### 📞 Support
- Report issues
- Get help with orders
- Contact customer service

## 📱 Commands

- `/start` - Start the bot and see welcome message
- `/menu` - Show the main menu
- `/help` - Display help information
- `/cancel` - Cancel current operation

## 🏗️ Architecture

### Conversation Handlers

The bot uses Telegram's ConversationHandler for multi-step flows:

- **Ride Booking Flow**: Pickup → Destination → Confirmation
- **Food Ordering Flow**: Restaurant → Menu Item → Order Confirmation
- **Support Flow**: Issue Description → Confirmation

### Data Storage

Currently uses in-memory dictionaries for demo purposes:
- `user_data` - Stores user wallet balances and preferences
- `orders` - Stores ride and food orders

**Note**: For production, replace with a proper database (PostgreSQL, MongoDB, etc.)

## 🔄 Extending the Bot

### Adding New Features

1. **Add new menu options** in `get_main_menu()`
2. **Create callback handlers** in `button_handler()`
3. **Add conversation states** for multi-step flows
4. **Integrate with real APIs** for actual services

### Integration Ideas

- **Payment Gateway**: Integrate with GrabPay API
- **Maps API**: Use Google Maps/OpenStreetMap for real locations
- **Restaurant API**: Connect to actual restaurant menus
- **Driver API**: Real-time driver matching
- **Database**: Store user data and orders persistently

### Example: Adding a New Service

```python
# In button_handler, add:
elif query.data == "new_service":
    await query.edit_message_text("New service description")
    return NEW_SERVICE_STATE

# Add conversation handler:
new_service_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(button_handler, pattern="^new_service$")],
    states={...},
    fallbacks=[CommandHandler('cancel', cancel)]
)
application.add_handler(new_service_handler)
```

## 🐛 Troubleshooting

### Bot doesn't respond
- Check if the bot is running (process should be active)
- Verify `.env` file has correct token
- Check logs for errors

### Commands not working
- Make sure handlers are registered in `main()`
- Check for typos in command names
- Verify conversation handlers don't conflict

### Webhook errors
- The bot automatically removes webhooks on startup
- If issues persist, manually delete webhook via BotFather

## 📝 Notes

- This is a **demo/simulation** bot for educational purposes
- Not connected to real Grab services
- Uses mock data for orders and transactions
- Suitable for learning Telegram bot development

## 🔐 Security

- Never commit `.env` file (already in `.gitignore`)
- Keep your bot token secret
- Validate user input in production
- Use HTTPS for webhooks (if deploying)

## 📄 License

This project is open source and available for educational use.

## 🤝 Contributing

Feel free to extend this bot with more features:
- Real-time GPS tracking
- Payment processing
- Database integration
- Multi-language support
- AI-powered responses

## 🚀 Hosting & Deployment

Your chatbot can be hosted on various cloud platforms for 24/7 operation. Here are the best options:

### Option 1: Railway (Recommended - Free Tier Available)

1. **Create an account** at [railway.app](https://railway.app)
2. **Connect your GitHub** repository
3. **New Project** → Deploy from GitHub repo
4. **Select your repository**: `RiThyVoNg22/Chatbot`
5. **Add Environment Variable**:
   - Key: `BOT_TOKEN`
   - Value: Your bot token from BotFather
6. **Deploy** - Railway will automatically detect and deploy!

Railway provides:
- ✅ Free tier with $5 credit/month
- ✅ Automatic deployments from GitHub
- ✅ Easy environment variable management
- ✅ HTTPS support
- ✅ Auto-restart on crashes

### Option 2: Render (Free Tier Available)

1. **Sign up** at [render.com](https://render.com)
2. **New** → Background Worker
3. **Connect your GitHub** repository
4. **Configure**:
   - Name: `grab-chatbot`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python bot.py`
   - Environment Variables: `BOT_TOKEN=your_token_here`
5. **Create Service**

Render provides:
- ✅ Free tier (spins down after inactivity)
- ✅ Automatic SSL
- ✅ Easy setup

### Option 3: Heroku

1. **Install Heroku CLI** and login
2. **Create Heroku app**:
   ```bash
   heroku create your-bot-name
   ```
3. **Set environment variable**:
   ```bash
   heroku config:set BOT_TOKEN=your_token_here
   ```
4. **Deploy**:
   ```bash
   git push heroku main
   ```

### Option 4: Docker Deployment

1. **Build the image**:
   ```bash
   docker build -t grab-chatbot .
   ```

2. **Run the container**:
   ```bash
   docker run -d --name grab-bot -e BOT_TOKEN=your_token_here grab-chatbot
   ```

Deploy to any Docker-compatible platform (AWS ECS, Google Cloud Run, Azure Container Instances, etc.)

### Option 5: VPS (Virtual Private Server)

For full control, deploy on a VPS:

1. **Get a VPS** (DigitalOcean, Linode, Vultr, etc.)
2. **SSH into your server**
3. **Clone repository**:
   ```bash
   git clone https://github.com/RiThyVoNg22/Chatbot.git
   cd Chatbot
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Set environment variable**:
   ```bash
   export BOT_TOKEN=your_token_here
   ```
6. **Run with process manager** (PM2, systemd, or screen):
   ```bash
   # Using screen (simple)
   screen -S bot
   python bot.py
   # Press Ctrl+A then D to detach
   ```

### Keep Bot Running 24/7

For VPS, use a process manager:

**Using PM2** (recommended):
```bash
npm install -g pm2
pm2 start bot.py --name grab-bot --interpreter python3
pm2 save
pm2 startup  # Run once to enable auto-start on boot
```

**Using systemd** (Linux):
```bash
# Create service file: /etc/systemd/system/grab-bot.service
sudo nano /etc/systemd/system/grab-bot.service
```

Service file content:
```ini
[Unit]
Description=Grab Telegram Bot
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/ChatBot
Environment="BOT_TOKEN=your_token_here"
ExecStart=/usr/bin/python3 bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl enable grab-bot
sudo systemctl start grab-bot
```

## 🌐 Deployment Files Included

This repository includes:
- ✅ `Procfile` - For Heroku/Railway
- ✅ `Dockerfile` - For Docker deployments
- ✅ `railway.json` - Railway configuration
- ✅ `.dockerignore` - Docker ignore rules

## 📝 Notes

- **Never commit `.env` file** - Always use environment variables in hosting platforms
- **Monitor your bot** - Check logs regularly
- **Set up alerts** - Get notified if the bot crashes
- **Free tiers** - Most platforms offer free tiers perfect for personal projects

## 🙏 Acknowledgments

Inspired by Grab's super-app functionality. This is an educational project demonstrating Telegram bot development patterns.
