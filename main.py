from config import bot
from handlers import main_handlers
main_handlers.registar_main_message_handlers()

bot.infinity_polling()

