from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8218185046:AAFrTce_i56f8kjPMeMMtfCAiqIzUXPm2Yg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Salom! KiberS UZB ga xush kelibsiz!\n\n"
        "📚 Kurslarimiz:\n"
        "🛡️ Kiberxavfsizlik Asoslari — 3 oy\n"
        "💻 Frontend Dasturlash — 4 oy\n"
        "⚙️ Python Backend — 4 oy\n"
        "🔍 Penetration Testing — 5 oy\n\n"
        "📝 Kursga yozilish: https://t.me/aza_13_09\n"
        "✈️ Kanal: @kibers_uzb\n"
        "📞 Tel: +998 87 811 32 30"
    )

async def xabar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Savollaringiz uchun:\n"
        "📞 +998 87 811 32 30\n"
        "✈️ @aza_13_09"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, xabar))
app.run_polling()
