from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import credentials

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN: str = credentials.my_token

# Создаем объекты бота и диспетчера
bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer("""Привет!\nМеня зовут English Buddy)\nЯ буду периодически присылать различные шутки в виде вопросов.
Кто сможет дать правильный ответ - получит 300 рублей скидкой на следующий урок от @s_egepro100    
    """)

# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer('эта функция пока не готова, разработчик не придумал что сюда запихнуть')

# Этот хэндлер будет срабатывать на все текстовые сообщения
@dp.message(lambda message: message.text and isinstance(message.text, str))
async def echo(message: Message):
    print(message.from_user)
    await message.answer(text=f"{message.text}")  # Используем await для асинхронного ответа
if __name__ == '__main__':
    dp.run_polling(bot)
