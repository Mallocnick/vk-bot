
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, json
from settings import *
import messageHandler

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Mallocnick!'
@app.route('/', methods=['POST'])
def processing():
    #Распаковываем json из пришедшего POST-запроса
    data = json.loads(request.data)
    #Вконтакте в своих запросах всегда отправляет поле типа
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object'], token)
        # Сообщение о том, что обработка прошла успешно
        return 'ok'

