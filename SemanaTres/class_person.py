#-----------------
#Person

#dni: int
#name: str
#lastname: int
#role: int

#-----------------

class Person:
    def __init__(self, dni: int, name: str, lastname: str, role: int):
        self.dni = dni
        self.name = name
        self.last_name = lastname
        self.role = role

    def __repr__ (self):
        return f"{self.dni} {self.name} {self.last_name} {self.role}"

person1 = Person(dni = 123, name="Luisito", lastname = "Velez", role=1)
person2 = Person(dni = 456, name="Andrea", lastname = "Saa", role=2)
person3 = Person(dni = 789, name="Diana", lastname = "Hernandez", role=3)
person4 = Person(dni = 101112, name="David", lastname = "Castro", role=4)

print(person1)
print(person2)
print(person3)
print(person4)