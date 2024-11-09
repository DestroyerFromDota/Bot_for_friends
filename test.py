from send_message import run_send_message
from get_joke import get_joke
import time


def joke():
    run_send_message(get_joke()[0])
    time.sleep(10)
    run_send_message(f'Правильный ответ:\n{get_joke()[1]}')