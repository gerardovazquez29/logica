
lista = [(3, 2), (1, 5), (4, 1)]
ordenada = sorted(lista, key=lambda x: x[0])
print(ordenada)  # [(1, 5), (3, 2), (4, 1)]

numeros = [1, 2, 3, 4, 5, 6, 25,28,36]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 28, 36]

