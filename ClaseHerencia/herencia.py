# superclase
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__ (self, nombre, edad, dueno):
        self.nombre = nombre
        self.edad = edad
        self.dueno = dueno

    # metodo
    @abstractmethod
    def hacer_sonido(self):
        return f"El animal hace un sonido"

#subclase
class Perro(Animal):
    def __init__(self, nombre, edad, dueno, raza, color):
        super().__init__(nombre, edad, dueno)
        self.raza = raza
        self.color = color

    def hacer_sonido(self):
        return 'Guau'

# animal_1 = Animal('Gato', 1, 'Maria')
# print(animal_1.nombre, animal_1.edad, animal_1.dueno)

perro = Perro ('Copito', 2, 'Luis', 'Labrador', 'Marron')
print(perro.nombre, perro.edad, perro.dueno, perro.raza, perro.color)
print(perro.hacer_sonido())

