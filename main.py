import os
from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import asyncio

# API ma'lumotlari ENV-dan olinadi
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH"))
BOT_PHONE = os.environ.get("BOT_PHONE")  # telefon raqam ENV-dan olinadi

# Session nomi va client
client = TelegramClient("userbot", API_ID, API_HASH).start(phone=BOT_PHONE)

# Soat style (bezakli)
def get_clock():
    return datetime.now().strftime("⏰ %H:%M | %d-%m-%Y ✨")

# Har 1 daqiqada profil nomini o‘zgartiradi
async def update_name():
    while True:
        name = get_clock()
        try:
            await client(UpdateProfileRequest(first_name=name))
        except Exception as e:
            print("Xato:", e)
        await asyncio.sleep(60)

# Avto-javob (Lickada)
@client.on(events.NewMessage(pattern="licka"))
async def handler(event):
    await event.reply("🤖 Salom! Men avto-javob botman ✨")

# Botni ishga tushurish
async def main():
    await client.start(phone=BOT_PHONE)
    print("✅ Userbot ishlayapti...")
    await update_name()

with client:
    client.loop.run_until_complete(main())
