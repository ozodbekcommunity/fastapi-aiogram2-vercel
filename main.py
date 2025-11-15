# main.py
# FastAPI webhook serveri (Vercel serverless muhitiga mos)

from fastapi import FastAPI, Request
from bot import dp, bot
import asyncio

app = FastAPI()

# Webhook URL (Vercel deploy linkini qo‘yasiz)
WEBHOOK_URL = "https://YOUR_PROJECT_NAME.vercel.app/api/webhook"


@app.on_event("startup")
async def on_startup():
    # Webhook o‘rnatish
    await bot.set_webhook(WEBHOOK_URL)


@app.post("/api/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()

    asyncio.create_task(dp.process_update(dp.updates_factory(data)))

    return {"status": "ok"}


@app.get("/")
async def home():
    return {"status": "Bot is running"}