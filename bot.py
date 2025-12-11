import os
import logging
import uuid
from datetime import datetime, timedelta
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, 
    CommandHandler, 
    MessageHandler, 
    CallbackQueryHandler,
    ConversationHandler,
    filters, 
    ContextTypes
)
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set!")

# Conversation states
(RIDE_PICKUP, RIDE_DESTINATION, FOOD_RESTAURANT, FOOD_ITEM, 
 TRACKING, WALLET_ACTION, SUPPORT_ISSUE) = range(7)

# Mock data storage (in production, use a database)
user_data = {}
orders = {}


def get_main_menu():
    """Create the main menu inline keyboard."""
    keyboard = [
        [
            InlineKeyboardButton("🚗 Book a Ride", callback_data="book_ride"),
            InlineKeyboardButton("🍔 Order Food", callback_data="order_food")
        ],
        [
            InlineKeyboardButton("📦 Track Order", callback_data="track_order"),
            InlineKeyboardButton("💳 My Wallet", callback_data="my_wallet")
        ],
        [
            InlineKeyboardButton("🎁 Promotions", callback_data="promotions"),
            InlineKeyboardButton("📞 Support", callback_data="support")
        ],
        [
            InlineKeyboardButton("ℹ️ About Grab", callback_data="about"),
            InlineKeyboardButton("⚙️ Settings", callback_data="settings")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    try:
        user = update.effective_user
        logger.info(f"Received /start command from user {user.id} (@{user.username})")
        
        welcome_message = (
            f"👋 <b>Welcome to Grab, {user.first_name}!</b>\n\n"
            f"Your everyday everything app.\n\n"
            f"🚗 <b>Ride</b> - Book a car or bike\n"
            f"🍔 <b>Food</b> - Order from restaurants\n"
            f"📦 <b>Deliveries</b> - Send packages\n"
            f"💳 <b>Payments</b> - GrabPay wallet\n\n"
            f"What would you like to do today?"
        )
        
        await update.message.reply_html(
            welcome_message,
            reply_markup=get_main_menu()
        )
        logger.info(f"Successfully sent start message to user {user.id}")
    except Exception as e:
        logger.error(f"Error in start handler: {e}", exc_info=True)
        try:
            await update.message.reply_text(
                "Welcome to Grab! Use /menu to see options.",
                reply_markup=get_main_menu()
            )
        except:
            pass


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show the main menu."""
    await update.message.reply_text(
        "📱 <b>Grab Main Menu</b>\n\nWhat would you like to do?",
        reply_markup=get_main_menu(),
        parse_mode='HTML'
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button callbacks."""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    
    if query.data == "book_ride":
        await query.edit_message_text(
            "🚗 <b>Book a Ride</b>\n\n"
            "Please share your pickup location.\n\n"
            "You can send:\n"
            "📍 Your current location (location button)\n"
            "📝 Or type your address",
            parse_mode='HTML'
        )
        context.user_data['ride_type'] = 'car'
        return RIDE_PICKUP
        
    elif query.data == "order_food":
        restaurants = [
            "🍕 Pizza Express",
            "🍜 Noodles House",
            "🍗 Fried Chicken Co",
            "🥗 Healthy Bites",
            "🍱 Sushi Station"
        ]
        keyboard = [[InlineKeyboardButton(r, callback_data=f"rest_{i}")] 
                   for i, r in enumerate(restaurants)]
        keyboard.append([InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")])
        
        await query.edit_message_text(
            "🍔 <b>Order Food</b>\n\n"
            "Select a restaurant:",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='HTML'
        )
        return FOOD_RESTAURANT
        
    elif query.data == "track_order":
        user_orders = [o for o in orders.values() if o.get('user_id') == user_id]
        if user_orders:
            latest = user_orders[-1]
            status = latest.get('status', 'Preparing')
            order_type = latest.get('type', 'Order')
            
            status_emoji = {
                'Preparing': '👨‍🍳',
                'On the way': '🚗',
                'Delivered': '✅'
            }.get(status, '📦')
            
            await query.edit_message_text(
                f"📦 <b>Track Your Order</b>\n\n"
                f"Order ID: {latest.get('id', 'N/A')}\n"
                f"Type: {order_type}\n"
                f"Status: {status_emoji} {status}\n"
                f"Estimated time: {latest.get('eta', '15-20 min')}\n\n"
                f"Your {order_type.lower()} is on the way!",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("🔄 Refresh", callback_data="track_order"),
                    InlineKeyboardButton("🔙 Back", callback_data="main_menu")
                ]]),
                parse_mode='HTML'
            )
        else:
            await query.edit_message_text(
                "📦 <b>No Active Orders</b>\n\n"
                "You don't have any active orders right now.",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")
                ]]),
                parse_mode='HTML'
            )
        return ConversationHandler.END
        
    elif query.data == "my_wallet":
        balance = user_data.get(user_id, {}).get('wallet_balance', 50.00)
        await query.edit_message_text(
            f"💳 <b>GrabPay Wallet</b>\n\n"
            f"Balance: <b>RM {balance:.2f}</b>\n\n"
            f"Recent transactions:\n"
            f"• Ride booking - RM 15.00\n"
            f"• Food order - RM 28.50\n"
            f"• Top-up - RM 100.00\n\n"
            f"💡 Tip: Top up your wallet for faster checkout!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("💵 Top Up", callback_data="topup")],
                [InlineKeyboardButton("📜 Transaction History", callback_data="history")],
                [InlineKeyboardButton("🔙 Back", callback_data="main_menu")]
            ]),
            parse_mode='HTML'
        )
        return WALLET_ACTION
        
    elif query.data == "promotions":
        await query.edit_message_text(
            "🎁 <b>Promotions & Deals</b>\n\n"
            "🔥 <b>Hot Deals:</b>\n\n"
            "• 20% off on first 3 rides\n"
            "   Code: GRAB20\n\n"
            "• Free delivery on orders above RM 30\n"
            "   Code: FREEDEL30\n\n"
            "• RM 5 off on food orders\n"
            "   Code: GRABFOOD5\n\n"
            "• Weekend Special: 15% cashback\n"
            "   Valid: Fri-Sun\n\n"
            "💡 Apply these codes at checkout!",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")
            ]]),
            parse_mode='HTML'
        )
        return ConversationHandler.END
        
    elif query.data == "support":
        await query.edit_message_text(
            "📞 <b>Grab Support</b>\n\n"
            "How can we help you today?\n\n"
            "Common issues:\n"
            "• Payment problems\n"
            "• Order issues\n"
            "• Account questions\n"
            "• Refund requests\n\n"
            "Please describe your issue:",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🔙 Back", callback_data="main_menu")
            ]]),
            parse_mode='HTML'
        )
        return SUPPORT_ISSUE
        
    elif query.data == "about":
        await query.edit_message_text(
            "ℹ️ <b>About Grab</b>\n\n"
            "Grab is Southeast Asia's leading super-app, providing everyday services:\n\n"
            "🚗 <b>Transport</b>\n"
            "Safe and reliable rides\n\n"
            "🍔 <b>Food Delivery</b>\n"
            "Your favorite restaurants delivered\n\n"
            "📦 <b>Logistics</b>\n"
            "Send packages anywhere\n\n"
            "💳 <b>Payments</b>\n"
            "GrabPay wallet and more\n\n"
            "Available in 8 countries across Southeast Asia!",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🔙 Back to Menu", callback_data="main_menu")
            ]]),
            parse_mode='HTML'
        )
        return ConversationHandler.END
        
    elif query.data == "settings":
        await query.edit_message_text(
            "⚙️ <b>Settings</b>\n\n"
            "Language: English\n"
            "Notifications: On\n"
            "Payment Method: GrabPay\n"
            "Preferred Vehicle: GrabCar\n\n"
            "More settings coming soon!",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🔙 Back", callback_data="main_menu")
            ]]),
            parse_mode='HTML'
        )
        return ConversationHandler.END
        
    elif query.data == "main_menu":
        await query.edit_message_text(
            "📱 <b>Grab Main Menu</b>\n\nWhat would you like to do?",
            reply_markup=get_main_menu(),
            parse_mode='HTML'
        )
        return ConversationHandler.END
        
    elif query.data.startswith("rest_"):
        restaurant_index = int(query.data.split("_")[1])
        restaurant_names = [
            "Pizza Express",
            "Noodles House",
            "Fried Chicken Co",
            "Healthy Bites",
            "Sushi Station"
        ]
        restaurant_name = restaurant_names[restaurant_index]
        
        menu_items = {
            0: ["🍕 Margherita Pizza - RM 25", "🍕 Pepperoni Pizza - RM 28", "🍕 Hawaiian Pizza - RM 30"],
            1: ["🍜 Beef Noodles - RM 18", "🍜 Chicken Noodles - RM 16", "🍜 Veggie Noodles - RM 14"],
            2: ["🍗 Original Fried Chicken - RM 15", "🍗 Spicy Fried Chicken - RM 16", "🍗 Chicken Combo - RM 22"],
            3: ["🥗 Caesar Salad - RM 20", "🥗 Greek Salad - RM 18", "🥗 Quinoa Bowl - RM 22"],
            4: ["🍱 Salmon Sushi Set - RM 35", "🍱 Mixed Sushi - RM 30", "🍱 Tuna Roll - RM 25"]
        }
        
        items = menu_items.get(restaurant_index, [])
        keyboard = [[InlineKeyboardButton(item, callback_data=f"food_{restaurant_index}_{i}")] 
                   for i, item in enumerate(items)]
        keyboard.append([InlineKeyboardButton("🔙 Back", callback_data="order_food")])
        
        await query.edit_message_text(
            f"🍔 <b>{restaurant_name}</b>\n\n"
            "Select an item:",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='HTML'
        )
        return FOOD_ITEM
        
    elif query.data.startswith("food_"):
        parts = query.data.split("_")
        restaurant_index = int(parts[1])
        item_index = int(parts[2])
        
        restaurant_names = ["Pizza Express", "Noodles House", "Fried Chicken Co", "Healthy Bites", "Sushi Station"]
        restaurant_name = restaurant_names[restaurant_index]
        
        order_id = str(uuid.uuid4())[:8].upper()
        order = {
            'id': order_id,
            'user_id': user_id,
            'type': 'Food',
            'restaurant': restaurant_name,
            'status': 'Preparing',
            'eta': '25-30 min',
            'created_at': datetime.now()
        }
        orders[order_id] = order
        
        await query.edit_message_text(
            f"✅ <b>Order Placed!</b>\n\n"
            f"Order ID: <b>{order_id}</b>\n"
            f"Restaurant: {restaurant_name}\n"
            f"Status: 👨‍🍳 Preparing\n"
            f"Estimated delivery: 25-30 minutes\n\n"
            f"You can track your order anytime!",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("📦 Track Order", callback_data="track_order"),
                InlineKeyboardButton("🔙 Menu", callback_data="main_menu")
            ]]),
            parse_mode='HTML'
        )
        return ConversationHandler.END
        
    elif query.data == "topup":
        await query.edit_message_text(
            "💵 <b>Top Up Wallet</b>\n\n"
            "Select amount:",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("RM 20", callback_data="topup_20"),
                    InlineKeyboardButton("RM 50", callback_data="topup_50")
                ],
                [
                    InlineKeyboardButton("RM 100", callback_data="topup_100"),
                    InlineKeyboardButton("RM 200", callback_data="topup_200")
                ],
                [InlineKeyboardButton("🔙 Back", callback_data="my_wallet")]
            ]),
            parse_mode='HTML'
        )
        
    elif query.data.startswith("topup_"):
        amount = float(query.data.split("_")[1])
        if user_id not in user_data:
            user_data[user_id] = {'wallet_balance': 50.00}
        user_data[user_id]['wallet_balance'] += amount
        
        await query.edit_message_text(
            f"✅ <b>Top Up Successful!</b>\n\n"
            f"Amount: RM {amount:.2f}\n"
            f"New Balance: RM {user_data[user_id]['wallet_balance']:.2f}\n\n"
            f"Thank you for using GrabPay!",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🔙 Back to Wallet", callback_data="my_wallet")
            ]]),
            parse_mode='HTML'
        )


async def handle_ride_pickup(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle ride pickup location input."""
    pickup = update.message.text if update.message else "Current Location"
    context.user_data['pickup'] = pickup
    
    await update.message.reply_text(
        f"📍 Pickup: {pickup}\n\n"
        "Now please share your destination.\n"
        "Type your destination address:"
    )
    return RIDE_DESTINATION


async def handle_ride_destination(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle ride destination input."""
    destination = update.message.text
    pickup = context.user_data.get('pickup', 'Current Location')
    
    # Simulate ride booking
    order_id = str(uuid.uuid4())[:8].upper()
    order = {
        'id': order_id,
        'user_id': update.effective_user.id,
        'type': 'Ride',
        'pickup': pickup,
        'destination': destination,
        'status': 'On the way',
        'eta': '8-12 min',
        'driver': 'Ahmad B.',
        'vehicle': 'Honda City ABC1234',
        'created_at': datetime.now()
    }
    orders[order_id] = order
    
    await update.message.reply_text(
        f"🚗 <b>Ride Booked!</b>\n\n"
        f"Order ID: <b>{order_id}</b>\n"
        f"Pickup: {pickup}\n"
        f"Destination: {destination}\n"
        f"Driver: {order['driver']}\n"
        f"Vehicle: {order['vehicle']}\n"
        f"Status: 🚗 On the way\n"
        f"ETA: 8-12 minutes\n\n"
        f"Your driver is on the way!",
        reply_markup=get_main_menu(),
        parse_mode='HTML'
    )
    
    context.user_data.clear()
    return ConversationHandler.END


async def handle_support(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle support issue."""
    issue = update.message.text
    await update.message.reply_text(
        f"📞 <b>Support Request Received</b>\n\n"
        f"Thank you for contacting Grab Support.\n\n"
        f"Your issue: {issue}\n\n"
        f"Our team will get back to you within 24 hours.\n"
        f"Reference ID: {str(uuid.uuid4())[:8].upper()}\n\n"
        f"For urgent matters, call: 1300-GRAB",
        reply_markup=get_main_menu(),
        parse_mode='HTML'
    )
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancel the current conversation."""
    await update.message.reply_text(
        "Operation cancelled. Use /menu to see options.",
        reply_markup=get_main_menu()
    )
    context.user_data.clear()
    return ConversationHandler.END


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send help message."""
    help_text = (
        "🤖 <b>Grab Bot Commands</b>\n\n"
        "/start - Start the bot\n"
        "/menu - Show main menu\n"
        "/help - Show this help\n"
        "/cancel - Cancel current operation\n\n"
        "💡 <b>Tips:</b>\n"
        "• Use inline buttons for quick actions\n"
        "• Track your orders anytime\n"
        "• Check promotions for great deals!\n\n"
        "Need help? Contact support via the menu!"
    )
    await update.message.reply_html(help_text, reply_markup=get_main_menu())


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle regular text messages."""
    user_message = update.message.text.lower()
    user = update.effective_user
    
    responses = {
        'hi': f"Hi {user.first_name}! How can I help you today?",
        'hello': f"Hello {user.first_name}! What would you like to do?",
        'thanks': "You're welcome! Anything else I can help with?",
        'bye': "Goodbye! Have a great day! 🚗"
    }
    
    response = responses.get(user_message, 
        f"Hi {user.first_name}! I'm here to help. "
        "Use /menu to see all available services.")
    
    await update.message.reply_text(response, reply_markup=get_main_menu())


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a telegram message."""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)
    
    if isinstance(update, Update) and update.message:
        try:
            await update.message.reply_text(
                "Sorry, something went wrong. Please try again or use /menu.",
                reply_markup=get_main_menu()
            )
        except:
            pass


async def post_init(application: Application) -> None:
    """Delete webhook if it exists."""
    bot = application.bot
    try:
        webhook_info = await bot.get_webhook_info()
        if webhook_info.url:
            logger.info(f"Removing existing webhook: {webhook_info.url}")
            await bot.delete_webhook(drop_pending_updates=True)
            logger.info("Webhook removed successfully")
    except Exception as e:
        logger.warning(f"Error checking/removing webhook: {e}")


def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).post_init(post_init).build()

    # Ride booking conversation
    ride_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(button_handler, pattern="^book_ride$")],
        states={
            RIDE_PICKUP: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_ride_pickup)],
            RIDE_DESTINATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_ride_destination)],
        },
        fallbacks=[CommandHandler('cancel', cancel), CommandHandler('menu', menu)],
    )
    
    # Food ordering conversation
    food_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(button_handler, pattern="^order_food$|^rest_|^food_")],
        states={
            FOOD_RESTAURANT: [CallbackQueryHandler(button_handler, pattern="^rest_|^order_food$")],
            FOOD_ITEM: [CallbackQueryHandler(button_handler, pattern="^food_|^order_food$")],
        },
        fallbacks=[CommandHandler('cancel', cancel), CommandHandler('menu', menu)],
    )
    
    # Support conversation
    support_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(button_handler, pattern="^support$")],
        states={
            SUPPORT_ISSUE: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_support)],
        },
        fallbacks=[CommandHandler('cancel', cancel), CommandHandler('menu', menu)],
    )

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("cancel", cancel))
    
    application.add_handler(ride_handler)
    application.add_handler(food_handler)
    application.add_handler(support_handler)
    
    # Button callback handler (must be after conversation handlers)
    application.add_handler(CallbackQueryHandler(button_handler))
    
    # Handle all other text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Register error handler
    application.add_error_handler(error_handler)

    # Start the bot
    logger.info("Starting Grab bot...")
    logger.info("Bot is now listening for messages...")
    application.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)


if __name__ == '__main__':
    main()
