from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import subprocess
import credentials

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN: str = credentials.buddy_token

# Создаем объекты бота и диспетчера
bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer("""Привет!\nМеня зовут English Buddy)\nЯ буду периодически присылать различные шутки в виде вопросов.
Кто сможет дать правильный ответ - получит 300 рублей скидкой на следующий урок от @s_egepro100.
Вопрос и ответ будут не всегда связаны между собой - чаще не связанны, а может связанны, я еще не определился)))   
ДА НАЧНЕТСЯ ИГРА?)
    """)

# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer("""Мой создатель @KJly6HuKA. По всем вопросам моего функционирования обращаться к нему.""")




# Этот хэндлер будет срабатывать на команду "/answer"
# Для получения ответа из игры "/start_game"
@dp.message(Command(commands=["answer"]))
async def process_help_command(message: Message):
    global answer
    await message.answer(f"""{answer}""")


answer = '' # переменная для хранения и последующего сравнения ответов в группе

@dp.message(Command(commands=["start_game"]))
async def process_start_game_command(message: Message):
    global answer
    try:
        result = subprocess.run(["python", "test.py"], capture_output=True, text=True)
        answer = result.stdout.strip()  # Получаем стандартный вывод и убираем лишние пробелы
        await message.answer("Игра началась! Напишите ваш ответ.")
    except Exception as e:
        await message.answer(f"Произошла ошибка при запуске игры: {str(e)}")

# Этот хэндлер будет срабатывать на все текстовые сообщения
@dp.message(lambda message: message.text and isinstance(message.text, str))
async def echo(message: Message):
    global answer
    if message.text.strip() in answer:  # Сравниваем ответ пользователя с правильным ответом
        await message.answer(text=f"""Мои поздравления, {message.from_user.full_name}!
Вы дали правильный ответ!""")  # Используем await для асинхронного ответа







if __name__ == '__main__':
    dp.run_polling(bot)
