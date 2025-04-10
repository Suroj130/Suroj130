from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime

# Bot config
api_id = 123456  # Replace with your API ID
api_hash = "your_api_hash"
bot_token = "your_bot_token"

app = Client("BrandrdXMusic", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# When someone starts the bot in private
@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    user = message.from_user
    text = (
        "**ᴮʳᵃⁿᵈʳᵈˣᴹᵘˢⁱᶜ JUST STARTED THE BOT.**\n\n"
        f"**USER ID :** `{user.id}`\n"
        f"**USERNAME :** @{user.username if user.username else 'No username'}"
    )
    await message.reply_text(text)

# When bot is added to a group
@app.on_message(filters.new_chat_members)
async def group_welcome(client, message: Message):
    for member in message.new_chat_members:
        if member.is_self:
            now = datetime.now().strftime("%d %B %Y")
            time_now = datetime.now().strftime("%I:%M %p")
            welcome_text = (
                "**⚔️ NEW RECRUIT ARRIVES ⚔️**\n\n"
                f"▌**NAME :** ᴮʳᵃⁿᵈʳᵈˣᴹᵘˢⁱᶜ\n"
                f"▌**DATE :** {now}\n"
                f"▌**TIME :** {time_now} IST\n\n"
                "**NEW RECRUIT. NEW HOPE.**\n"
                "**THE WINGS OF FREEDOM FLAP AGAIN...**\n"
                "**SHINZOU WO SASAGEYO!**"
            )
            await message.reply_text(welcome_text)

app.run()