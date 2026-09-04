from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def register_search(app, db):
    @app.on_message(filters.private & filters.command("search"))
    async def search_command(_, message):
        if len(message.command) < 2:
            await message.reply_text("Use: /search filename")
            return

        query = " ".join(message.command[1:])
        results = db.search(query)

        if not results:
            await message.reply_text("No matching files found.")
            return

        buttons = []
        for item in results:
            buttons.append([
                InlineKeyboardButton(
                    item["name"][:60],
                    callback_data=f"file:{item['chat_id']}:{item['message_id']}"
                )
            ])

        await message.reply_text(
            f"Found {len(results)} result(s):",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    @app.on_callback_query(filters.regex(r"^file:-?\d+:\d+$"))
    async def send_file(_, query):
        _, chat_id, message_id = query.data.split(":")
        await query.answer("Preparing file...")
        await app.copy_message(
            chat_id=query.from_user.id,
            from_chat_id=int(chat_id),
            message_id=int(message_id)
        )
