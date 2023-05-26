from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""Hᴇʏ {msg.from_user.mention},

Tʜɪs ɪs {me2},
𝐈𝐍𝐓𝐙𝐀𝐑 𝐍𝐀𝐇𝐈 𝐇𝐄 𝐊𝐈𝐒𝐈 𝐑𝐀𝐍𝐈 𝐊𝐀 𝐀𝐁 𝐇𝐀𝐌 𝐁𝐀𝐓𝐀𝐘𝐄𝐍𝐆𝐄 𝐑𝐔𝐓𝐁𝐀 𝐊𝐘𝐀 𝐇𝐎𝐓𝐀 𝐇𝐄 𝐉𝐀𝐕𝐀𝐍𝐈 𝐊𝐀 ..!! 🚬🦋💫
ᴊɪsᴋᴇ ᴊᴀɪʙ ᴍᴇ ɢᴀɴᴅʜɪ  ᴄʜᴏʀɪ ᴜsᴋᴇ ᴘʏᴀᴀʀ ᴍᴇ ᴀᴀɴᴅʜɪ 🖤.

Mᴀᴅᴇ ᴡɪᴛʜ ❤ ʙʏ : [𝗕𝗥𝗔𝗡𝗗𝗘𝗗 𓆩🇽𓆪 𝗞𝗜𝗡𝗚](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="✌ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ ✌", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("😊 sᴏᴜʀᴄᴇ 😊", url="https://t.me/BRANDED_LINK"),
                    InlineKeyboardButton("🙌 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🙌", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
