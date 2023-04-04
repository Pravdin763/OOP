#39. Python Data Classes при наследовании

from dataclasses import dataclass, field, InitVar
from typing import Any


class GoodsMethodFactory:   # класс для  measure

    @staticmethod
    def get_init_measure():
        return [0, 0, 0]

@dataclass
class Goods:            # базовый класс
    current_uid = 0     # декоратор его НЕ видит, тк. он не аннотирован никаким типом! (и никуда не добавит)

    uid: int = field(init=False)    # он не попадет в инициализатор __init__(), его формируем сами через post_init
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print('Goods post_init')
        Goods.current_uid +=1
        self.uid = Goods.current_uid

@dataclass
class Book(Goods):
    title: str = ''         # они идут после uid, price, weight, т.к. переопределяются
    author : str = ''       # они идут после uid, price, weight, т.к. переопределяются
    price: float = 0
    weight: int | float = 0
    measure :list = field(default_factory=GoodsMethodFactory.get_init_measure)  # вызывается функция из класса

    def __post_init__(self):
        super().__post_init__()     # если не написать, то метод post_init в Goods НЕ вызывается, соответсвтвенно uid НЕ формируется - ошибка
        print('Book post_init')


b = Book()
print(b)
b2 = Book(1000, 100, 'питон ООП', 'Правдин И')
print(b2)