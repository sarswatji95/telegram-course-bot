import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Kota", callback_data='kota')],
        [InlineKeyboardButton("Jaipur", callback_data='jaipur')],
        [InlineKeyboardButton("Sikar", callback_data='sikar')]
    ]
    await update.message.reply_text(
        "📍 City Select karo:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# BUTTON HANDLER
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'kota':
        keyboard = [
            [InlineKeyboardButton("Allen", callback_data='allen')],
            [InlineKeyboardButton("Resonance", callback_data='resonance')]
        ]
        await query.edit_message_text(
            "🏫 Coaching Select karo:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == 'allen':
        keyboard = [
            [InlineKeyboardButton("NEET", callback_data='neet')],
            [InlineKeyboardButton("JEE", callback_data='jee')]
        ]
        await query.edit_message_text(
            "📚 Course Select karo:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == 'neet':
        await query.edit_message_text(
            "🎯 NEET Free Content:\n\n"
            "📺 YouTube: https://youtube.com\n"
            "📄 Notes: https://drive.google.com"
        )

    elif query.data == 'jee':
        await query.edit_message_text(
            "🚀 JEE Free Content:\n\n"
            "📺 YouTube: https://youtube.com\n"
            "📄 Notes: https://drive.google.com"
        )

# MAIN FUNCTION
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot started ✅")
    await app.run_polling()

# RUN BOT (FIXED EVENT LOOP)
if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
