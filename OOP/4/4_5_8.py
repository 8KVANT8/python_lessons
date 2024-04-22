from abc import ABC, abstractmethod
class CountryInterface(ABC):
    @abstractmethod
    @property
    def name (self):
        print("""Абстрактный объект-свойство""")
    @abstractmethod
    @property
    def population (self):
        print(  """Абстрактный объект-свойство""")
    
    @abstractmethod
    @property
    def square (self):
        print(  """Абстрактный объект-свойство""")

    @abstractmethod
    def get_info(self):
        print("""Абстрактный метод """)

class Country(CountryInterface):
    def __init__(self, name, population, square):
        self.name = name
        self.population = population
        self.square = square





