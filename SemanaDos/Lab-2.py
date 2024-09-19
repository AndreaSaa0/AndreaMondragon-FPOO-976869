# product
#     "id": 
#     "name":
#     "price":
#     "section":

# 1. tech
# 2. clothes
# 3. food

store = []

id = int(input("Por favor ingrese el id de su producto:\n"))
name = input("Por favor ingrese el nombre de su producto:\n")
price = float(input("Por favor ingrese el valor del producto a comprar:\n"))
section = input("Por favor ingrese la sección para su producto:\n")

product1 = {
    "id": id,
    "name": name,
    "price": price,
    "section": section

}

store.append(product1)

#Mostrar los productos del almacén
for product in store:
    print(product)
