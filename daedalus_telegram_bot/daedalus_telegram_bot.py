import os
import logging
import textwrap

from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update, ParseMode
from dotenv import load_dotenv


def setup_logger():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def main():
    load_dotenv()
    setup_logger()

    bot_token = os.getenv("BOT_TOKEN")
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    message_handler = MessageHandler(Filters.all, unknown_command)
    dispatcher.add_handler(message_handler)

    updater.start_polling()


def start(update: Update, context: CallbackContext):
    logging.info("Received start command from %s, chat_id %s", update.effective_user.username, update.effective_chat.id)
    text = textwrap.dedent(f"""
        Hello\\! I am the Daedalus Telegram Bot\\.
        I don't have any commands yet\\.
        Please give this chat id to Jurriaan: `{update.effective_chat.id}`
    """)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        parse_mode=ParseMode.MARKDOWN_V2
    )


def unknown_command(update: Update, context: CallbackContext):
    logging.warning(
        "Received unknown command from %s, chat_id %s",
        update.effective_user.username,
        update.effective_chat.id
    )
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm sorry, I don't understand that command.\nI only respond to /start"
    )


if __name__ == "__main__":
    main()
