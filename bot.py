from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes
import asyncio

TOKEN = "8046169927:AAHIUWTllO-LNUtehCjJwx9P3fU4UFrwnpo"
CHAT_ID = "-1003928019134"
ADMIN_ID = 8230499004

votes = {"yes": 0, "more": 0, "questions": 0}

async def send(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    
    if len(context.args) < 2:
        await update.message.reply_text("❌ اكتب هكذا:\n/send رابط_الفيديو موضوع_الدرس")
        return
    
    video = context.args[0]
    topic = " ".join(context.args[1:])
    
    votes["yes"] = 0
    votes["more"] = 0
    votes["questions"] = 0
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ استفدت، جاهز للمرحلة الجاية", callback_data="yes")],
        [InlineKeyboardButton("📖 نحتاج درس إضافي", callback_data="more")],
        [InlineKeyboardButton("❓ عندي أسئلة", callback_data="questions")]
    ])
    
    bot = Bot(TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text=f"🎬 فيديو هذا الأسبوع\n\n📝 الموضوع: {topic}\n\n🔗 {video}\n\nبعد ما تتفرج صوّت 👇",
        reply_markup=keyboard
    )
    await update.message.reply_text("✅ تبعث!")

async def results(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    
    bot = Bot(TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text=f"📊 نتائج هذا الأسبوع:\n\n✅ جاهزين للمرحلة الجاية: {votes['yes']}\n📖 يحتاجو درس إضافي: {votes['more']}\n❓ عندهم أسئلة: {votes['questions']}"
    )
    await update.message.reply_text("✅ النتائج تبعثات للجروب!")

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer("✅ صوتك تسجل!")
    votes[query.data] += 1

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("send", send))
app.add_handler(CommandHandler("results", results))
app.add_handler(CallbackQueryHandler(button))
app.run_polling()
