from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# /start command handler
async def start(update, context):
    message = (
        "👋 Hello, welcome to *RaidenPay*!\n\n"
        "With RaidenPay, you can send and receive USDT on Polygon, "
        "and also send funds directly to your local bank account.\n\n"
        "We're glad to have you here 💚"
    )
    
    # Buttons
    keyboard = [
        [InlineKeyboardButton("💸 Send", callback_data='send')],
        [InlineKeyboardButton("📥 Receive", callback_data='receive')],
        [InlineKeyboardButton("🏦 Cashout", callback_data='cashout')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(message, reply_markup=reply_markup, parse_mode="Markdown")

# Button handler
async def button_handler(update, context):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'send':
        await query.edit_message_text(text="You clicked *Send*! (Send logic goes here)", parse_mode="Markdown")
    elif query.data == 'receive':
        await query.edit_message_text(text="You clicked *Receive*! (Receive logic goes here)", parse_mode="Markdown")
    elif query.data == 'cashout':
        await query.edit_message_text(text="You clicked *Cashout*! (Cashout logic goes here)", parse_mode="Markdown")

# Main function
def main():
    # Replace with your BotFather token
    app = ApplicationBuilder().token("8598638419:AAH5tcQp5iEEt3h9sDXxnIJlyigkjKpdv3Y").build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    # Start the bot
    app.run_polling()

# Run the bot
if __name__ == "__main__":
    main()
    