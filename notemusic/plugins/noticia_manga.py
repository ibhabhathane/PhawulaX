import os
import feedparser
from .sql import db
from time import sleep, time
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from apscheduler.schedulers.background import BackgroundScheduler
from notemusic import NoteMusic

import random

feed_urls = list(set(i for i in os.environ.get("FEED_URLS").split(" | ")))
log_channel = "-1001446397223"# "-1001165341477"  # Canal do Bot+ BotAdmin
check_interval = 100
max_instances = 200 

# if db.get_link(feed_url) == None:
  # db.update_link(feed_url, "*")

def verificar_postar():
    # for feed_url in feed_urls:
        # feed_url = feed_url
    feed_url = random.choice(feed_urls)
    FEED = feedparser.parse(feed_url)
    entry = FEED.entries[0]
    if entry.id != db.get_link(feed_url).link:
        message = f"""
🎮 {entry.title}
▫️ | {entry.link}

◾️ | <code>Mantido por:</code> @NoteZV
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

scheduler = BackgroundScheduler()
scheduler.add_job(verificar_postar, "interval", seconds=check_interval, max_instances=max_instances)
scheduler.start()
