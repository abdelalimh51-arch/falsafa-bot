import asyncio
import os
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes

TOKEN = "8046169927:AAHIUWTllO-LNUtehCjJwx9P3fU4UFrwnpo"
CHAT_ID = "-1003928019134"
ADMIN_ID = 8230499004  # ID تاعك أنت

VIDEOS = [
    "https://www.youtube.com/watch?v=w7cyYBWnP-E",
    "https://www.youtube.com/watch?v=zWXSjfWkHlE&t=2s",
    "https://www.youtube.com/watch?v=UD3n0hWoOWY",
    "https://www.youtube.com/watch?v=4q_npbS8F5E",
    "https://www.youtube.com/watch?v=t-PfIN6wYC8",
    "https://www.youtube.com/watch?v=pZnRfBZKAd8&t=1s",
    "https://www.youtube.com/watch?v=VA7WXXFPRJc",
    "https://www.youtube.com/watch?v=YhbCQ8aWHBQ&t=962s",
]

admin_message = "📝 برافو! دابا اكتب ملخصك وارسله في الجروب!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_ID:
        await update.message.reply_text("البوت شغال ✅")

async def setmessage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global admin_message
    if update.effective_user.id == ADMIN_ID:
        admin_message = " ".join(context.args)
        await update.message.reply_text(f"✅ الرسالة تبدلت:\n{admin_message}")

async def sendvideo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_ID:
        bot = Bot(TOKEN)
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("✅ تفرجت!", callback_data="done")],
            [InlineKeyboardButton("⏳ مزال ما تفرجتش", callback_data="not_yet")]
        ])
        await bot.send_message(chat_id=CHAT_ID, text=f"🎬 فيديو هذا الأسبوع:\n{VIDEOS[0]}")
        await bot.send_message(chat_id=CHAT_ID, text="واش تفرجت؟", reply_markup=keyboard)
        await update.message.reply_text("✅ الفيديو تبعث!")

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "done":
        await query.from_user.send_message(admin_message)
    elif query.data == "not_yet":
        await query.from_user.send_message("⏰ متنساش تتفرج قبل نهاية الأسبوع!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("setmessage", setmessage))
app.add_handler(CommandHandler("sendvideo", sendvideo))
app.add_handler(CallbackQueryHandler(button))
app.run_polling()
