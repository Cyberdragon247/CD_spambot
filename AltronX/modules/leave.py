from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10, SUDO_USERS, CMD_HNDLR as hl
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon import events

@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
async def leave(e):
    if e.sender_id in SUDO_USERS:
        mkl = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)

        if len(e.text) > 7:
            event = await e.reply("» ʟᴇᴀᴠɪɴɢ...")
            try:
                await event.client(LeaveChannelRequest(int(mkl[0])))
            except Exception as e:
                await event.edit(str(e))
        else:
             if e.is_private:
                  alt = f"» 𝐘𝐎𝐔 𝐂𝐀𝐍'𝐓 𝐃𝐎 𝐓𝐇𝐈𝐒 𝐇𝐄𝐑𝐄 𝐁𝐎𝐒𝐒!🤧 !!\n\n» {hl}leave <ᴄʜᴀɴɴᴇʟ/ᴄʜᴀᴛ ɪᴅ> \n» {hl}leave : 𝐓𝐘𝐏𝐄 𝐈𝐍 𝐓𝐇𝐄 𝐆𝐑𝐎𝐔𝐏 𝐀𝐍𝐃 𝐁𝐎𝐓 𝐖𝐈𝐋𝐋 𝐀𝐔𝐓𝐎 𝐋𝐄𝐀𝐕𝐄 𝐓𝐇𝐄 𝐆𝐑𝐎𝐔𝐏😏."
                  await e.reply(alt)
             else:
                  event = await e.reply("» 𝐉𝐀𝐑𝐀 𝐇𝐔 𝐘𝐇𝐀 𝐒𝐄 🥺😩! 𝐀𝐋𝐖𝐈𝐃𝐀 𝐃𝐎𝐒𝐓𝐎𝐍 𝐃𝐔𝐀 𝐌𝐄 𝐘𝐀𝐀𝐃 𝐑𝐊𝐇𝐍𝐀 😌 #𝐂𝐘𝐁𝐄𝐑𝐃𝐑𝐀𝐆𝐎𝐍𝐒_𝐎𝐍_𝐓𝐎𝐏 ⚡⚡⚡...")
                  try:
                      await event.client(LeaveChannelRequest(int(e.chat_id)))
                  except Exception as e:
                      await event.edit(str(e))
