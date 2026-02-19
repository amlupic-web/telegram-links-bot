import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

SPREADSHEET_ID = "ВСТАВЬ_СЮДА_ID_ТАБЛИЦЫ"

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json", scope
)
client = gspread.authorize(creds)
sheet = client.open_by_key(SPREADSHEET_ID).sheet1


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот работает. Пришли ссылку.")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    link = update.message.text
    sheet.append_row([link])
    await update.message.reply_text("Ссылка сохранена ✅")


app = ApplicationBuilder().token("ВСТАВЬ_СЮДА_BOT_TOKEN").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
