from config import bot, ADMIN_USERNAME
from keyboards import main 

def start(message):
    with open("images/main/vitamin.png", "rb") as image:
        bot.send_photo(message.chat.id, image, caption="Добрый день!\nПриветствуем тебя в нашем телеграмм боте",
                       reply_markup=main.start_keyboard)


def send_information(message):
    bot.send_message(message.chat.id, text="Выберите нужную категорию", reply_markup=main.info_kb)
    

def send_contacts(callback):
    bot.send_message(callback.message.chat.id, text=f"*Admin's contact:\n@{ADMIN_USERNAME}*",
                      parse_mode="markdown")
    
def send_location(callback):
    bot.send_message(callback.message.id, "Отправить геоданные", reply_markup=main.start_keyboard)
    













def registar_main_message_handlers():
    bot.register_message_handler(start, commands=["start"])
    bot.register_message_handler(send_information, func=lambda message: message.text=="Информация")
    bot.register_callback_query_handler(send_contacts, func=lambda callback: callback.data=="contacts_info")
    bot.register_callback_query_handler(send_location, func=lambda callback: callback_data=="Геоданные")

    