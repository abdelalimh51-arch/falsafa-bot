import asyncio
from telegram import Bot

TOKEN = "8046169927:AAHIUWTllO-LNUtehCjJwx9P3fU4UFrwnpo"
CHAT_ID = "-5151491349"

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

async def send_video():
    bot = Bot(TOKEN)
    video = VIDEOS[0]
    await bot.send_message(chat_id=CHAT_ID, text=f"🎬 فيديو هذا الأسبوع:\n{video}")
    await bot.send_message(chat_id=CHAT_ID, text="📝 بعد ما تشوفو الفيديو، ارسلو مقالتكم هنا!")

asyncio.run(send_video())
