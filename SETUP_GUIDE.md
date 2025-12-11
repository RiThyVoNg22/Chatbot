# Step-by-Step Setup Guide

## Step 1: Create Your Bot on Telegram

1. **Open Telegram** on your phone or computer
2. **Search for @BotFather** in Telegram and open the chat
3. **Send the command**: `/newbot`
4. **Choose a name** for your bot (e.g., "My Awesome ChatBot")
5. **Choose a username** for your bot (must end with "bot", e.g., "myawesome_chatbot")
6. **Copy the token** BotFather gives you - it looks like:
   ```
   1234567890:ABCdefGHIjklMNOpqrsTUVwxyz123456789
   ```
   ⚠️ **Keep this token secret!** Never share it publicly.

## Step 2: Install Dependencies

Make sure you have Python 3.8+ installed, then run:

```bash
pip install -r requirements.txt
```

If you prefer using a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Step 3: Configure Your Bot Token

1. Create a `.env` file in the project directory:
   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file and replace `your_bot_token_here` with your actual token:
   ```
   BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz123456789
   ```
   (Use the token you got from BotFather)

## Step 4: Run the Bot

```bash
python bot.py
```

You should see:
```
Starting bot...
```

If you see this, your bot is now **running and connected to Telegram**! 🎉

## Step 5: Test Your Bot

1. Open Telegram and search for your bot using the username you created (e.g., `@myawesome_chatbot`)
2. Click "Start" or send `/start`
3. Your bot should respond with a welcome message!

## Troubleshooting

- **Error: "BOT_TOKEN environment variable is not set!"**
  - Make sure you created a `.env` file
  - Check that the token is correct in the `.env` file
  - Make sure there are no extra spaces around the `=`

- **Import errors**
  - Run `pip install -r requirements.txt` again
  - Make sure you're using Python 3.8 or higher

- **Bot doesn't respond**
  - Make sure the bot script is still running (check the terminal)
  - Check your internet connection
  - Verify the token is correct

## Stopping the Bot

Press `Ctrl+C` in the terminal where the bot is running.

## Running in Background (Optional)

To keep your bot running even when you close the terminal:

- **macOS/Linux**: Use `nohup python bot.py &` or `screen`/`tmux`
- **Cloud Services**: Consider deploying to Heroku, Railway, or a VPS

