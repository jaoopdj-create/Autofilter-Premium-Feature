import os
from datetime import datetime
from pyrogram import filters

def register_indexer(app, db):
    allowed = {
        int(x.strip())
        for x in os.getenv("INDEX_CHANNELS", "").split(",")
        if x.strip()
    }

    @app.on_message(filters.channel & (filters.document | filters.video | filters.audio))
    async def index_file(_, message):
        if allowed and message.chat.id not in allowed:
            return

        media = message.document or message.video or message.audio
        name = getattr(media, "file_name", None) or "unnamed_file"

        db.add_file({
            "file_unique_id": media.file_unique_id,
            "file_id": media.file_id,
            "name": name,
            "size": getattr(media, "file_size", 0),
            "chat_id": message.chat.id,
            "message_id": message.id,
            "mime_type": getattr(media, "mime_type", None),
            "created_at": datetime.utcnow(),
        })
