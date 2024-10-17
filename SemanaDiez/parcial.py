class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"Autor: {self.nombre} ({self.nacionalidad})"

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Libro: {self.titulo} - {self.autor}"

class Seccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def libros_por_autor(self, autor):
        return [libro for libro in self.libros if libro.autor == autor]

    def __str__(self):
        resultado = f"Sección: {self.nombre}\n"
        for libro in self.libros:
            resultado += str(libro) + "\n"
        return resultado

# Mostrar los autores y sus libros
autor_1 = Autor("Gabriel García Márquez", "Colombiano")
autor_2 = Autor("Miguel de Cervantes", "Español")

libro_1 = Libro("Cien años de soledad", autor_1)
libro_2 = Libro("La Galatea", autor_2)
libro_3 = Libro("El amor en los tiempos del cólera", autor_1)

# Se muestran todos los libros agregados
seccion_1 = Seccion("Libros Latinos")
seccion_1.agregar_libro(libro_1)
seccion_1.agregar_libro(libro_2)
seccion_1.agregar_libro(libro_3)

print(seccion_1)

# Obtenemos lo libros del autor Gabriel García Marquez
libros_gabriel_garcia_marquez = seccion_1.libros_por_autor(autor_1)
print("\nLibros de Gabriel García Márquez:")
for libro in libros_gabriel_garcia_marquez:
    print(libro)