# 8. Паттерн "Моносостояние"
# https://www.youtube.com/watch?v=WNj55JzXnvc&t=4s&ab_channel=selfedu

class Mono:

    __all_dict = {
        'name': 'Timur',
        'age': 27,
        'date': '29.10.2000'
    }

    def __init__(self):
        self.__dict__ = self.__all_dict     # !

m1 = Mono()
m2 = Mono()
m3 = Mono()

m1.name = 'igor'            # Меняем в м1
m2.age = 100                # Меняем в m2
m3.surname = 'Pravdin'      # Создаем новый атрибут в m3

print(m1.__dict__)          # они все одинаковые
print(m2.__dict__)          # они все одинаковые
print(m3.__dict__)          # они все одинаковые