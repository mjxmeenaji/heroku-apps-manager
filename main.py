import time
import traceback

import heroku3
import concurrent.futures

from pyrogram import Client, filters, enums, idle
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardMarkup

from helpers import get_get_all_apps, get_all_apps_with_status, get_apps_buttons, change_dynos_and_get_current_buttons
from vars import Var

AppsManager = Client("Yplatinum", api_id=Var.API_ID, api_hash=Var.API_HASH, bot_token=Var.BOT_TOKEN)


@AppsManager.on_message(filters.command(['start']) & filters.private)
async def start(c, m):
    chat_id = m.chat.id
    username = m.chat.username
    first_name = m.from_user.first_name

    if username == Var.OWNER_ID:

        await AppsManager.send_chat_action(chat_id, enums.ChatAction.TYPING)

        apps = await get_get_all_apps()

        apps_with_status = await get_all_apps_with_status(apps)

        print(apps_with_status)

        buttons = await get_apps_buttons(apps_with_status)


        """await c.send_photo(chat_id=chat_id, photo=Var.YOUR_PLATINUM_MOVIES_LOGO, caption=text_messages_eng['welcome_1'].format(chat_id, first_name), reply_markup=choice_eng)
    
        suggestions_buttons = [[InlineKeyboardButton(v, callback_data=k)] for k, v in suggestions_eng.items()]
        await asyncio.sleep(5)"""
        await m.reply_text("Hello World !", reply_markup=InlineKeyboardMarkup(buttons))


@AppsManager.on_callback_query()
async def callback(c, q):
    try:
        chat_id = q.from_user.id
        message_id = q.message.id

        username = q.message.chat.username
        if username == Var.OWNER_ID:

            data = q.data
            app_name = data.split('|')[0]
            current_status = int(data.split('|')[1])

            buttons = q.message.reply_markup.inline_keyboard

            current_buttons = await change_dynos_and_get_current_buttons(app_name, current_status, buttons)

            await c.edit_message_reply_markup(chat_id, message_id, InlineKeyboardMarkup(current_buttons))


    except:
        traceback.print_exc()
        err = "⚠️ Error: " + str(traceback.format_exc())
        await AppsManager.send_message(Var.OWNER_ID, err)



try:
    if __name__ == "__main__":
        AppsManager.start()
        print("I'm live !!")
        idle()
        AppsManager.stop()

except FloodWait as e:
    print(f'FloodWait, waiting for {e.value}s ...')
    time.sleep(e.value)





