# Импортируем необходимые классы.
import logging
import json
import requests
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


def toponym(text):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={text}&format=json"

    # Выполняем запрос.
    response = requests.get(geocoder_request)
    if response:
        # Преобразуем ответ в json-объект
        json_response = response.json()

        # Получаем первый топоним из ответа геокодера.
        # Согласно описанию ответа, он находится по следующему пути:
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        # Полный адрес топонима:
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
        # Координаты центра топонима:
        toponym_coodrinates = toponym["Point"]["pos"]
        # Печатаем извлечённые из ответа поля:
        return toponym_coodrinates


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


async def get_response(url, params):
    logger.info(f"getting {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            return await resp.json()


async def yandex_weather(update, context):
    location = ' '.join(context.args)
    coords = toponym(location).split()
    conditions = {'clear': 'ясно', 'partly-cloudy': 'малооблачно', 'cloudy': 'облачно с прояснениями',
                  'overcast': 'пасмурно', 'drizzle': 'морось', 'light-rain': 'небольшой дождь',
                  'rain': 'дождь', 'moderate-rain': 'умеренно сильный', 'heavy-rain': 'сильный дождь',
                  'continuous-heavy-rain': 'длительный сильный дождь', 'showers': 'ливень',
                  'wet-snow': 'дождь со снегом', 'light-snow': 'небольшой снег', 'snow': 'снег',
                  'snow-showers': 'снегопад', 'hail': 'град', 'thunderstorm': 'гроза',
                  'thunderstorm-with-rain': 'дождь с грозой', 'thunderstorm-with-hail': 'гроза с градом'
                  }
    wind_dir = {'nw': 'северо-западное', 'n': 'северное', 'ne': 'северо-восточное', 'e': 'восточное',
                'se': 'юго-восточное', 's': 'южное', 'sw': 'юго-западное', 'w': 'западное', 'с': 'штиль'}
    params = {"lat": coords[1],
              "lon": coords[0],
              "lang": "ru_RU",
              "hours": "false",
              "extra": "true"}
    headers = {"X-Yandex-API-Key": "00e5b9a8-2f6b-4583-9953-3e5c2ff2d16c"}
    res = requests.get('https://api.weather.yandex.ru/v2/forecast', params=params, headers=headers).json()

    await update.message.reply_text(f"Вы выполнили запрос погоды по адресу: {location} \nТемпература: {res['fact']['temp']}°C \nОщущается, как: {res['fact']['feels_like']}°C\nОсадки: {conditions[res['fact']['condition']]}")


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
    application.add_handler(CommandHandler('weather', yandex_weather))

    application.run_polling()


if __name__ == '__main__':
    main()
