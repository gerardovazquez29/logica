""" 
Ejercicio 1: Contador de Números Pares e Impares
Crea un programa que reciba una lista de números y cuente cuántos son pares e impares.
 """
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = 0
impares = 0
for num in numeros:
    if num % 2 == 0:
        pares += 1        
    else:
        impares += 1
print(f"pares: {pares}")
print(f"impares: {impares}")

""" 
Ejercicio 2: 
Filtrador de Palabras Largas
Dado un diccionario con nombres y edades, crea una nueva lista solo 
con los nombres que tengan más de 5 letras. 
"""
# Ejemplo de entrada
personas = {
    "Ana": 25,
    "Roberto": 30,
    "Luis": 22,
    "Mariana": 28,
    "José": 35
}
nombre_largo = []

for nombre in personas:
    if len(nombre) > 5:
        nombre_largo.append(nombre)
print(nombre_largo)
        
# Debe devolver: ["Roberto", "Mariana"]
