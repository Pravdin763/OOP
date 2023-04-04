#33. Вложенные классы |

class Women:
    title = 'объект класса для поля title'
    photo = 'объект класса для поля photo'
    ordering = 'объект класса для поля ordering'

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + '@' + psw)     # из класса Women можем обращаться к свойствам класса Meta, НО не наоборот

    class Meta:         # во вложенных классах обращаться к атрибутам внешнего класса нельзя!
        ordering = ['id']

        def __init__(self, access):
            self._access = access
            self._t = Women.title       # Обращение из класса Meta к свойству класса Women, НО так делать НЕ  РЕКОМЕНДУЕТСЯ!


w = Women('root', '12345')
print(w.ordering)
print(w.Meta.ordering)
print(w.__dict__)
print(w.meta.__dict__)