from abc import ABCMeta, abstractmethod

class animal(metaclass=ABCMeta):
    @abstractmethod
    def talk(self, t):
        pass

class dog(animal):
    def talk(self):
        print('dog')

class cat(animal):
    def talk(self):
        print('cat')

class animal_factory():
    @staticmethod
    def MakeAnimal(t):
        if t == 'cat': return cat()
        if t == 'dog': return dog()

an = animal_factory.MakeAnimal('cat')
an.talk()
