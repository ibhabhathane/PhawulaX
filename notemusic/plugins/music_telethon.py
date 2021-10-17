from telethon import TelegramClient, events
from youtubesearchpython import SearchVideos
from notemusic import Functions
import time
import os
import youtube_dl

api_id = 3716600
api_hash = "0ed423ceea4fbb06c0e627d9db0f4a6b"
bot_token = "2090823500:AAF3R8ERmALkx0seexQEL5JGRmzSrPdBytU"

c = TelegramClient("test", api_id, api_hash).start(bot_token=bot_token)

def input_str(event):
    input_ = event.text
    if ' ' in input_ or '\n' in input_:
        return str(input_.split(maxsplit=1)[1].strip())
    return ''
    
async def down_music(link, file_name):
    _opts = {
        "outtmpl": f"./cache/{file_name}",
           "prefer_ffmpeg": True,
           "format": "bestaudio/best",
           
           "extractaudio": True,
           "audioformat": "mp3",
    }
    with youtube_dl.YoutubeDL(_opts) as ydl:
        info_dict = ydl.download([link])

@c.on(events.NewMessage(pattern="^/song*"))
async def song(event):
    if input_str(event) == "":
        await event.reply("Vou pesquisar o vento, arrombado?")
        return
    result = Functions.search_music(event.text.split(maxsplit=1)[1])
    link = Functions.get_link(result)
    file_name = Functions.get_file_name(result)
    try:
        Functions.down_music(link, file_name)# await down_music(link, file_name)
    except:
        await event.reply("Num deu pra baixar...")
    if os.path.exists(f"./cache/{file_name}"):
        try:
            await c.send_file(event.chat_id, f"./cache/{file_name}", caption="MUSICAAAAAA")
        except:
            await event.reply("Credita que num deu pra enviar?")
        time.sleep(2)
        os.remove(f"./cache/{file_name}")
        
@c.on(events.NewMessage(pattern="^/on$"))
async def on(event):
    await event.reply("I'm alive!")
    