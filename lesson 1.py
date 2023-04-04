# 1 Классы и объекты. Атрибуты классов и объектов
# https://www.youtube.com/watch?v=P4CNNo8jWj4&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=2&ab_channel=selfedu

class Point:
    color = 'red'       # атрибуты(свойства)
    circle = 2          # атрибуты(свойства)
    # .__dict__    Выводит ВСЕ атрибуты класса
    # a = Point()     Экземпляр класса поинт
    #  getattr(класс, что ищем, False)  выводит True или False есть ли атрибут в классе
    #  hasattr(классб что ищем)  выводит True или False