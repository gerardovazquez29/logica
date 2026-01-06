
# Ejercicio 1: Buscador de Precios

productos = {"Laptop": 800, "Mouse": 20, 
             "Teclado": 45, "Monitor": 150, 
             "Cable": 10}

productos_modificados = []


for producto, precio in productos.items():
    if precio >= 50 :
        nuevo_precio = precio * 0.9
    else:
        nuevo_precio = precio
    productos_modificados.append(nuevo_precio)
    ofertas = f"El Producto {producto} ahora cuesta {nuevo_precio}"
    print(ofertas)
""" 
El Producto Laptop ahora cuesta 720.0
El Producto Mouse ahora cuesta 20     
El Producto Teclado ahora cuesta 45   
El Producto Monitor ahora cuesta 135.0
El Producto Cable ahora cuesta 10   
"""
# Ejercicio 2: Suma de Números Positivos

datos = [10, 5, -3, 20, -8, 15, 0, 30, 5]

total = 0


for numero in datos:
    if numero > 0:
       total += numero
    elif numero == 0:
        break
    print(total)
