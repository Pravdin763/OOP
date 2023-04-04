#25. Множественное наследование
# https://www.youtube.com/watch?v=9YPooWY6x9o&ab_channel=selfedu
 #    MRO - алгоритм обхода базовых классов !

class Goods:
    def __init__(self, name, weight, price):
        super().__init__()          # вызывает метод из класса Mixenlog, ИНАЧЕ может быть ошибка!!
        print('init Goods')
        self.name = name
        self.weight = weight
        self. price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


class Mixenlog:     # логирование
    ID = 0
    def __init__(self):         # Можно указать параметры, НО НЕ рекомендуется, обычно только self
        super().__init__()
        print(' init MixenLog')
        Mixenlog.ID +=1         # реализацию не понял, так надо...
        self.ID = Mixenlog.ID   # реализацию не понял, так надо...

    def save_salle_log(self):
        print(f'{self.ID} товар был продан в 00:00 часов')

    def print_info(self):
        print(f'Вызов метода {self.__class__} из Mixenlog')


class Mixenlog2:
    def __init__(self):
        super().__init__()
        print('Mixenlog2')

    def print_shtoto(self):
        print('Для примера')

    def print_info(self):
        print(f'Вызов метода {self.__class__} из Mixenlog2')




class Notebook(Goods, Mixenlog, Mixenlog2):        # Порядок классов ОЧЕНЬ ВАЖЕН, обращаются поочереди!
    def print_info(self):           # ПЕРЕОПРЕДЕЛИЛИ, ЧТОБЫ МЕТОД print_info ВСЕГДА ВЫЗЫВАЛСЯ ИЗ КЛАССА Mixenlog !!
        Mixenlog.print_info(self)


n = Notebook('Acer', 1.5, 30000)
n.print_info()          # вызывается из Goods, елси убрать print_info из класса Notebooks
n.save_salle_log()
print(Notebook.__mro__)         # Показывает как идет до object
n.print_shtoto()
Mixenlog.print_info(n)          # Если мы РАЗОВО хотим вызвать метод из класса, который НЕ первый, в данном примере Mixenlog
Mixenlog2.print_info(n)         # 2 пример
n.print_info()
