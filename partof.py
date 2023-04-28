import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, ConversationHandler
import datetime
import random

BOT_TOKEN = '5999252740:AAENPLeEI4GGgo_0H4QTWZiuCzqn2KWVtQU'
count = 0
reply_keyboard = [['/menu_random', '/rules', '/top_secret']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


async def start(update, context):
    await update.message.reply_text(
        "Привет. Здесь ты можешь неплохо приподнятся!\n"
        "Вы можете проверить совю дачу, нажав /play.\n"
        "Можно послать команду /rules , если хотите понять правила.\n"
        "Также можно просто закончить диалог с помощью команды /stop\n"
        "Чтобы вернться в меню введите /menu_random\n"
        "Если вам что-то непонятно, кликайте сюда /help",
         reply_markup=markup)

    return 1


async def help(update, context):
    await update.message.reply_text(
        "чел боже")

async def top_secret(update, context):
    await update.message.reply_text("Отблагодарите авторов деревянным рубликом:\n"
                                    "5536914016758595")


async def rules(update, context):
    await update.message.reply_text(
        "Итак, данный раздел нашего бота просто конченный!")


async def menu_random(update, context):
    await update.message.reply_text(
        "Вы можете проверить свою удачу, нажав /play.\n"
        "Можно послать команду /rules , если хотите понять правила.\n"
        "Также можно просто закончить диалог с помощью команды /stop")

    return 1


async def first_level(update, context):
    global count
    user_input = update.message.text
    if count != context.user_data['number']:
        count += 1
    if count <= 4:
        if user_input.isdigit():
            answer_number = int(user_input)
            if answer_number > context.user_data['number']:
                await update.message.reply_text('Ваше число слишком большое. Попробуйте еще раз.')
            elif answer_number < context.user_data['number']:
                await update.message.reply_text('Ваше число слишком маленькое. Попробуйте еще раз.')
            else:
                await update.message.reply_text('Вы угадали число! Поздравляем :) Напишите /play_l2, чтобы сыграть на новом уровне.')
                count = 0
        else:
            await update.message.reply_text('Вообще не понимаю, что вы пишете')
    else:
        await update.message.reply_text('Попробуйте еще раз./play')
        count = 0


async def second_level(update, context):
    global count
    user_input = update.message.text
    if count != context.user_data['number']:
        count += 1
    if count <= 4:
        if user_input.isdigit():
            answer_number = int(user_input)
            if answer_number > context.user_data['number']:
                await update.message.reply_text('Ваше число слишком большое. Попробуйте еще раз.')
            elif answer_number < context.user_data['number']:
                await update.message.reply_text('Ваше число слишком маленькое. Попробуйте еще раз.')
            else:
                await update.message.reply_text(
                    'Вы угадали число! Поздравляем :) Напишите /play_l3, чтобы сыграть на новом уровне.')
                count = 0
        else:
            await update.message.reply_text('Вообще не понимаю, что вы пишете')
    else:
        await update.message.reply_text('Попробуйте еще раз. /play')
        count = 0


async def stop(update, context):
    await update.message.reply_text("Всего доброго!")
    return ConversationHandler.END



async def play(update, context):
    number = random.randint(1, 50)
    context.user_data['number'] = number
    await update.message.reply_text(
        f"я загадал число от 1 до 50, отгадай")

    return 1

async def play_l2(update, context):
    number = random.randint(1, 100)
    context.user_data['number'] = number
    await update.message.reply_text(
        f"я загадал число от 1 до 100, отгадай")
    return 2

async def play_l3(update, context):
    number = random.randint(1, 250)
    context.user_data['number'] = number
    await update.message.reply_text(
        f"я загадал число от 1 до 250, отгадай")

    return 2


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],


        states={

            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, first_level)],

            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, second_level)]
        },


        fallbacks=[CommandHandler('stop', stop), CommandHandler('menu_random', menu_random),
                   CommandHandler('play', play), CommandHandler('play_l2', play_l2), CommandHandler('play_l3', play_l3),
                   CommandHandler('rules', rules), CommandHandler('help', help), CommandHandler('top_secret', top_secret)]
    )

    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
