from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import asyncio

# API ma'lumotlari
API_ID = 21716532
API_HASH = "4a9ea732220e7d827166f5b0780426c4"

# Sessiya fayli oldin lokalda yaratildi, input so‘ramaydi
client = TelegramClient("userbot", API_ID, API_HASH)

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
    await event.reply("🤖 Salom! Men avto-javob botman Tez orada javob yoziladi✨")

# Botni ishga tushurish
async def main():
    await client.start()  # endi kod so‘ramaydi
    print("✅ Userbot ishlayapti...")
    await update_name()

with client:
    client.loop.run_until_complete(main())
