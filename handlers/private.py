from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("2_5271914077705212510.tgs")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [AlphaElias](https://t.me/AlphaElias).

Add me to your group and play music freely!

Commands 🛠
For all in group
/play - reply to youtube url or song file to play song
/ytp <song name> - play song without youtube url or song file (best method)
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
Admins only
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://github.com/Infinity-Bots/GroupMusicPlayerBot")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/AndroisCave"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/AndroidCave"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/AlphaMusicXD_Bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Infinity_BOTs")
                ]
            ]
        )
   )


