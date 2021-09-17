from pyrogram import Client, filters
from pyrogram.types import Message

from notemusic import Functions
from client import NoteMusic

from typing import Union
from functools import partial, wraps



import os

import feedparser

from plugins.sql import db
from time import sleep, time
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from apscheduler.schedulers.background import BackgroundScheduler


cmd = partial(filters.command, prefixes=list("/"))

CREATOR_ID = 1157759484

def check_owner(user: Union[int, str]) -> bool:
    if user == CREATOR_ID:
        return True
    return False




@NoteMusic.on_message(filters.chat(-1001165341477))
async def kek(_, message: Message):
    check_interval = 200  
    max_instances = 200
    feed_url = "http://betteranime.net/lancamentos-rss"
    if db.get_link(feed_url) == None:
        db.update_link(feed_url, "*")
    def verificar_postar():
        FEED = feedparser.parse(feed_url)
        entry = FEED.entries[0]
        if entry.id != db.get_link(feed_url).link:
    # CONFIGURE ESTA PARTE COMO DESEJAR
    # Tag para Resumo:{entry.summary}
            message = f"""
🎮 Adicione um título [aqui:]({entry.link}) 
▫️ | <code>v1.5.Nerd ✅</code> 
◾️ | <code>Powered By:</code> @applled
"""
            try:
                NoteMusic.send_message(-1001165341477, message)
                db.update_link(feed_url, entry.id)
            except FloodWait as e:
                print(f"FloodWait: {e.x} segundos")
                sleep(e.x)
            except Exception as e:
                print(e)
            else:
                print(f"FEED Verificado: {entry.id}")
    scheduler = BackgroundScheduler()
    scheduler.add_job(verificar_postar, "interval", seconds=check_interval, max_instances=max_instances)
    scheduler.start()
            
            
        
        # rss = feedparser.parse("https://betteranime.net/lancamentos-rss")
        # await NoteMusic.send_message(-1001165341477, f"[\u200c](https:{rss.entries[0].links[1].href}){rss.entries[0].title}\n\n{rss.entries[0].link}")
            




@NoteMusic.on_message(cmd("sm"))
async def sm(_, message: Message):
    if check_owner(message.from_user.id) == True:
        msg = Functions.input_str(message)
        id_ = msg.split(maxsplit=1)[0]
        msg_ = msg.split(maxsplit=1)[1]
        await NoteMusic.send_message(id_, msg_)
        

@NoteMusic.on_message(cmd("fp"))
async def fp_answer(_, message: Message):
    if check_owner(message.from_user.id) == True:
        await NoteMusic.send_message(-1001446397223, Functions.input_str(message))
    
    
@NoteMusic.on_message(filters.private)
async def pm_answer(_, message: Message):
    exceptions_ = [1157759484, 1986585144]
    if not message.from_user.id in exceptions_:
        await message.forward(1157759484)
    if message.reply_to_message:
        fw_id = message.reply_to_message.forward_from.id
        if message.text:
            await NoteMusic.send_message(fw_id, message.text)
        elif message.sticker:
            await NoteMusic.send_sticker(fw_id, message.sticker.file_id)
        elif message.photo:
            if not message.caption:
                await NoteMusic.send_photo(fw_id, message.photo.file_id)
                return
            await NoteMusic.send_photo(fw_id, message.photo.file_id, message.caption)
        elif message.animation:
            if not message.caption:
                await NoteMusic.send_animation(fw_id, message.animation.file_id)
                return
            await NoteMusic.send_animation(fw_id, message.animation.file_id, message.caption)
        elif message.video:
            if not message.caption:
                await NoteMusic.send_video(fw_id, message.video.file_id)
                return
            await NoteMusic.send_video(fw_id, message.video.file_id, message.caption)
        elif message.audio:
            if not message.caption:
                await NoteMusic.send_audio(fw_id, message.audio.file_id)
                return
            await NoteMusic.send_audio(fw_id, message.audio.file_id, message.caption)
        elif message.document:
            if not message.caption:
                await NoteMusic.send_document(fw_id, message.document.file_id)
                return
            await NoteMusic.send_document(fw_id, message.document.file_id, caption=message.caption)
            
                