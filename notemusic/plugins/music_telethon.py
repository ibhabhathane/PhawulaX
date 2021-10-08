from telethon import TelegramClient, events
from youtubesearchpython import SearchVideos
import time
import os
import json
import youtube_dl

api_id = 3716600
api_hash = "0ed423ceea4fbb06c0e627d9db0f4a6b"
bot_token = "2090823500:AAGq5HhTTFu_mj3lA8yCry3kHjM73f2fEIk"

c = TelegramClient("test", api_id, api_hash).start(bot_token=bot_token)

    	
def search_music(user_input):
    search = SearchVideos(user_input, offset = 1, mode = "json", max_results = 1)
    if not search.result() == None:
        return json.loads(search.result())
        
def get_link(result):
    if not result == None:
        return result['search_result'][0]['link']
        
def get_file_name(result):
        if not result == None:
            title = result["search_result"][0]["title"]
            if not ("[" and "]") in title:
                return title + ".mp3"
            else:
                return title.replace(("]" or "["), "") + ".mp3"
                
def down_music(link, file_name):
    _opts = {
        "outtmpl": f"./cache/{file_name}",
        "prefer_ffmpeg": True,
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            },
        ],
    }
    with youtube_dl.YoutubeDL(_opts) as ydl:
        info_dict = ydl.download([link])

@c.on(events.NewMessage(pattern="^/song*"))
async def song(event):
    if not event.text.split(maxsplit=1)[1]:
        await event.reply("Vou pesquisar o vento, arrombado?")
        return
    result = search_music(event.text.split(maxsplit=1)[1])
    link = get_link(result)
    file_name = get_file_name(result)
    try:
        down_music(link, file_name)
    except:
        await event.reply("Num deu pra baixar...")
    if os.path.exists(f"./cache/{file_name}"):
        try:
            await c.send_file(event.chat_id, f"./cache/{file_name}", voice_note=True, caption="MUSICAAAAAA")
        except:
            await event.reply("Credita que num deu pra enviar?")
        time.sleep(2)
        os.remove(f"./cache/{file_name}")
        
@c.on(events.NewMessage(pattern="/kek"))
async def kek(event):
    await event.reply("KEEEEEK")
    