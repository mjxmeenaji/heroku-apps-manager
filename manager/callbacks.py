# Written by Hamza Farahat <farahat.hamza1@gmail.com>, 12/25/2024
# Contact me for more information:
# Contact Us: https://terabyte-26.com/quick-links/
# Telegram: @hamza_farahat or https://t.me/hamza_farahat
# WhatsApp: +212772177012

import traceback

from vars import Var
from manager import AppsManager
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, List
from helpers import (get_get_all_apps_from_heroku,
                     get_all_apps_with_status,
                     get_apps_buttons,
                     change_dynos_and_get_current_buttons
                     )


@AppsManager.on_message(filters.command(['start']) & filters.private)
async def start(c, m):
    chat_id: int = m.chat.id

    if chat_id == Var.ADMIN_ID:

        try:
            first_name = m.from_user.first_name
        except:
            first_name = 'Dear'

        await c.send_chat_action(chat_id, enums.ChatAction.TYPING)

        apps = await get_get_all_apps_from_heroku()

        apps_with_status = await get_all_apps_with_status(apps)

        buttons = await get_apps_buttons(apps_with_status)

        await m.reply_text(
            Var.MESSAGES['welcome'].format(
                chat_id,
                first_name
            ), reply_markup=InlineKeyboardMarkup(buttons)
        )


@AppsManager.on_callback_query()
async def callback(c, q):

    chat_id: int = q.from_user.id

    if chat_id == Var.ADMIN_ID:

        try:
            message_id: int = q.message.id

            data: str = q.data
            app_name: str = data.split('|')[0]
            current_status: int = int(data.split('|')[1])

            buttons: List[List[InlineKeyboardButton]] = q.message.reply_markup.inline_keyboard

            current_buttons: list[list[InlineKeyboardButton]] = await change_dynos_and_get_current_buttons(app_name, current_status, buttons)
            await c.edit_message_reply_markup(chat_id, message_id, InlineKeyboardMarkup(current_buttons))

        except:
            err: str = "⚠️ Error: " + str(traceback.format_exc())
            await AppsManager.send_message(Var.ADMIN_ID, err)

