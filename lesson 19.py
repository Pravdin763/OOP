# #19. Магические методы __iter__ и __next__

class Frange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.i = self.start - self.step         # !
        return self

    def __next__(self):
        if self.i + self.step < self.stop:
            self.i += self.step
            return self.i
        else:
            raise StopIteration


class Frange2d:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):  # rows - колличество строк
        self.rows = rows
        self.fr = Frange(start, stop, step)         # !


    def __iter__(self):
        self.value = 0          # !
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value +=1
            return iter(self.fr)
        else:
            raise StopIteration

fr = Frange2d(0.0, 2.0, 0.5, 4)

for i in fr:
    for x in i:
        print(x, end=' ')
    print()

