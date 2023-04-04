# #4. Магический метод __new__. Пример паттерна Singleton
# https://www.youtube.com/watch?v=-xoT6rntpK0&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=5&ab_channel=selfedu


# все классы ссылаются на базовый класс object

# class Point:
#
#     def __new__(cls, *args, **kwargs):              # cls ссылается на сам класс!!!
#
#         print('Вызов  __new__ для ',  str(cls))
#         return super().__new__(cls)                 # Должен возвращать адрес нового созданного объекта
#
#     def __init__(self, x=0, y=0):                   # self ссылвается на экземпляр класса!
#         print('Вызов __init__ для  ', str(self))
#         self.x = x
#         self.y = y
#
# dp = Point(1, 2)
# print(dp)



        #  ПАТТЕРН Singleton

class Database:

    __instance = None       # ссылка на экземпляр класса !

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        Database.__instance = None      # Если объект будет удален сборщиком мусора, то мы присваеваем снова атрибуту __instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Соединение с базой данных {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Закрытие соединение с БД')

    def read(self):
        return 'данные из БД'

    def write(self, data):
        print(f'записть в БД {data}')


dp = Database('root', '1234', 80)
dp.connect()
dp2= Database('root2', '5678', 40)          # переприсвоилось
dp.connect()
print()

print(id(dp), id(dp2))         # dp2 ссылается на ранее созданный объект dp
dp.connect()