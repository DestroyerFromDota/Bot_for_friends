import telegram
import asyncio
import credentials

my_token = credentials.my_token
my_chat_id = credentials.my_chat_id

async def send(msg, chat_id, token=my_token):
    """
    Send a message "msg" to a telegram user or group specified by "chat_id"
    msg         [str]: Text of the message to be sent. Max 4096 characters after entities parsing.
    chat_id [int/str]: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
    token       [str]: Bot's unique authentication token.
    """
    bot = telegram.Bot(token=token)
    await bot.sendMessage(chat_id=chat_id, text=msg)


def run_send_message(MessageString):
    # отправка сообщения MessageString в чат
    asyncio.run(send(msg=MessageString, chat_id=my_chat_id, token=my_token))


