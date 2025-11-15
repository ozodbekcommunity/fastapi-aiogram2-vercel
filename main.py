from fastapi import FastAPI, Request
from bot import bot, dp
from aiogram import types
import asyncio

app = FastAPI()

WEBHOOK_PATH = "/api/webhook"
WEBHOOK_URL = "https://fastapi-aiogram3-webhook-uz.vercel.app/api/webhook"


@app.post(WEBHOOK_PATH)
async def telegram_webhook(request: Request):
    data = await request.json()

    update = types.Update.model_validate(data)

    asyncio.create_task(dp.feed_update(bot, update))

    return {"ok": True}


@app.get("/")
async def home():
    return {"status": "Bot is running"}
