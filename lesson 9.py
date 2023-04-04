#9. Свойства property. Декоратор @property
# https://www.youtube.com/watch?v=MxviMwbGl3I&ab_channel=selfedu

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):              # Через геттеры и сеттеры мы взаимодействуем с приватными атрибутами!
        return self.__old

    def set_old(self, old):         # Через геттеры и сеттеры мы взаимодействуем с приватными атрибутами!
        self.__old = old

    old = property(get_old, set_old)     # объекс свойства property предназначен чтобы не запоминать названия get_old и set_old,
                                            #  мы можем напрямую обращаться к атрибуду old для вывода или изменения

    @property
    def name(self):                 # ЭТО геттер !! @propery ОБЯЗАТЕЛЬНО ПЕРЕД ГЕТТЕРОМ!
        return self.__name

    @name.setter
    def name(self, name):           # это сеттер !!
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name


p = Person('Sergey', 20)
p2 = Person('Igor', 16)
print(p.old, ', выводится за счет property p')
print(p2.get_old(), ', выводится за счет get_old p2')

p.set_old(35)               # меняется за счет set_old
print(p.get_old(), ', выводится за счет get_old p, а меняется за счет get_old')
p2.old = 27             # меняется за счет property p2
print(p2.old, ', выводится за счет property p2')

print()

print('вывод через декоратор p:', p.name)
print('вывод через декоратор p2:', p2.name)

p.name = 'Kirill'           # Изменение через декоратор
p2.name = 'Katya'           # Изменение через декоратор

print('вывод через декоратор p:', p.name)
print('вывод через декоратор p2:', p2.name)
print()
del p.name                  # Удаление через декоратор !
print(p.__dict__)           # мы удалили name через декоратор, выведется только old

# ЗАМЕТКИ
# Приоритет всегда идет на property ! т.е любое обращение в первую очередь к свойству property, даже если в классе есть атрибут с таким же именем!