# Una excepción es un error pero el código sigue, solo es una notificación que se le da al usuario
# While True: Bluce infinito

while True:
    number_1 = input('Por favor ingrese un número\n')
    number_2 = input('Por favor ingrese otro número\n')

# se va a ejecutar y posiblemente altera el codigo, try es intento
    try:
        total = int(number_1)/int(number_2)
        print (f"El resultado es: {total}")
        
# si hay una excepción, ejecute la línea 13
    except Exception as e:
        print(f"Se produjo un error de tipo: {e}")



#    try:
#        total = int(number_1)/int(number_2)
#        print (f"El resultado es: {total}")
#    except ValueError:
#        print('ERROR: por favor ingrese solo números')
#    except ZeroDivisionError:
#        print('ERROR: INDETERMINADO')