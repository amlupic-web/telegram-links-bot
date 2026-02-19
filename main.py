import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

SPREADSHEET_ID = "10ffqEkVaBHjtiROjlullxrGKu5yM8S_CUUcK_U_lXbc"

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


app = ApplicationBuilder().token("8433445267:AAEsQ83xH64-78KD8CjlLZ-ln6-ElaD8tG8").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
