# bot.py
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command

BOT_TOKEN = "8377704874:AAGSHaqX1b37EFx_lXGoBDvkcf_6QEsNHAM"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

@router.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Salom! Aiogram 3 + FastAPI serverless bot ishlayapti 🚀")
