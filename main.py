import os

from dotenv import load_dotenv

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.effective_chat.id,
    )


def main():
    load_dotenv()

    application = ApplicationBuilder().token(os.getenv("TOKEN")).build()

    start_handler = CommandHandler("id", start)
    application.add_handler(start_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
