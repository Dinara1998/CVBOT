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


test_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
contact_btn = types.KeyboardButton("Телефон", request_contact=True)
geo_btn = types.KeyboardButton("Геоданные",request_location=True) 
test_kb.add(contact_btn,geo_btn)


button_phone = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
phone_btn = types.KeyboardButton("Номер телефона", request_contact=True)
button_phone.add(phone_btn)

location_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
location_btn = types.KeyboardButton("геолокация", request_location=True)
location_kb.add(location_btn)