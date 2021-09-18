import os
import feedparser
from .sql import db
from time import sleep, time
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from apscheduler.schedulers.background import BackgroundScheduler
from notemusic import NoteMusic

import random


# CONFIGURAÇÃO IMPORTANTE 
feed_url_ = "https://betteranime.net/lancamentos-rss | https://br.ign.com/feed.xml".split("|")



log_channel = "-1001165341477"# "-1001446397223" # Canal do Bot+ BotAdmin
check_interval = 10
max_instances = 200 

# if db.get_link(feed_url) == None:
  # db.update_link(feed_url, "*")

# AQUI É ONDE É EXIBIDO O POST APÓS CHECK DE URL/FEED
def verificar_postar():
    feed_url = random.choice(feed_url_)
    FEED = feedparser.parse(feed_url)
    print("HEEEEEETEEEE: " + feed_url)
    entry = FEED.entries[0]
    if feed_url == "https://betteranime.net/lancamentos-rss":
        if entry.id != db.get_link(feed_url).link:
# CONFIGURE ESTA PARTE COMO DESEJAR
# Tag para Resumo:{entry.summary}
            message = f"""
🎮 [\u200c](https:{entry.links[1].href}){entry.title}
▫️ | {entry.link}

◾️ | <code>Powered By:</code> @NoteZV
"""
            try:
                NoteMusic.send_message(log_channel, message)
                db.update_link(feed_url, entry.id)
            except FloodWait as e:
                print(f"FloodWait: {e.x} segundos")
                sleep(e.x)
            except Exception as e:
                print(e)
        else:
            print(f"FEED Verificado: {entry.id}")
    else:
        if entry.id != db.get_link(feed_url).link:
            message = f"**{entry.title}**\n"
            try:
                NoteMusic.send_message(log_channel, message)
                db.update_link(feed_url, entry.id)
            except FloodWait as e:
                print(f"FloodWait: {e.x} segundos")
                sleep(e.x)
            except Exception as e:
                print(e)
        else:
            print(f"FEEEEED Verificado: {entry.id}")

scheduler = BackgroundScheduler()
scheduler.add_job(verificar_postar, "interval", seconds=check_interval, max_instances=max_instances)
scheduler.start()
