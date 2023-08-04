from telebot import types
from config import ADMIN_USERNAME

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
fill_form = types.KeyboardButton("Заполнить анкету")
information = types.KeyboardButton("Информация")
start_keyboard.add(fill_form, information)



info_kb = types.InlineKeyboardMarkup(row_width=1)
contact_btn = types.InlineKeyboardButton("Контакты", callback_data="contacts_info")
report_btn = types.InlineKeyboardButton("Обратная связь", url=f"https://t.me/{ADMIN_USERNAME}")
info_kb.add(contact_btn, report_btn)
geoposition = types.InlineKeyboardButton("Геопозиция", request_location=True)
info_kb.add(geoposition)