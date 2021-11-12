import os
import sys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import tasks


token = "2128680883:AAElqIKrXfpmZ6NPlshVsxfmRn8IPO6mWtM"
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    """
    대화방이 처음 열리면, 자동으로 호출되는 함수.
    """
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="안녕. 나는 Devops야. 만나서 반가워.")



def echo(update, context):
    received_text: str = update.message.text

    supported_tasks = [tasks.get_current_lotto_numbers,
                       tasks.ya,
                       tasks.naver_search,
                       tasks.predict_lotto_numbers
                       ]

    for task in supported_tasks:
        if task.check_available(received_text):
            response_text = task.make_response(received_text)
            break
    else:
        response_text = "지원하지 않는 명령입니다."


    tasks.get_current_lotto_numbers.check_available()
    tasks.get_current_lotto_numbers.numbers.make_response()


    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=response_text)



start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)



echo_handler = MessageHandler(
    Filters.text & (~Filters.command),
    echo,
)
dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()


