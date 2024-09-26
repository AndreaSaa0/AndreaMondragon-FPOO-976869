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
        return f"{self.name} {self.last_name}"

person1 = Person(dni = 123, name="Luisito", lastname = "Velez", role=1)

print(person1)