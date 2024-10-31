class Mascota:
    def __init__(self, nombre, especie, edad):
        self._nombre = nombre
        self._especie = especie
        self.edad = edad

    def __str__(self):
        return f" Nombre: {self._nombre}, Especie: {self._especie}, Edad: {self.edad}"

class Dueño:
    def __init__(self, nombre, telefono):
        self._nombre = nombre
        self._telefono = telefono
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def __str__(self):
        mascota_info = ""
        for mascota in self.mascotas:
            mascota_info += str(mascota) + "\n"
        return f"Dueño: {self._nombre}, Telefono: {self._telefono}\nMascotas:\n{mascota_info.strip()}"

class Consulta:
    def __init__(self, fecha, motivo, mascota):
        self.fecha = fecha
        self.motivo = motivo
        self.mascota = mascota

    def __str__(self):
        return f"Fecha: {self.fecha}, Motivo: {self.motivo}, Mascota: {self.mascota}"

Mascota_1 = Mascota('Lucas', 'Beagle', 8)
Mascota_2 = Mascota('Bruno', 'Chanda', 3)

Andrea = Dueño('Andrea', '1234567890')

Andrea.agregar_mascota(Mascota_1)
Andrea.agregar_mascota(Mascota_2)

Consulta_1 = Consulta('30-Octubre-2024', 'Tos', Mascota_1) 

print(Consulta_1)
print(Andrea)