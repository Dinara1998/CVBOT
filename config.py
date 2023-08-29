import sqlite3
import telebot



bot = telebot.TeleBot("6338767781:AAEOMAifeZkYLzEg4yIodRckG2_JkMSfYjQ")

ADMIN_USERNAME = "dinarayad"

db = sqlite3.connect("db.db", check_same_thread=False)
cursor = db.cursor()

