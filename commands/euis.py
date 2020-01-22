import command_system
#пасхалки потом когда-ниубдь доделаю.

def eus():
  message = 'Берешь зачетку, уверенно подходишь и говоришь: "Поставьте троечку, я от бота Маллокника" B-)'
  return message, ''

eus_command = command_system.Command()
eus_command.description = 'расскажу как успешно закрыть сессию'
eus_command.keys = ['автомат']
eus_command.process = eus

def kon():
    message = 'Возможно вы имели в виду Плехановку?\nНет?\n\nНа пересдачу.'
    return message, ''
kon_command = command_system.Command()
kon_command.description = 'зачет в стиле коня'
kon_command.keys = ['конь']
kon_command.process = kon
