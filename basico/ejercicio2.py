
numeros = [12, 5, 3, 8, 2, 11, 10]

total = 0

for n in numeros:
    if n % 2 == 0:
        total += n

print(f'la lista es {numeros}')
print(f'la suma de los numeros pares es: {total}')


import random 

numero_secreto = random.randint(1,10)

adivinado = False

print('¡He pensado un numero del 1 al 10!')

while adivinado == False:
    try:
        numero = int(input('¿Cual crees que es: '))

        if numero == numero_secreto:
            print('¡Felicidades! el numero es correcto')
            adivinado = True
            

        elif numero > numero_secreto:
            print('el numero es mayor intenta de nuevo.')
        
        else:
            print('el numero es menor intenta de nuevo.')
    except ValueError:
        print('Ingrese un numero valido')
    