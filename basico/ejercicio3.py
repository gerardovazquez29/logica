n = int(input('ingresa un numero: '))
print(f'Numeros pares desde 1 hasta {n}: ')

for i in range(1, n +1):
    if i % 2 == 0:
        print(i, end=' ')
print()


contador_mayores_10 = 0

print('Ingresa 5 numeros enteros: ')

for i in range(5):
    numero = int(input(f'Ingresa un numero {i + 1}: '))
    if numero > 10:
        contador_mayores_10 += 1

print(f'Hay {contador_mayores_10} numeros mayores que 10.')

