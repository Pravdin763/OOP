#34. Метаклассы. Объект type / #35. Пользовательские метаклассы.

# class Point:
#     max_coord = 100
#     min_coord = 0
#
# class B1:
#     pass
#
# class B2:
#     pass
#
# P = type('Point', (B1, B2), {'max_coord': 100, 'min_coord': 0})  # Альтернативное (динамическое) создание класса

#P.__mro__()

# def create_class_point(name, base, attrs):      # метакласс с помощю функции      # 1 способ
#     attrs.update({'max_coord': 100, 'min_coord': 0})
#     return type(name, base, attrs)

class Meta(type):
    def __new__(cls, name, base, attrs):                     # 2 способ
        attrs.update({'max_coord': 100, 'min_coord': 0})
        return type.__new__(cls, name, base, attrs)
    # def __init__(cls, name, base, attrs):                  # 3 способ
    #     super().__init__(name, base, attrs)
    #     cls.max_coord = 100
    #     cls.min_coord = 0

class Point(metaclass=Meta):  # или create_class_point тогда раскоментить функцию или Meta
    def get_coords(self):
        return (0, 1)


pt = Point()
print(pt.max_coord)
print(pt.get_coords())