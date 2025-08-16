import logging
from pyrogram import Client
from Config import Config
import json
import os
import sys
import telepot
import time
from telepot.loop import MessageLoop
import ntplib  # <- adăugat pentru sincronizare timp

logging.basicConfig(level=logging.INFO)

# --- Sincronizare timp ---
try:
    c = ntplib.NTPClient()
    response = c.request('pool.ntp.org')
    t = response.tx_time
    offset = t - time.time()
    print(f"[INFO] Offset de timp: {offset:.2f} secunde")
    if offset > 0:
        time.sleep(offset)  # Ajustează timpul local pentru Pyrogram
except Exception as e:
    print("[WARN] Nu s-a putut sincroniza timpul:", e)

# --- Pluginuri ---
plugins = dict(
    root="plugins",
    include=[
        "forceSubscribe",
        "help"
    ]
)

# --- Client Pyrogram ---
app = Client(
     'ForceSubscribe',
     bot_token=Config.BOT_TOKEN,
     api_id=Config.APP_ID,
     api_hash=Config.API_HASH,
     plugins=plugins
)

# --- Rulează botul ---
app.run()
