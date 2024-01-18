import time
import traceback

from pyrogram import Client, filters, enums, idle
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardMarkup

from helpers import get_get_all_apps, get_all_apps_with_status, get_apps_buttons, change_dynos_and_get_current_buttons
from vars import Var

AppsManager = Client("heroku_apps_manager", api_id=Var.API_ID, api_hash=Var.API_HASH, bot_token=Var.BOT_TOKEN)


@AppsManager.on_message(filters.command(['start']) & filters.private)
async def start(c, m):
    chat_id = m.chat.id
    first_name = m.from_user.first_name

    await c.send_chat_action(chat_id, enums.ChatAction.TYPING)

    apps = await get_get_all_apps()

    apps_with_status = await get_all_apps_with_status(apps)

    buttons = await get_apps_buttons(apps_with_status)

    await m.reply_text(Var.MESSAGES['welcome'].format(chat_id, first_name), reply_markup=InlineKeyboardMarkup(buttons))


@AppsManager.on_callback_query()
async def callback(c, q):
    try:
        chat_id = q.from_user.id
        message_id = q.message.id

        username = q.message.chat.username

        if username in Var.OWNER_ID:
            data = q.data
            app_name = data.split('|')[0]
            current_status = int(data.split('|')[1])

            buttons = q.message.reply_markup.inline_keyboard

            current_buttons = await change_dynos_and_get_current_buttons(app_name, current_status, buttons)
            await c.edit_message_reply_markup(chat_id, message_id, InlineKeyboardMarkup(current_buttons))


    except:
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





