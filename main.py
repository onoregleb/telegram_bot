import nest_asyncio
nest_asyncio.apply()

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import asyncio


scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Замените 'path' на путь к вашему JSON файлу с учетными данными
creds = ServiceAccountCredentials.from_json_keyfile_name('path', scope)
client = gspread.authorize(creds)

spreadsheet = client.open("test")  # Замените на имя вашей таблицы
sheet = spreadsheet.sheet1

# Функция, которая срабатывает при нажатии на /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Добрый день, вы можете оставить обратную связь")

# Функция, которая срабатывает при получении сообщения
async def handle_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    feedback = update.message.text
    response_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    username = user.username if user.username else user.first_name

    # Сохранение данных в Google Таблицу
    sheet.append_row([feedback, response_time, username])

    await update.message.reply_text("Спасибо за обратную связь")

async def main() -> None:
    # Замените 'YOUR_TOKEN' на токен вашего бота
    app = ApplicationBuilder().token("YOUR_TOKEN").build()

    # Обработчик команды /start
    app.add_handler(CommandHandler("start", start))

    # Обработчик текстовых сообщений
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_feedback))

    # Запуск бота
    await app.run_polling()

# Запуск основного цикла
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if "This event loop is already running" in str(e):
            asyncio.create_task(main())
        else:
            raise e
