from telethon import events, Button
from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10
from AltronX.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("☆ 𝐂ᴏᴍᴍᴀɴᴅs ☆", data="help_back")
        ],
        [
        Button.url("☆ 𝐂ʜᴀɴɴᴇʟ ☆", "https://t.me/CD_CYBERDRAGONS"),
        Button.url("☆ 𝐒ᴜᴘᴘᴏʀᴛ", "https://t.me/CD_CHATS")
        ],
        [
        Button.url("☆ 𓆩𝐂ᴅ𓆪_𝐗_𝐍𝐄𝐓𝐖𝐎𝐑𝐊", "https://t.me/CD_NETWORK")
        ]
        ]


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        BotName = AltBot.first_name
        BotId = AltBot.id
        TEXT = f"**𝐇𝐞𝐲 [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n𝐈 𝐀ᴍ [{BotName}](tg://user?id={BotId})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **✦ 𝐃ᴇᴠᴇʟᴏᴘᴇᴅ 𝐁ʏ :~ [𝐍ᴇᴏ𝑵𝑋 ⚡𓆩𝐂ᴅ𓆪](https://t.me/LORD_NEONX)**\n\n"
        TEXT += f"» **𝐂𝐃 𝐒𝐏𝐀𝐌 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 :** `3.2`\n"
        TEXT += f"» **𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍 𝐕𝐄𝐑𝐒𝐈𝐎𝐍:** `{telethon.__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                event.chat_id,
                "https://te.legra.ph/file/5ae11cd68886afe7145d2.jpg",
                caption=TEXT, 
                buttons=PythonButton)
