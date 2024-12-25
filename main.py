# Written by Hamza Farahat <farahat.hamza1@gmail.com>, 12/25/2024
# Contact me for more information:
# Contact Us: https://terabyte-26.com/quick-links/
# Telegram: @hamza_farahat or https://t.me/hamza_farahat
# WhatsApp: +212772177012

import time

from pyrogram.errors import FloodWait
from manager import AppsManager


if __name__ == "__main__":

    try:
        print("I'm live !!")
        AppsManager.run()

    except FloodWait as e:
        print(f'FloodWait, waiting for {e.value}s ...')
        time.sleep(e.value)

