from pyrogram import filters
from pyrogram.types import Message

from ProMusic import app
from ProMusic.core.call import Pro

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await Pro.stop_stream_force(message.chat.id)
