#10. Пример использования объектов property
# https://www.youtube.com/watch?v=ury9pdPXa6s&ab_channel=selfedu

class Person:
    def __init__(self, fio, old, ps, weight):
        self.verifyfio(fio)                 # Подгружаем проверку на фио
        self.verifyold(old)                 # Подгружаем проверку на возраст
        self.verifyps(ps)                   # Подгружаем проверку на паспорт
        self.verifyweight(weight)           # Подгружаем проверку на вес

        self.__fio = fio.split()
        self.__old = old
        self.__ps = ps
        self.__weight = weight

    @classmethod
    def verifyfio(cls, fio):        # Проверка на фио, если не проходит, возбуждаем ошибку, иначе, все ок
        if type(fio) != str:
            raise TypeError('Не верный тип ввода ФИО')
        f = fio.split()
        if len(f)!=3:
            raise TypeError('Не верный формат записи')
        f1 = fio.replace(' ', '')
        if f1.isalpha() == False:
            raise TypeError('ФИО должно содержать только буквы алфавита')

    @classmethod
    def verifyold(cls, old):        # Проверка на возраст, если не проходит, возбуждаем ошибку, иначе, все ок
        if type(old) != int:
            raise TypeError('Не верный формат ввода, должно быть цело число')
        if old > 100 or old < 14:
            raise TypeError('Возраст должен быть от 14 до 100 лет')

    @classmethod
    def verifyps(cls, ps):          # Проверка на паспорт, если не проходит, возбуждаем ошибку, иначе, все ок
        if type(ps) != str:
            raise TypeError('Не верный формат ввода, должна быть строка')
        p = ps.split()
        if len(p[0]) != 4 or len(p[1]) !=6 or len(p) !=2:
            raise TypeError('Не верный формат паспорта, должно быть 4 и 6 цифр разделенных пробелом')
        p1 = ps.replace(' ', '')
        if p1.isdigit() ==False:
            raise TypeError('серия номер паспорта должна содержать только цифры')

    @classmethod
    def verifyweight(cls, weight):      # Проверка на вес, если не проходит, возбуждаем ошибку, иначе, все ок
        if not isinstance(weight, (int, float)):
            raise TypeError('Не верный формат ввода, должно быть целое илии вещественное число')
        if weight < 20 or weight >150:
            raise TypeError('Не верно указан вес или вы слишком жирный!')

                    # геттеры и сеттеры нужны, чтобы мы могли обращаться к __приватным атрибутам вне класса. (выводить, изменять)
    @property
    def fio(self):          # геттер ФИо
        return self.__fio

    @property               # Геттер возраста
    def old(self):
        return self.__old

    @old.setter             # сеттер возраста
    def old(self, old):
        self.verifyold(old)
        self.__old = old

    @property               # Геттер веса
    def weight(self):
        return self.__weight

    @weight.setter          # сеттер веса
    def weight(self, weight):
        self.verifyweight(weight)
        self.__weight = weight

    @property               # Геттер паспорта
    def ps(self):
        return self.__ps

    @ps.setter              #  cеттер паспорта
    def ps(self, ps):
        self.verifyps(ps)
        self.__ps = ps



p = Person('Правдин Игорь Николаевич', 27, '6314 123456', 80.3)
p.old = 99
p.ps = '9911 123456'
p.weight = 75.5
print(p.__dict__)
print(p.old)
