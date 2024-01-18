import os
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(os.environ.get('API_ID'))
    API_HASH = os.environ.get('API_HASH')
    BOT_TOKEN = os.environ.get('BOT_TOKEN')

    HEROKU_API_KEY = os.environ.get('HEROKU_API_KEY')

    OWNER_ID = "hamza_farahat"



