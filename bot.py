# bot.py
# Aiogram 2.25.1 konfiguratsiyasi

from aiogram import Bot, Dispatcher, types

# Bot tokenini shu yerga qo‘ying
BOT_TOKEN = "8377704874:AAGSHaqX1b37EFx_lXGoBDvkcf_6QEsNHAM"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer("Salom! Serverless FastAPI + Aiogram 2.25.1 bot ishlayapti 🚀")