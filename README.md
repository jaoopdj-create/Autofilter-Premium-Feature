# Advanced AutoFilter Premium Bot

A modular Telegram bot starter for indexing and searching files from channels.

## Features
- Pyrogram-based bot
- MongoDB storage
- Channel file indexing
- Inline-style text search through `/search`
- Admin commands
- Environment-based secrets
- Render deployment support

## Setup
1. Create a bot with BotFather.
2. Get API ID and API HASH from my.telegram.org.
3. Create a MongoDB database.
4. Copy `.env.example` to `.env` and fill values.
5. Install dependencies:
   `pip install -r requirements.txt`
6. Run:
   `python bot.py`

Never commit `.env` or bot tokens.
