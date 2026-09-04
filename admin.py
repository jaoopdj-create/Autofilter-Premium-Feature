import os
from pyrogram import filters

def register_admin(app, db):
    owner_id = int(os.getenv("OWNER_ID", "0"))

    @app.on_message(filters.private & filters.command("stats"))
    async def stats(_, message):
        if message.from_user.id != owner_id:
            return
        await message.reply_text(f"Indexed files: {db.count()}")

    @app.on_message(filters.private & filters.command("broadcast"))
    async def broadcast(_, message):
        if message.from_user.id != owner_id:
            return
        if len(message.command) < 2:
            await message.reply_text("Use: /broadcast message")
            return
        await message.reply_text(
            "Broadcast module is intentionally left disabled in this starter. "
            "Add your own user-consent and rate-limit checks before enabling it."
        )
