from config import bot, ADMIN_USERNAME, db, cursor
from keyboards import main 


def start(message):
    cursor.execute(f"SELECT * FROM users WHERE user_id = {message.from_user.id}")
    user_data = cursor.fetchone()
    if user_data is None:
        
        cursor.execute(f'''INSERT INTO users(user_id, first_name, last_name, username, chat_id, first_login, last_login)
                        VALUES(
                            {message.from_user.id},
                            "{message.from_user.first_name}",
                            "{message.from_user.last_name}",
                            "{message.from_user.username}",
                            {message.chat.id},
                            {message.date},
                            {message.date});''')

        db.commit()
    else:

       
        cursor.execute(f'''UPDATE users SET last_login = {message.date} WHERE user_id ={message.from_user.id}''') 
        db.commit() 
    print(user_data)
    



    with open("images/main/vitamin.png", "rb") as image:
        bot.send_photo(message.chat.id, image, caption="Добрый день!\nПриветствуем тебя в нашем телеграмм боте",
                       reply_markup=main.start_keyboard)


def send_information(message):
    bot.send_message(message.chat.id, text="Выберите нужную категорию", reply_markup=main.info_kb)
    

def send_contacts(callback):
    bot.send_message(callback.message.chat.id, text=f"*Admin's contact:\n@{ADMIN_USERNAME}*",
                      parse_mode="markdown")
    
def send_test_message(message):
    bot.send_message(message.chat.id, text="Это тестовое сообщение", reply_markup=main.test_kb)

    

def send_location_info(message):
    bot.send_message(message.chat.id, text=f'''Ваша широта {message.location.latitude} 
Ваша долгота{message.location.longitude}''')


def send_phone(message):
    bot.send_message(message.chat.id, text="телефон", reply_markup=main.button_phone)


def send_number(message):
    if message.contact is not None:
        print(message.contact.phone_number)



def start_form(message):

    send = bot.send_message(message.chat.id, text="Как Вас зовут?")
    bot.register_next_step_handler(send, form_send_lastname)


def form_send_lastname(message):
    cursor.execute(f''' INSERT INTO form(user_id, first_name) 
                   VALUES({message.from_user.id}, "{message.text.lower()}")''')


    db.commit()

    send = bot.send_message(message.chat.id, text="Ваша фамилия?")
    bot.register_next_step_handler(send,form_send_phone)

def form_send_phone(message):
    cursor.execute(f''' UPDATE form SET last_name = "{message.text.lower}" WHERE user_id = {message.from_user.id}''')
    db.commit()


    send = bot.send_message(message.chat.id, text="Ваш номер телефона?", reply_markup=main.button_phone)
    bot.register_next_step_handler(send, form_send_email)

def form_send_email(message):
    cursor.execute(f''' UPDATE form SET phone_number = "{message.contact.phone_number}" WHERE user_id = {message.from_user.id}''')
    db.commit()

    send = bot.send_message(message.chat.id, text="Ваша электронная почта?")
    bot.register_next_step_handler(send, form_send_city)

def form_send_city(message):
    cursor.execute(f''' UPDATE form SET email = "{message.text.lower}" WHERE user_id = {message.from_user.id} ''')
    db.commit()

    send = bot.send_message(message.chat.id, text="Ваш город?")
    bot.register_next_step_handler(send, form_location_latitude_longitude)

def form_location_latitude_longitude(message):
    cursor.execute(f''' UPDATE form SET city = "{message.text.lower}" WHERE user_id = {message.from_user.id} ''')
    db.commit()

    send = bot.send_message(message.chat.id, text="Ваша локация?", reply_markup=main.location_kb)
    bot.register_next_step_handler(send, form_send_all_info) 

def form_send_all_info(message):
    cursor.execute(f''' UPDATE form SET location_latitude = {message.location.latitude}, location_longitude = {message.location.longitude}
                    WHERE user_id = {message.from_user.id}''')
    db.commit()

    cursor.execute(f"SELECT * FROM form WHERE user_id = {message.from_user.id}")    
    user_form_data = cursor.fetchone()
    bot.send_message(message.chat.id, text=f'''Ваша информация
Ваш id: {user_form_data[0]}
Ваше имя:{user_form_data[1]}  
Ваша фамилия: {user_form_data[2]}
Ваш номер телефона: {user_form_data[3]}
Ваша электронная почта: {user_form_data[4]}
Ваш город: {user_form_data[5]}
                     ''')
    bot.send_location(message.chat.id, latitude=user_form_data[6], longitude=user_form_data[7])


def registar_main_message_handlers():
    bot.register_message_handler(start, commands=["start"])
    bot.register_message_handler(send_information, func=lambda message: message.text=="Информация")
    bot.register_callback_query_handler(send_contacts, func=lambda callback: callback.data=="contacts_info")
    bot.register_message_handler(send_test_message, commands=["test"])
    bot.register_message_handler(send_location_info, content_types=["location"])
    bot.register_message_handler(send_phone, commands=["phone"])
    bot.register_message_handler(send_number, content_types=["contact"])
    bot.register_message_handler(start_form, commands=["lastname"])
    bot.register_message_handler(start_form, commands=["form"])
    
    
    
