#18. Магические методы __getitem__, __setitem__ и __delitem__
# https://www.youtube.com/watch?v=EAoiOwYQSuY&t=8s&ab_channel=selfedu

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):        # item - индекс. Позволяет НАПРЯМУЮ выводить элемент по индексу ОТ ЭКЗЕМПЛЯРА КЛАССА
        if 0 <= item <len(self.marks):
            return self.marks[item]
        else:
            raise IndexError('НЕверный индекс')

    def __setitem__(self, key, value):
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым числом')
        del self.marks[key]

s1 = Student('Sergey', [5, 5, 3, 2, 4])
print(s1[2])        # без getitem была бы ошибка, пришлось бы печатать s1.marks[2]
s1[2]=1     # устанавливем благодаря setitem, иначе ошибка!
print(s1[2])
del s1[2]   # благодаря delitem удалили элемент из списка
print(s1.marks)