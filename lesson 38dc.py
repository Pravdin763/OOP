#38. Введение в Python Data Classes (часть 2) |

from dataclasses import dataclass, field, InitVar

class Vector3d:
    def __init__(self, x, y, z, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.lenght  = (x**2 +y**2 +z**2)**0.5 if calc_len else 0


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=True, frozen=False, slots=False)     # через = прописал И ТАК значения по умолчанию
class V3d:
    x: int = field(repr=False)  # не будет сразу печататься, только при конкретном вызове или dict
    y: int
    z: int = field(compare=False)   # игнорируется при сравнении
    calc_len: InitVar[bool] = True      # все что аннотированно InitVar, автоматически попадает в __post_init__
    lenght: float = field(init=False, compare=False, default=0)   # теперь будет попадать в __repr__

    def __post_init__(self, calc_len: bool):        # инициализирует в самом конце, если нужно ВЫЧЕСЛИТЬ
        if calc_len:
            self.lenght  = (self.x**2 +self.y**2 +self.z**2)**0.5       # в __repr__ не попадает


v = V3d(1, 2, 3)
print(v)        # x не отображается, потому что исключили из repr
print(v.__dict__)
v2 = V3d(1, 2, 5, False)
print(v ==v2)   # True потому что z не сравнивается, compare = False
print(v2)       # т.к. calc_len, меняет значение на False, то lenght не высчитывается, а принимает значение по умолчанию = 0


# ПАРАМЕТРЫ ДЛЯ field
# repr - использовать ли атрибут в маг. методе. по умолчанию True.  (repr сразу печатает значения при печати экземпляра класса)
# compare - использовать ли атрибут для сравнения объектов, по умолчанию True, если поставить False, то этот атрибут игнорируется при сравнении
# default - Значение по умолчанию

# *  все что аннотированно InitVar, автоматически попадает в __post_init__

# ПАРАМЕТРЫ декоратора dataclass
# init=True - объявляется инициализатор, False - не объявляется
# repr=True - объявляется магический метод repr
# eq=True - (==, !=)
# order=False - (<=, >=, >, <), использует метод eq, так что или оба True или order=False
# unsafe_hash - влияет на формирование метода __hash__()
# frozen=False - если True, то атрибуты объектов класса становятся НЕИЗМЕНЯЕМЫМИ!
# slots= False - если True, то атрибуты объявляются в коллекции slots