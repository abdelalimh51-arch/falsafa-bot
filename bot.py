import asyncio
from telegram import Bot
import schedule
import time
import threading

TOKEN = "8046169927:AAGS9sHzCaBfHRTyQhjClG1l8F6iWHLL0c4"
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

current_video = [0]

async def send_video():
    bot = Bot(TOKEN)
    if current_video[0] < len(VIDEOS):
        video = VIDEOS[current_video[0]]
        await bot.send_message(chat_id=CHAT_ID, text=f"🎬 فيديو هذا الأسبوع:\n{video}")
        await bot.send_message(chat_id=CHAT_ID, text="📝 بعد ما تشوفو الفيديو، ارسلو مقالتكم هنا!")
        current_video[0] += 1

def run_schedule():
    schedule.every().saturday.at("10:00").do(lambda: asyncio.run(send_video()))
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    threading.Thread(target=run_schedule).start()
    print("البوت شغال ✅")
