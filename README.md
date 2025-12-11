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

## 🙏 Acknowledgments

Inspired by Grab's super-app functionality. This is an educational project demonstrating Telegram bot development patterns.
