import config
from DEADLYSPAM import BOT0, deadlyversion, SUDOERS
from telethon import events, version, Button
from telethon.tl.custom import button

PIC = config.ALIVE_PIC

if config.ALIVE_PIC:
    DEADLY_PIC = PIC
else:
    DEADLY_PIC = "https://telegra.ph/file/c6f99c0b68ff07439ed72.jpg"

hl = config.CMD_HNDLR


DEADLY = "â¯ ðð²ð®ð±ð¹ð ð¦ð½ð®ðº ðð²ð¿ð² â¯\n\n"
DEADLY += f"âââââââââââââââââââ\n"
DEADLY += f"â¢ **á´Êá´Êá´É´ á´ á´ÊsÉªá´É´** : `4.0.0`\n"
DEADLY += f"â¢ **á´á´Êá´á´Êá´É´ á´ á´ÊsÉªá´É´** : `{version.__version__}`\n"
DEADLY += f"â¢ **á´á´á´á´ÊÊÊá´á´ á´ á´ÊsÉªá´É´**  : `{deadlyversion}`\n"
DEADLY += f"âââââââââââââââââââ\n\n"   


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event): 
  if event.sender_id in SUDOERS:
     Blaze = [[Button.url("á´Êá´É´É´á´Ê", "https://t.me/DEADLY_SPAMBOT"), Button.url("sá´á´á´á´Êá´", "https://t.me/DEADLY_SPAM_BOT")], [Button.url("â¢ Êá´á´á´ â¢", "https://github.com/Team-Deadly/DEADLY-SPAMBOT")]]
     await BOT0.send_file(event.chat_id, DEADLY_PIC, caption=DEADLY, buttons=Blaze) 
  else:
      await event.reply("**á´á´á´Êá´Ê Êá´á´Ê á´á´¡É´ á´á´á´á´ÊÊ-ê±á´á´á´Êá´á´!**") 
