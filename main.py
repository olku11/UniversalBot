# Импортируем необходимые классы.
import logging
import json
import aiohttp
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

# Запускаем логгирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)

apikey = "24c8b16e-642c-44d0-a9fa-a895d26316cf"
right_answers = ['9,58 секунд', 'углерод', 'Стэнли Кубрик', 'водород', 'Япония',
                 'Осло', 'Юрий Гагарин', 'Азия', 'хамелеон', 'Испания']
all_answers = []


async def questions(update, context):
    global all_answers, right_answers
    reply_keyboard = [['9,58 секунд', '9,68 секунд'],
                      ['9,78 секунд', '9,88 секунд']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        "Привет. Пройдите небольшой опрос, пожалуйста!\n"
        "Вы можете прервать опрос, послав команду /stop.\n"
        "Какой рекорд установил Усэйн Болт на Олимпийских играх 2008 года в Пекине в беге на 100 метров?",
        reply_markup=markup)

    return 1


# 1
async def first_response(update, context):
    global all_answers, right_answers
    reply_keyboard = [['углерод', 'железо'],
                      ['гелий', 'кислород']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    all_answers.append(update.message.text)
    await update.message.reply_text(
        f"Какой химический элемент имеет наибольшее количество изотопов?", reply_markup=markup)
    return 2


# 2
async def second_response(update, context):
    global all_answers, right_answers
    reply_keyboard = [['Стэнли Кубрик', 'Роб Райнер'],
                      ['Фрэнк Дарабонт', 'Брайан Де Пальма']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    all_answers.append(update.message.text)
    await update.message.reply_text(
        f"Какой из этих режиссеров не снимал фильмы по произведениям Стивена Кинга?", reply_markup=markup)
    return 3


# 3
async def third_response(update, context):
    global all_answers, right_answers
    reply_keyboard = [['кислород', 'азот'],
                      ['углекислый газ', 'водород']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    all_answers.append(update.message.text)
    await update.message.reply_text(
        f"Какой газ не является частью атмосферы Земли?", reply_markup=markup)
    return 4


# 4
async def fourth_response(update, context):
    global all_answers, right_answers
    reply_keyboard = [['Россия', 'Япония'],
                      ['Австралия', 'Швеция']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    all_answers.append(update.message.text)
    await update.message.reply_text(
        f"В какой из этих стран в году находится меньше дней, чем в остальных?", reply_markup=markup)
    return 5


# 5
async def fifth_response(update, context):
    global all_answers, right_answers
    reply_keyboard = [['Берлин', 'Вена'],
                      ['Копенгаген', 'Осло']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    all_answers.append(update.message.text)
    await update.message.reply_text(
        f"Какой из этих городов не является столицей европейской страны?", reply_markup=markup)
    return 6


# 6
async def sixth_response(update, context):
    global all_answers, right_answers
    reply_keyboard = [['Юрий Гагарин', 'Алексей Леонов'],
                      ['Нил Армстронг', 'Базз Олдрин']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    all_answers.append(update.message.text)
    await update.message.reply_text(
        f"Кто был первым космонавтом в истории?", reply_markup=markup)
    return 7


# 7
async def seventh_response(update, context):
    global all_answers, right_answers
    reply_keyboard = [['Африка', 'Европа'],
                      ['Азия', 'Северная Америка']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    all_answers.append(update.message.text)
    await update.message.reply_text(
        f"Какой материк является самым населенным?", reply_markup=markup)
    return 8


# 8
async def eighth_response(update, context):
    global all_answers, right_answers
    reply_keyboard = [['гепард', 'хамелеон'],
                      ['горилла', 'тигр']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    all_answers.append(update.message.text)
    await update.message.reply_text(
        f"Какое животное может менять цвет своей кожи для скрытия от врагов?", reply_markup=markup)
    return 9


# 9
async def ninth_response(update, context):
    global all_answers, right_answers
    reply_keyboard = [['Испания', 'Италия'],
                      ['Франция', 'Германия']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    all_answers.append(update.message.text)
    await update.message.reply_text(
        f"Какая страна является родиной футбольного клуба 'Барселона'?", reply_markup=markup)
    return 10


# 10
async def tenth_response(update, context):
    global all_answers, right_answers
    all_answers.append(update.message.text)
    n = 0
    for i in range(len(all_answers)):
        if all_answers[i] == right_answers[i]:
            n += 1
    await update.message.reply_text(
        f'Вы выполнили тест на {n / len(right_answers) * 100}%', reply_markup=ReplyKeyboardRemove())
    all_answers = []
    return ConversationHandler.END


async def stop(update, context):
    global all_answers, right_answers
    await update.message.reply_text("Всего доброго!", reply_markup=ReplyKeyboardRemove())
    all_answers = []
    return ConversationHandler.END


async def challenge(update, context):
    reply_keyboard = [['1', '2', '3']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        "Добро пожаловть в квест!\n"
        "Вам необходимо пройти небольшое текстое испытание, посредством выбор дверей\n"
        "Только одна из них ведет на свободу, после других вас ждет смерть\n"
        "Вы можете прервать квест, послав команду /stop.\n"
        "Вы просыпаетесь в заброшенной теммнице. Здесь сыровато\n"
        "На полу вы находите ключ и выбираетесь из темницы\n"
        "Перед вами три двери. За первой дврью вы слышите детский плач.\n"
        "За второй дверью слыше звон монет, а за третьей вы слышите лишь пустоту\n"
        "Куда пойдем?",
        reply_markup=markup)

    return 1


async def chal_1(update, context):
    if update.message.text == "1":
        reply_keyboard = [['1', '2', '3']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            "Детский плач оказался мелким ручейком. Напившись вдволь, вы продолжили путь\n"
            "Перед вами снова три двери\n"
            "В щель первой двери вы видите яркий свет. За второй дверь слышатся звуки панк-музыки\n"
            "За третьей вы слышите ветер. Куда пойдем?",
            reply_markup=markup)
        return 2
    elif update.message.text == "2":
        await stop1(update, context, t=1)
    elif update.message.text == "3":
        await stop1(update, context, t=2)
    else:
        reply_keyboard = [['1', '2', '3']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            "Я вас не понял. Какую дверь вы выбрали? Напишите число.",
            reply_markup=markup)
        return 1


async def chal_2(update, context):
    if update.message.text == "1":
        reply_keyboard = [['1', '2', '3']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            "За первой дверью скрывался самый мощныж прожектор Эльбрус 512.172000.1200\n"
            "Найдя нужную кнопку, вы выключаете его. Перед вами снова три двери\n"
            "За первой дверью вы слышите звуки волн. За второй дверью - пение птиц\n"
            "А за третьей - стрельба. Куда пойдем?",
            reply_markup=markup)
        return 3
    elif update.message.text == "2":
        await stop1(update, context, t=3)
    elif update.message.text == "3":
        await stop1(update, context, t=4)
    else:
        reply_keyboard = [['1', '2', '3']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            "Я вас не понял. Какую дверь вы выбрали? Напишите число.",
            reply_markup=markup)
        return 2


async def chal_3(update, context):
    if update.message.text == "3":
        await update.message.reply_text(
            "Вы оказались на премьере нового боевика. Он был на столько скучным, что вы заснули\n"
            "Это был всего лишь сон. Поздравляю, вы справились с квестом\n",
            reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    elif update.message.text == "1":
        await stop1(update, context, t=5)
    elif update.message.text == "2":
        await stop1(update, context, t=6)
    else:
        reply_keyboard = [['1', '2', '3']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            "Я вас не понял. Какую дверь вы выбрали? Напишите число.",
            reply_markup=markup)
        return 3


async def stop1(update, context, t=0):
    if t == 0:
        await update.message.reply_text(
            "Вы смирились с безысходностью, присели у  стены лабиринта и уснули на веки вечные. Увы, вы умерли")
    if t == 1:
        await update.message.reply_text(
            "Звук монет оказался звоном капающей непонятной жикости. Дотронувшись до нее вы испарились. Увы, вы умерли")
    if t == 2:
        await update.message.reply_text(
            "Сделав шаг вы провалились в яму и разбились об пики. Увы, вы умерли")
    if t == 3:
        await update.message.reply_text(
            "В нужный момент вы не крикнули 'Панки хой!', вас задавила толпа. Увы, вы умерли")
    if t == 4:
        await update.message.reply_text(
            "Вы попали в внентиляцию, ветер вас понес прямо на вентилятор, где вас раскромсало на кусочки. Увы, "
            "вы умерли")
    if t == 5:
        await update.message.reply_text(
            "Вы на пляж в самый разгар цунами. Вам не удалось спастись. Увы, вы умерли")
    if t == 6:
        await update.message.reply_text(
            "Вы попали на отвесный уступ скалы. Не найдя другог выхода, вы прыгнули и разбились. Увы, вы умерли")
    await update.message.reply_text("Всего доброго!", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


async def geocoder(update, context):
    geocoder_uri = "http://geocode-maps.yandex.ru/1.x/"
    response = await get_response(geocoder_uri, params={
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "format": "json",
        "geocode": update.message.text
    })

    toponym = response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    ll, spn = get_ll_spn(toponym)
    # Можно воспользоваться готовой функцией,
    # которую предлагалось сделать на уроках, посвящённых HTTP-геокодеру.

    static_api_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&spn={spn}&l=map"
    await context.bot.send_photo(
        update.message.chat_id,  # Идентификатор чата. Куда посылать картинку.
        # Ссылка на static API, по сути, ссылка на картинку.
        # Телеграму можно передать прямо её, не скачивая предварительно карту.
        static_api_request,
        caption="Нашёл:"
    )


async def get_response(url, params):
    logger.info(f"getting {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            return await resp.json()


def main():
    application = Application.builder().token('5999252740:AAENPLeEI4GGgo_0H4QTWZiuCzqn2KWVtQU').build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('questions', questions)],
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, first_response)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, second_response)],
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, third_response)],
            4: [MessageHandler(filters.TEXT & ~filters.COMMAND, fourth_response)],
            5: [MessageHandler(filters.TEXT & ~filters.COMMAND, fifth_response)],
            6: [MessageHandler(filters.TEXT & ~filters.COMMAND, sixth_response)],
            7: [MessageHandler(filters.TEXT & ~filters.COMMAND, seventh_response)],
            8: [MessageHandler(filters.TEXT & ~filters.COMMAND, eighth_response)],
            9: [MessageHandler(filters.TEXT & ~filters.COMMAND, ninth_response)],
            10: [MessageHandler(filters.TEXT & ~filters.COMMAND, tenth_response)]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )
    conv_handler1 = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('challenge', challenge)],

        # Состояние внутри диалога.
        # Вариант с двумя обработчиками, фильтрующими текстовые сообщения.
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, chal_1)],
            # Функция читает ответ на второй вопрос и завершает диалог.
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, chal_2)],
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, chal_3)]

        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop1)]
    )

    application.add_handler(conv_handler)

    application.add_handler(conv_handler1)
    application.add_handler(CommandHandler('questions', questions))

    application.run_polling()


if __name__ == '__main__':
    main()
