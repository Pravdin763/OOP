#3. Инициализатор __init__ и финализатор __del__
# https://www.youtube.com/watch?v=-J3Ou8-8vVk&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=4&ab_channel=selfedu

#   __Магический метод__

class Point:
    color = 'red'
    circle = 2
    def __init__(self, x=0, y=0):           # магический метод инициализатор объекта класса
        self.x = x
        self.y = y

    def __del__(self):                      # Финализатор магический метод del
        print('Удаление экземпляра ', str(self))
    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

pt = Point(1, 2)
pt2 = Point()
print(pt.__dict__)
print(pt2.__dict__)