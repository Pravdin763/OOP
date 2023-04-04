#31. Инструкция raise и пользовательские исключения |

class ExceptionPrintSendDate(Exception):
    """Класс исключений для отправки данных принтеру"""
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'Ошибка {self.message}'

class Printdate:
    def print(self, data):
        self.send_data(data)
        print('печать: ', str(data))

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendDate('Принтер не отвечает')

    def send_to_print(self, data):
        return False


p = Printdate()
#try:
p.print('123')
#except ExceptionPrintSendDate:
    #print('Принтер не отвечает')