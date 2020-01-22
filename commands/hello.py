import command_system


def hello():
   message = 'Привет! Я новый чат-бот Mallocnick &#128521; Всегда готов забить место в первой восьмерке для тебя <3\nНапиши "хелп", чтобы увидеть список команд!'
   return message, ''

hello_command = command_system.Command()

hello_command.keys = ['привет', 'hello', 'дратути', 'здравствуй', 'здравствуйте', 'hi', 'ку', 'добрый вечер', 'здарова', 'приветствую']
hello_command.description = 'поприветствую тебя'
hello_command.process = hello
