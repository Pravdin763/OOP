#37. Введение в Python Data Classes (часть 1)

from dataclasses import dataclass, field
from pprint import pprint

class Tging:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):             # метод, ктороый вместо абракадабры выводит параметры при печати экземпляра класса
        return f'Thing {self.__dict__}'



@dataclass          # магический метод __init__(), __repr__(), __eq__()(сравнение)
class ThingData:
    name: str      # аннотация обязательна !
    weight: int
    price: float = 0       # по умолчанию можно тольк НЕИЗМЕНЯЕМЫЕ объекты
    dims: list = field(default_factory=list)    # Благодаря этому можно по умолчанию объявить измен. объект, например list и он для КАЖДОГО ЭКЗЕМПЛЯРА КЛАССА СВОЙ!!

t = Tging('Учений Питона', 77, 100)             # стандартным способом и маг метод repr
td = ThingData('Учений Питона 2 ', 78, 101)     # с помощю декоратора dataclass
print(t)
print(td)
print()
#pprint(ThingData.__dict__)     # новая библиотека pprint
td2 = ThingData('Ученик ООП ', 79, 1000)
td3 = ThingData('Ученик ООП ', 79, 1000)
print(td ==td2)
print(td2==td3)
print()

dt4 = ThingData('Ученик ООП 2 ', 80, 100)
dt4.dims.append(10)     # добавляем в dt4
print(dt4.dims)         # благодаря list = field(default_factory=list)  разные значения
dt5 = ThingData('Ученик ООП 3 ', 10, 10)
print(dt5.dims)         # благодаря list = field(default_factory=list)  разные значения
