from send_message import run_send_message
from get_joke import get_joke
import time

def joke():
    # Получаем шутку с помощью get_joke() из get_joke.py
    # и отправляем run_send_message() из send_message.py
    run_send_message(get_joke()[0])
    time.sleep(10)
    run_send_message(f'Правильный ответ:\n{get_joke()[1]}')






# joke()