from art import tprint
from colorama import Fore
from config import bot
from handlers import main_handlers
from db.tables import create_tables


tprint("Welcome")

create_tables()

main_handlers.registar_main_message_handlers()


print(Fore.GREEN + "[BOT] bot started", Fore.RESET + "")

bot.infinity_polling()

print(Fore.RED + "[BOT] bot is break", Fore.RESET + "")
