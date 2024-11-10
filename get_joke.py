import aiohttp
import asyncio

async def fetch_joke():
    # Получение шутки
    url = "https://official-joke-api.appspot.com/random_joke"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                joke = await response.json()
                question_and_answer = [joke['setup'], joke['punchline']]
                return question_and_answer
            else:
                return ["Не удалось получить шутку."]

async def return_joke():
    # Возврат самой шутки в виде list с двумя значениями 0-вопрос 1-ответ
    joke = await fetch_joke()
    return joke

def get_joke():
    # Запуск асинхронной функции и возврат результата
    return asyncio.run(return_joke())



