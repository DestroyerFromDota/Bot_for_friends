from send_message import run_send_message
from get_joke import get_joke
import time

def joke():
    # Получаем шутку с помощью get_joke() из get_joke.py. Отравляем вопрос в чат
    # и печатем ответ для перехвата сабпроцессом основым ядром программы
    run_send_message(get_joke()[0])
    print({get_joke()[1]})
joke()