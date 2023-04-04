#16. Магические методы __eq__ и __hash__
#  https://www.youtube.com/watch?v=Cfx4VCnWeCE&ab_channel=selfedu

class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def __eq__(self, other):            # ПЕРЕОПРЕДЕЛИЛИ    Будет ошибка
        return self.x == other.x and self.y ==other.y

    def __hash__(self):                 # теперь ошибки не будет!
        return hash((self.x, self.y))   # вычисляем хэш КОРТЕЖА!

p = Point(1, 2)
p2 = Point(1, 2)
print(hash(p), hash(p2))    # разынй хэш, воспринимаются как НЕизменяемые

d = {}

d[p] = 1
d[p2] = 2
print(d)    # p и p2 воспринимается как один и тотже ключ