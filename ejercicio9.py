
# Filtrar y transformar
import random

lista = [random.randint(1,50) for i in range(10)]
print(f"lista: {lista}")

lista_pares = [num for num in lista if num % 2 == 0]
print(f"lista pares: {lista_pares}")

#* Ejercicio 1: Filtrar Números Primos de una Lista

numeros = [2, 8, 13, 15, 17, 20, 23, 28, 29, 31, 35, 37]
num_primos = []

for n in numeros:
    if n < 2:
        continue
    
    es_primo = True
    for d in range(2, n):
        if n % d == 0:
            es_primo = False
            break
    if es_primo:
        num_primos.append(n)
print(num_primos)
# [2, 13, 17, 23, 29, 31, 37]   
        
 
#* Ejercicio 2: Análisis de Inventario        

inventario = {
    "laptop": 5,
    "mouse": 15,
    "teclado": 0,
    "monitor": 8,
    "webcam": 12,
    "audifonos": 3
}

stock_bajo = []
total_producto = 0
disponibles = []

for producto, cantidad in inventario.items():
    total_producto += cantidad
    
    if cantidad < 10 and cantidad > 0:
       stock_bajo.append(f"{producto} ({cantidad})")
       
    if cantidad > 0:    
        disponibles.append(producto)
print(f"Stock Bajo: {', '.join(stock_bajo)}")
print(f"Total productos: {total_producto}")
print(f"Disponibles: {', '.join(disponibles)}")
"""   
Stock Bajo: laptop (5), monitor (8), audifonos (3)    
Total productos: 43
Disponibles: laptop, mouse, monitor, webcam, audifonos 
"""
         