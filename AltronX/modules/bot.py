import os
import sys
import heroku3
from datetime import datetime
from config import MK1, MK2, MK3, MK4, MK5 , MK6, MK7, MK8, MK9, MK10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        altron = await e.reply(f"» #​𓆩ℂ𝕐𝔹𝔼ℝ𝔻ℝ𝔸𝔾𝕆ℕ𝕊𓆪_ᴏɴ_ᴛᴏᴘ⚡", parse_mode=None, link_preview=None)
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await altron.edit(f"__🤖𝐂𝐃 𝐒𝐏𝐀𝐌𝐌𝐄𝐑𝐒 𝐃𝐔𝐒𝐇𝐌𝐀𝐍 𝐊𝐈 𝐌𝐀𝐀 𝐂𝐇𝐎𝐃𝐍𝐄 𝐊𝐎 𝐓𝐀𝐈𝐘𝐀𝐑 𝐇𝐀𝐈 #𝐂𝐘𝐁𝐄𝐑𝐃𝐑𝐀𝐆𝐎𝐍𝐒_𝐎𝐍_𝐓𝐎𝐏⚡ __\n» `{mp} ms`")


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"𝗦𝗕𝗥 𝗞𝗥𝗢 𝗧𝗛𝗢𝗗𝗔 𝗕𝗢𝗦𝗦🥵! 𝗕𝗢𝗧𝗥𝗘𝗦𝗧𝗔𝗥𝗧 𝗛𝗢𝗥𝗘 𝗖𝗗⚡ 𝗞𝗘 𝗗𝗨𝗦𝗛𝗠𝗔𝗡𝗢 𝗞𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗡𝗘 𝗞𝗢😈")
        try:
            await MK1.disconnect()
        except Exception:
            pass
        try:
            await MK2.disconnect()
        except Exception:
            pass
        try:
            await MK3.disconnect()
        except Exception:
            pass
        try:
            await MK4.disconnect()
        except Exception:
            pass
        try:
            await MK5.disconnect()
        except Exception:
            pass
        try:
            await MK6.disconnect()
        except Exception:
            pass
        try:
            await MK7.disconnect()
        except Exception:
            pass
        try:
            await MK8.disconnect()
        except Exception:
            pass
        try:
            await MK9.disconnect()
        except Exception:
            pass
        try:
            await MK10.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        

Heroku = heroku3.from_key(HEROKU_API_KEY)
sudousers = os.environ.get("SUDO_USER", None)

@MK1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply(f"» _𝗔𝗗𝗗𝗜𝗡𝗚 𝗔 𝗡𝗘𝗪 𝗦𝗨𝗗𝗢 𝗨𝗦𝗘𝗥 𝗜𝗡 𝗦𝗨𝗗𝗢 𝗟𝗜𝗦𝗧 𝗕𝗢𝗦𝗦⚡⚡⚡ 𝗜𝗧 𝗪𝗜𝗟𝗟 𝗧𝗔𝗞𝗘 𝗔 𝗕𝗜𝗧 𝗧𝗜𝗠𝗘 𝗙𝗢𝗥 𝗕𝗢𝗧𝗦 𝗧𝗢 𝗥𝗘𝗦𝗧𝗔𝗥𝗧☹️🤧__")
        mks = "SUDO_USER"
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except Exception:
            await ok.edit("» 𝗝𝗜𝗦𝗞𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗡𝗜 𝗨𝗦𝗦𝗘 𝗥𝗘𝗣𝗟 𝗞𝗥𝗞𝗞𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗 𝗗𝗢 𝗕𝗢𝗦𝗦😪😪 !!")
        if len(sudousers) > 0:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"» **𝖭𝖤𝖶 𝖢𝖮𝖬𝖬𝖠𝖭𝖣𝖤𝖱**: `{target}`\n» 𝗕𝗢𝗧𝗦 𝗔𝗥𝗘 𝗥𝗘𝗦𝗧𝗔𝗥𝗧𝗜𝗡𝗚 𝗜𝗡 𝗙𝗘𝗪 𝗠𝗜𝗡𝗨𝗧𝗘𝗦 ⚡⚡⚡...`")
        heroku_var[mks] = newsudo   
   
     
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(GetFullUserRequest(previous_message.forward.sender_id))
        else:
            replied_user = await event.client(GetFullUserRequest(previous_message.sender_id))
    return replied_user.user.id
