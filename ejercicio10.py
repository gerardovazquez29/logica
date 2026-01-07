
# Ejercicio 1: Filtrar números pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
print(pares)  # [2, 4, 6, 8, 10]
    
    
    
# Calificaciones aprobadas

calificaciones = [5, 7, 8, 4, 9, 6, 3, 10]

aprobadas = []

for a in calificaciones:
    if a >= 6:
        aprobadas.append(a)
print(aprobadas)