#2. Методы классов. Параметр self
#  https://www.youtube.com/watch?v=Lw8TeLS4_IA&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=3&ab_channel=selfedu

class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):         # Метод класса (тоже атрибут класса)
        self.x = x          # Локальные свойства
        self.y = y

    def get_coords(self):
        return self.x, self.y

pt = Point()
pt2 = Point()
pt.set_coords(1, 2)
pt2.set_coords(10, 20)

f = getattr(pt, 'get_coords')
print(f())
