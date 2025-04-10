from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime

# Bot config
api_id = 123456    # Replace with your API ID
api_hash = "your_api_hash"
bot_token = "your_bot_token"

app = Client("welcome_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Start handler
@app.on_message(filters.command("start") & filters.private)
async def start(client, message: Message):
    user = message.from_user
    msg = (
        f"**ʀɪᴏ JUST STARTED THE BOT.**\n\n"
        f"**USER ID :** `{user.id}`\n"
        f"**USERNAME :** @{user.username if user.username else 'No username'}"
    )
    await message.reply(msg)

# When bot is added to a group
@app.on_message(filters.new_chat_members)
async def welcome_new_bot(client, message: Message):
    for member in message.new_chat_members:
        if member.is_self:
            now = datetime.now().strftime("%d %B %Y")
            time_now = datetime.now().strftime("%I:%M %p")
            msg = (
                "**⚔️ NEW RECRUIT ARRIVES ⚔️**\n\n"
                f"▌**NAME :** AOT BEATS • | 🎀\n"
                f"▌**DATE :** {now}\n"
                f"▌**TIME :** {time_now} IST\n\n"
                "**NEW RECRUIT. NEW HOPE.**\n"
                "**THE WINGS OF FREEDOM FLAP AGAIN...**\n"
                "**SHINZOU WO SASAGEYO!**"
            )
            await message.reply_text(msg)

app.run()