#12. Магический метод __call__. Функторы и классы-декораторы

# https://www.youtube.com/watch?v=UqX5Qekb9sU&ab_channel=selfedu

class Counter:
    def __init__(self):
        self.__counter =0

    def __call__(self, step =1, *args, **kwargs):    # с помойшью этого маг. метода, можно вызывать () экземпляры класса
        print('__call__')
        self.__counter +=step
        return self.__counter

c = Counter()
c2 = Counter()

c(2)     #1
c(step=10)     #2
res2 = c2(5)    #1
c()     #3
res = c()   #4
print(res, res2)
print()

class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('должна быть строкой')
        return args[0].strip(self.__chars)      # Удаляем вконце и вначале все сиволы переданные в аргумент chars

s1 = StripChars('?!*_ .,')
res = s1('? Hi Igor you Ahuenniy!!!*.')
res2 = s1('!  Ahulit Ahulit   !')
print(res)
print(res2)

print()

import math
class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.001, *args, **kwargs):       # автоматически вызывается метод call
        return (self.__fn(x+dx) - self.__fn(x)) / dx

@Derivate               # Декорируем функцию синуса
def sinx(x):
    return math.sin(x)

print(sinx(0.0014))