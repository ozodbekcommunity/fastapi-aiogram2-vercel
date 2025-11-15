# main.py
from fastapi import FastAPI, Request
from bot import bot, dp
import asyncio

app = FastAPI()

WEBHOOK_PATH = "/api/webhook"
WEBHOOK_URL = "https://fastapi-aiogram3-webhook-uz.vercel.app" + WEBHOOK_PATH


@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)


@app.post(WEBHOOK_PATH)
async def webhook(request: Request):
    data = await request.json()
    asyncio.create_task(dp.feed_update(bot, data))
    return {"status": "ok"}


@app.get("/")
async def home():
    return {"status": "Bot is running"}
