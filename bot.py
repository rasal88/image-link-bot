from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

BOT_OWNER_ID = 7241898482  # baad me apna Telegram User ID daalna

pending_links = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Image Link Bot Ready\n\n"
        "Link bhejo, phir image bhejo."
    )

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != BOT_OWNER_ID:
        return

    text = update.message.text.strip()

    if text.startswith("http://") or text.startswith("https://"):
        pending_links[update.effective_user.id] = text
        await update.message.reply_text(
            "Link received. Ab image bhejo."
        )

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != BOT_OWNER_ID:
        return

    user_id = update.effective_user.id

    if user_id in pending_links:
        link = pending_links[user_id]

        await update.message.reply_text(
            f"Demo Save Success\n\nLink:\n{link}"
        )

        del pending_links[user_id]
    else:
        await update.message.reply_text(
            "Abhi search system add karenge."
        )

def main():
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_text))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    app.run_polling()

if __name__ == "__main__":
    main()
