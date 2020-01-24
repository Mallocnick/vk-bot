import command_system

def info():
    message = ''
    for c in command_system.command_list:
        message += c.keys[0] + ' - ' + c.description + '\n'
    return message, ''


info_command = command_system.Command()

info_command.keys = ['помощь', 'команды', 'help', 'хелп', 'info', 'не понял', 'как']
info_command.description = 'покажу список команд'
info_command.process = info
#info