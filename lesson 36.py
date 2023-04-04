#36. Метаклассы в API ORM Django

# class Meta(type):                                         # 1 реализация
#     def create_locale_attrs(self, *args, **kwargs):
#         for key, value in self.class_attrs.items():
#             self.__dict__[key] = value
#
#     def __init__(cls, name, base, attrs):
#         cls.class_attrs = attrs
#         cls.__init__ = Meta.create_locale_attrs
#
#
#
# class Women(metaclass=Meta):
#     title ='Заголовок'
#     content = 'Контент'
#     photo = 'Путь к фото'




class Women:                                                # 2 реализация, тоже самое
    class_attrs = {'title': 'заголовок', 'content': 'контент', 'photo': 'Путь к фото'}
    title = 'Заголовок'
    content = 'Контент'
    photo = 'Путь к фото'

    def __init__(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value



w = Women
print(w.__dict__)