# tupla_1 = ('Hola', 'Mundo', 9, 24.3, 'Hola', 'hola',)


# #Datos de accesibilidad
# print(tupla_1[0]) #muestra lo que hay en esa posición
# print(tupla_1.index('Mundo')) #muestra el espacio

# #Slicing
# print(tupla_1[1:3]) #sirve para truncar información, es decir, mostramos solo lo que queremos

# print(tupla_1.count('Hola')) #¿Cuántos elementos hay una tupla? en este ejemplo los 'Hola'

# # (tupla_1[0]) = 'Hola'

tupla_1 = ('Hola', 'Mundo', 9, 24.3)
#tipo_dato(aqui): Casting, parseo
tupla_to_list = list(tupla_1)

tupla_to_list.append(10)

list_to_tupla = tuple(tupla_to_list)

print(tupla_1)
print(tupla_to_list)
print(list_to_tupla)






#tupla es un conjunto de datos inmutable, siempre tiene el mismo estado... aunque se puede hacer modificaciones indirectas
#como por ejemplo la cédula


