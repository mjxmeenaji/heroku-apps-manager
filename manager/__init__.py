# Written by Hamza Farahat <farahat.hamza1@gmail.com>, 12/25/2024
# Contact me for more information:
# Contact Us: https://terabyte-26.com/quick-links/
# Telegram: @hamza_farahat or https://t.me/hamza_farahat
# WhatsApp: +212772177012

from vars import Var
from pyrogram import Client


AppsManager: Client = Client(
    "heroku_apps_manager",
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN
)

import manager.callbacks

