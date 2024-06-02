class Digit:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значение не соответствует типу объекта')
        self.vel = value


class Integer(Digit):
    def __init__(self, value):
        super().__init__(value)
        if type(value) != int:
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):
    def __init__(self, value):
        super().__init__(value)
        if type(value) != float:
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):
    def __init__(self, value):
        super().__init__(value)
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):
    def __init__(self, value):
        super().__init__(value)
        if value > -1:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    def __init__(self, v):
        super().__init__(v)


class FloatPositive(Float, Positive):
    def __init__(self, v):
        super().__init__(v)


digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
          FloatPositive(3.5), FloatPositive(8.9)]

lst_positive = []  ##  все объекты, относящиеся к классу Positive;

lst_float = []  ##все объекты, относящиеся к классу Float.

for X in digits:
    if isinstance(X, Positive):
        lst_positive.append(X)
    elif isinstance(X, Float):
        lst_float.append(X)
