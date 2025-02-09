# Written by Hamza Farahat <farahat.hamza1@gmail.com>, 12/25/2024
# Contact me for more information:
# Contact Us: https://terabyte-26.com/quick-links/
# Telegram: @hamza_farahat or https://t.me/hamza_farahat
# WhatsApp: +212772177012

import os
from dotenv import load_dotenv

load_dotenv()


class Var(object):

    #----------------<Telegram Stuff>---------------#
    API_ID: int = int(os.environ.get('API_ID'))
    API_HASH: str = os.environ.get('API_HASH')
    BOT_TOKEN: str = os.environ.get('BOT_TOKEN')
    ADMIN_ID: int = int(os.environ.get('ADMIN_ID'))
    #-----------------------------------------------#


    #----------------<Heroku Stuff>-----------------#
    HEROKU_API_KEY: str = os.environ.get('HEROKU_API_KEY')
    #-----------------------------------------------#


    #----------------<Manager Bot Stuff>------------#
    RED_ZONE: list[str] = ['heroku-apps-manager', ]
    MESSAGES: dict[str: str] = {
        'welcome': "<b><u>Welcome <a href='tg://user?id={}'>{}</a></u></b> !"
    }
    #-----------------------------------------------#
