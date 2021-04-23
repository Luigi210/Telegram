import telebot
import random

bot = telebot.TeleBot('1159299080:AAF3CKzBFWVgRNHC0I1ztbkhPK1EW2av1AQ')


@bot.message_handler(content_types=['text', 'audio'])
def get_message(message):
    global a, english
    global k, t
    t = '/broAssan'
    k = False
    english = False
    a = ['hi', 'хай', 'hello', 'Привет', 'Саламалейкум']

    for i in range(len(a)):
        if message.text == a[i] and (a[i] == 'hi' or a[i] == 'hello'):
            bot.send_message(message.from_user.id, a[i] + ", need help?")
            k = True
            english = True
            break
        elif message.text == a[i] and a[i] != 'hi' and a[i] != 'hello':
            bot.send_message(message.from_user.id, a[i] + ", нужна помощь?")
            k = True
            english = False
            break
    if message.text == t:
        bot.send_message(message.from_user.id, 'https://t.me/intelligent_1')
    elif message.text == '/needhelp':
        bot.send_message(message.from_user.id, "Напиши что то из этого :")
        for i in range(len(a)):
            bot.send_message(message.from_user.id, a[i])
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    elif message.text == '/red_book':
        bot.send_message(message.from_user.id, "The Red Book is a list of rare and endangered animals, plants and mushrooms in Kazakhstan. There are three editions, the last of which was published in 1999.\n\nEvery year the animal world of Kazakhstan loses its population. The efforts of environmentalists and volunteers, for whom the animals of the Red Book are the main object of concern and anxiety, slow this process, but do not stop it. \n\nThe current edition includes:\n129 species and subspecies of vertebrates.\n18 fish and round fish.\n3 amphibians.\n10 reptiles.\n58 birds.\n40 mammals...\nHowever, many of Kazakhstan’s animals listed in the Red Book can still be saved through popularization of the issue, education.\n\nWe will explain in detail which animals in the Red Book of Kazakhstan are symbols of our country and their protection has become a public task.")
        bot.register_next_step_handler(message, get_reply)
        # if get_message() == 'reptiles':
        #     bot.send_message(message.from_user.id, "POST")
        #     bot.register_next_step_handler(message, get_name)

    elif k == False:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши '/needhelp'.")


name = ""
surname = ""
age = 0


def get_reply(message):
    bot.send_message(message.from_user.id, 'Who exactly?')
    bot.register_next_step_handler(message, who_exactly)


def who_exactly(message):
    if message.text == 'reptiles':
        bot.send_photo(message.from_user.id, 'https://i.natgeofe.com/n/5506954d-6e0f-444c-aa83-a24adbe874e1/reptiles-hero_3x2.jpg')

    elif message.text == 'mammals':
        bot.send_message(message.from_user.id, 'It is raccoon dog')
        bot.send_photo(message.from_user.id, 'https://www.duluthnewstribune.com/incoming/4721378-74eknm-Raccoon-dog-1.jpg/alternates/BASE_LANDSCAPE/Raccoon%20dog%201.jpg')
        bot.send_message(message.from_user.id, 'It is Hare-Tolai')
        bot.send_photo(message.from_user.id,
                   'https://floranimal.ru/upload/iblock/b92/b92eba2158486b4bd25b6a7b85a5f5d6.jpg')


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except :
            bot.send_message(message.from_user.id, 'Цифрами пожалуйста')
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
        question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + " " + surname + '?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
        # код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'Смело го')
    # elif call.data == "no":


bot.polling(none_stop=True, interval=0)
