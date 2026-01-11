
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)


calificaciones = [5, 7, 8, 4, 9, 6, 3, 10]

aprovado = []
reprovado = []

for n in calificaciones:
    if n >= 6:
        aprovado.append(n)
    else:
        reprovado.append(n)
print(f"calificaciones aprovadas: {aprovado}")