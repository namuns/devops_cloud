import os
import sys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import tasks



#TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
#if TELEGRAM_TOKEN is None:
#    print("TELEGRAM_TOKEN 환경변수를 지정해주세요", file=sys.stderr)
#    sys.exit(1) #종료 상태 값을 1로 지정하고 프로그램 종료하는 변수 0이 아니기 떄문에 오류로 규정하고 넘어감

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
    reply_text = received_text

    if tasks.ya.check_available(received_text):
        response_text = tasks.ya.make_response((received_text))
    elif tasks.naver_search.check_available(received_text):
        response_text = tasks.naver_search.make_response(received_text)
    else:
        response_text = "지원하지 않는 명령입니다."

#    if received_text == "야":
#        reply_text = "왜?"
#    elif received_text.startswith("네이버 검색:"): #체킹
#        query = received_text[7:]
#        post_list = tasks.naver_search(query)
#        #tasks폴더면 _언더바가 있는 py파일을 읽어온다.
#        # Todo: 응답 문자열을 생성해야합니다.
#        reply_text = ""
#        for post in post_list:
#            reply_text += post["title"] + "\n" #응답

#       for post in post_list:
#          reply_text += post + "\n" 이거는 tag.text로만 썼을 떄고 "\n"이거는 띄어쓰기/
#    else:
#        reply_text = "지원하지 않는 명령입니다."

   # tasks.naver_search(query)

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


# bot = telegram.Bot(token)
# # info = bot.getMe()
# # pprint.pprint(info)
# # resp = bot.getUpdates()
# # pprint.pprint(resp)
#
# chat_id = 42478249
# bot.sendMessage(chat_id=chat_id, text="안녕. 나는 봇이야!!!")