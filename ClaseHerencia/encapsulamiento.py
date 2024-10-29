# Superclase(Clase Padre): Es de la que heredan.
# Subclase (Clase Hija): Esta hereda de otra clase.
# getters and setters
# getter es un metodo que da el nombre y setters permite cambiar el nombre y es otro metodo
# @ indica que es un decorado, ej: @property     y significa que todo metodo se vuelve una propiedad
# metodo ()   y propiedad sin parentesis
# setter es un decorador

# doble __ encapsula y _ lo quita

# templatestr es poder acompañar una variable

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter and Setters

    @property
    def name (self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f"Persona(name= {self.__name}, age={self.__age})"

person_1 = Person('Maria', 18)

print(person_1.name, person_1.age)

person_1.name = 'Maria Fernanda'
person_1.age = 19

print(person_1.name, person_1.age)


print(person_1)