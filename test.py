import telebot
import sqlite3

bot = telebot.TeleBot('7441214068:AAEth_XRJN1I0UaqScKue73KeuBYtwjJ0-c')

name = 'None'



@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('IT_Академия.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')

    conn.commit()
    cur.close()
    conn.close()


    bot.send_message(message.chat.id, '      Привет сейчас тебя зарегистрируем! Введите ваше имя  потом подпишись на канал  ' )
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name 
    name = message.text.strip()
    bot.send_message(message.chat.id, ' Введите пароль   ' )
    bot.register_next_step_handler(message, user_pass)




def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('IT_Академия.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, pass ) VALUES ('%s', '%s')" % (name, password))

    conn.commit()
    cur.close()
    conn.close()



    # markup = telebot.types.InlineKeyboardMarkup()
    # markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users' ))
    bot.send_message(message.chat.id, ' Пользователь зарегистрирован !   ',  )
   



bot.polling(none_stop=True)