import asyncio
import logging
import os
import random
import re
import string
from datetime import datetime
from typing import Pattern

import requests
from telethon import Button, TelegramClient, events
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.sessions import StringSession
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_display_name


from config import API_HASH, API_ID, SESSION


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)


bot = TelegramClient(
    StringSession(SESSION), api_id=API_ID, api_hash=API_HASH, lang_code="tr"
)

# ----------------------ping
@bot.on(events.NewMessage(pattern=".ping"))
async def ping(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("Pong!\n`{}`".format(ms))
    
@bot.on(events.NewMessage(pattern=".reklam"))
async def reklam(event):
    await event.edit(
        "**Light Dark Hub** š\n24 saat 300TL (1 Yenileme 5 Flood)\n\nš**Turkzzers_KKTC**š\n24 saat 200 TL (1 yenileme 2 Flood)\n\nš**Turklinkhubs**š\n24 saat 100TL (1 Yenileme 5 Flood)\n\n**Kanal Linkleri**š\n**Light Dark Hub** š\nš https://t.me/+GT6tnlStZw45YWI0\n\nš**Turkzzers_KKTC**š\nš https://t.me/+UbtuJcTibw2Jksct\nš https://t.me/+_NAIbmiWGoI0ZDE0\nš https://t.me/+XIa6Dtdc6DI4ZjI8\n\nš**Turklinkhubs**š\nš https://t.me/+QRZt5CMd9ho5NGE0"
    )    
