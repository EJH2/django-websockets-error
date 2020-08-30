import time
from random import random

from celery import shared_task
from celery_progress.websockets.backend import WebSocketProgressRecorder


@shared_task(bind=True)
def ws_task(self, *args, number):
    progress_recorder = WebSocketProgressRecorder(self)
    for i in range(number):
        time.sleep(.1)
        progress_recorder.set_progress(i+1, number)
    return int(random()*10)


@shared_task(bind=True)
def ws_error_task(self, *args, number):
    progress_recorder = WebSocketProgressRecorder(self)
    for i in range(number):
        time.sleep(.01)
        progress_recorder.set_progress(i+1, number)
    return random()*1000

