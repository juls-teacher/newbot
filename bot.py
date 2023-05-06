import os
import logging


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(
        f"Message from chat #{update.effective_user.first_name}"
        f" username {update.effective_chat.id}"
                )
    await update.message.reply_text(
        f"Hello {update.effective_user.first_name} ({update.effective_chat.id})"
    )

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(
        f"Message from chat #{update.effective_user.first_name}"
        f" username {update.effective_chat.id}"
                )
    await update.message.reply_text(
        f"Hello {update.effective_user.first_name} ({update.effective_chat.id})"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(~filters.COMMAND, message))
    app.run_polling()

