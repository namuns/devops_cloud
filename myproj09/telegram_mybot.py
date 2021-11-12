import os
import sys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import tasks

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
if TELEGRAM_TOKEN is None:
    print("TELEGRAM_TOKEN 환경변수를 지정해주세요", file=sys.stderr)
    sys.exit(1)  # 종료 상태 값을 1로 지정하고 프로그램 종료하는 변수 0이 아니기 떄문에 오류로 규정하고 넘어감

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    """
    대화방이 처음 열리면, 자동으로 호출되는 함수.
    """
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="안녕. 나는 Devops야. 만나서 반가워."
    )


def echo(update, context):
    received_text: str = update.message.text

    supported_tasks = [
        tasks.get_current_lotto_numbers,
        tasks.ya,
        tasks.naver_search,
        tasks.predict_lotto_numbers,
    ]

    for task in supported_tasks:
        if task.check_available(received_text):
            response_text = task.make_response(received_text)
            break
    else:
        response_text = "지원하지 않는 명령입니다."

    tasks.get_current_lotto_numbers.check_available()
    tasks.get_current_lotto_numbers.numbers.make_response()

    context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)


start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)


echo_handler = MessageHandler(
    Filters.text & (~Filters.command),
    echo,
)
dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()


# bot = telegram.Bot(token)
# # info = bot.getMe()
# # pprint.pprint(info)
# # resp = bot.getUpdates()
# # pprint.pprint(resp)
#
# chat_id = 42478249
# bot.sendMessage(chat_id=chat_id, text="안녕. 나는 봇이야!!!")
