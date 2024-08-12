import os
from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
# Load environment variables
load_dotenv()

ENV_TELEGRAM_BOT_TOKEN = os.getenv('ENV_TELEGRAM_BOT_TOKEN')
TOKEN = ENV_TELEGRAM_BOT_TOKEN
WEB_APP_URL = "https://blink-mini.vercel.app/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Open Web App", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Click the button to open the web app:", reply_markup=reply_markup)

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
    
    
# python3 -m venv myenv
# source myenv/bin/activate   
# python3 main.py