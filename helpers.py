import time
import heroku3
import threading
import concurrent.futures

from vars import Var
from typing import List, Any
from heroku3.api import Heroku
from heroku3.models.dyno import Dyno
from concurrent.futures import Future
from pyrogram.types import InlineKeyboardButton
from heroku3.structures import KeyedListResource


status_emojis: list[str] = ["❌", "✅"]


async def get_get_all_apps_from_heroku() -> list[KeyedListResource]:
    """
    function that get all apps in heroku
    :return: list of all apps
    """
    HEROKU_API_KEY: str = Var.HEROKU_API_KEY
    heroku_conn: Heroku = heroku3.from_key(HEROKU_API_KEY)
    apps: KeyedListResource = heroku_conn.apps(order_by="name", sort="asc")

    new_apps: list[KeyedListResource] = [app for app in apps if app.name not in Var.RED_ZONE]

    return new_apps


def get_app_status(app) -> dict[str, int]:
    """
    function that gets app status
    :param app: heroku app
    :return: app and his status
    """
    dynos: list[Dyno] = app.dynos()
    status: int = 1 if len(dynos) > 0 else 0

    return {app.name: status}


async def get_all_apps_with_status(apps: list[Any]) -> dict:
    """
    function that get all the apps with there status (dynos status)
    :param apps: all apps
    :return: results: apps with status
    """
    start: float = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures: list[Future[dict[Any, int]]] = [executor.submit(get_app_status, app) for app in apps]

    results = {}
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        results.update(result)

    elapsed: float = time.time() - start
    print(f'Elapsed Time: {elapsed:.2f}s')

    sorted_results = dict(sorted(results.items()))

    return sorted_results


async def get_apps_buttons(apps) -> List[List[InlineKeyboardButton]]:
    """
    function that takes apps and return it as apps buttons
    :param results: apps
    :return: apps as inline buttons
    """

    buttons: List[List[InlineKeyboardButton]] = []

    for app_name, app_status in apps.items():

        if app_name not in Var.RED_ZONE:

            buttons.append(
                [
                    InlineKeyboardButton(
                        f'{app_name} {status_emojis[app_status]}',
                        callback_data=f'{app_name}|{app_status}'
                    )
                ]
            )

    return buttons


async def change_dynos_and_get_current_buttons(app_name: str, current_status: int, buttons: List[List[InlineKeyboardButton]]) -> List[List[InlineKeyboardButton]]:
    """
    function that control app dynos in heroku, and get the new buttons
    :param app_name: app name that we select
    :param current_status: current status (1 = up, 0 = down)
    :param buttons: new formatted buttons
    :return:
    """
    future_status: int = 1 if current_status == 0 else 0

    button_index_to_change: int = next(
        (
            index
            for index, button in enumerate(buttons)
            if button[0].callback_data.split('|')[0] == app_name),
        None
    )

    if button_index_to_change is not None:
        buttons[button_index_to_change][0].text = f'{app_name} {status_emojis[future_status]}'
        buttons[button_index_to_change][0].callback_data = f'{app_name}|{future_status}'

    thread: threading.Thread = threading.Thread(target=heroku_scale, args=(app_name, future_status))
    thread.start()

    return buttons


def heroku_scale(app_name: str, scale: int):
    """
    function that control dynos in heroku
    :param app_name: app name that we want to control
    :param scale: (up = 1, down = 0)
    :return:
    """
    HEROKU_API_KEY = Var.HEROKU_API_KEY
    PROCESS_TYPES: list[str] = ["worker", "web"]

    for process in PROCESS_TYPES:

        try:
            heroku_conn: Heroku = heroku3.from_key(HEROKU_API_KEY)
            app = heroku_conn.app(app_name)
            app.process_formation()[process].scale(scale)
            break

        except:
            pass

