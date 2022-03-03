from .. import Raizen
from telethon import events, custom, Button 

@Raizen.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    if event.is_private:
        await event.reply("**Hey there, this is Raizen Assistant of 𝘿𝙄𝙋𝙀𝙎𝙃!**\n",        
                        buttons=[                                
                           [Button.inline("Info", data="Info")],
                      ])
@Raizen.on(events.callbackquery.CallbackQuery(data="Info"))
async def ommmmk(event):
    await event.edit("**Owner** -Nishith\n**OwnerID** - `1981129808`\n**Message Forwards** - `True`\n**Nishith** [v0.6.7](github.com/xD-Hiro/Raizen), **powered by @KristinaSupportChat**",
                    buttons=[
                        [Button.inline("Close", data="Close")],                        
                    ])

@Raizen.on(events.callbackquery.CallbackQuery(data="Close"))
async def ommmmk(event):
    await event.delete()
