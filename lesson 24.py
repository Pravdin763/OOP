#24. Полиморфизм и абстрактные методы
# https://www.youtube.com/watch?v=fzUI3NyJflw&t=3s&ab_channel=selfedu
class Geom:
    def get_pr(self):       # вызов метода get_pr из базового класса, если забыли добавить метод в нужный класс
        return f'Вызво метода из базового класса, добавьте метод get_pr в {self.__class__}'
class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h =h

    def get_pr(self):              # В каждом классе метод возврата периметра будет называться ОДИНАКОВО!
        return 2* (self.h + self.w)



class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):           # В каждом классе метод возврата периметра будет называться ОДИНАКОВО!
        return 4* self.a

class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    #def get_pr(self):          # В каждом классе метод возврата периметра будет называться ОДИНАКОВО!
        #return self.a + self.b + self.c        # Можно убрать # сделано специально, чтобы вызов был из базового класса Geom

r1 = Rectangle(1, 2)
r2 =Rectangle(3, 4)

s1 = Square(10)
s2 = Square(20)

t1 = Triangle(2, 4, 6)
t2 = Triangle(3, 5, 7)

#print(r1.get_rect_pr(), r2.get_rect_pr())
#print(s1.get_square(), s2.get_square())

geom = [r1, r2, s1, s2, t1, t2]

for i in geom:              # Вызов методов из разных классов!
    print(i.get_pr())