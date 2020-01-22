import random
import command_system

def num():
    attachment = random.randint(3, 5)
    message = 'Сегодня ты получишь оценку ' + str(attachment)
    return message, attachment

num_command = command_system.Command()

num_command.keys = ['предсказание' , 'будущее', 'прдск']
num_command.description = 'пришлю твою будущую оценку'
num_command.process = num