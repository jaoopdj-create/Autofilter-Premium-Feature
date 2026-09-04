import asyncio
import logging
import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message

from database import FileDB
from plugins.indexer import register_indexer
from plugins.search import register_search
from plugins.admin import register_admin

load_dotenv()
logging.basicConfig(level=logging.INFO)

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
BOT_TOKEN = os.environ["BOT_TOKEN"]

db = FileDB(
    os.environ["MONGO_URI"],
    os.getenv("DATABASE_NAME", "autofilter")
)

app = Client(
    "advanced_autofilter_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=20
)

register_indexer(app, db)
register_search(app, db)
register_admin(app, db)

@app.on_message(filters.private & filters.command("start"))
async def start(_, message: Message):
    await message.reply_text(
        "Welcome! Send a search term to find indexed files.\n"
        "Use /help for commands."
    )

@app.on_message(filters.private & filters.command("help"))
async def help_command(_, message: Message):
    await message.reply_text(
        "/search <name> - search indexed files\n"
        "/stats - database statistics\n"
        "/id - show chat/user ID"
    )

@app.on_message(filters.private & filters.command("id"))
async def show_id(_, message: Message):
    await message.reply_text(
        f"User ID: `{message.from_user.id}`\n"
        f"Chat ID: `{message.chat.id}`"
    )

if __name__ == "__main__":
    app.run()
