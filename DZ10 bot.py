#Прикрутить бота к задачам с предыдущего семинара:
Создать телефонный справочник с возможностью импорта и экспорта 
данных в нескольких форматах.#

import sqlite3
import telebot

bot = telebot.TeleBot("token")

conn = sqlite3.connect('db/telefon_book.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val(User_id: int, surname: str, name: str, phone_number: str, discription: str):
	cursor.execute('INSERT INTO test (User_id, surname, name, phone_number, discription) VALUES (?, ?, ?, ?, ?)', (User_id, surname, name, phone_number, discription))
	conn.commit()


@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Добро пожаловать')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text.lower() == 'привет':
		bot.send_message(message.chat.id, 'Привет! Ваше Фамилия добавлено в базу данных!')
		
		us_id = message.from_User.id
		us_sname = message.from_user.surname
		us_name = message.from_user.name
		us_phone = message.from_user.phone_number
        us_discr = message.from_user.discription
		
        db_table_val(User_id=us_id, surname=us_sname, name=us_name, phone_number=us_phone, discription=us_discr)


bot.polling(none_stop=True)
