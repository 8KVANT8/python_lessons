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

