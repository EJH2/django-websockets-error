from django.shortcuts import render
from celery import chain

from .tasks import ws_task, ws_error_task


def index(request):
    return render(request, 'index.html')


def ws_view(request):
    result = chain(ws_task.s(number=10) | ws_task.s(number=10) | ws_task.s(number=10) | ws_task.s(number=10) | ws_task.s(number=10))()
    id_chain = []
    while result.parent:
        id_chain.insert(0, result.id)
        result = result.parent
    id_chain.insert(0, result.id)
    return render(request, 'ws.html', context={'task_ids': id_chain})


def ws_error_view(request):
    result = chain(ws_error_task.s(number=10) | ws_error_task.s(number=10) | ws_error_task.s(number=10) | ws_error_task.s(number=10) | ws_error_task.s(number=10))()
    id_chain = []
    while result.parent:
        id_chain.insert(0, result.id)
        result = result.parent
    id_chain.insert(0, result.id)
    return render(request, 'ws.html', context={'task_ids': id_chain})
