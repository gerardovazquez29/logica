
"""
1. El Clasificador de Números
Objetivo: Practicar condicionales y entrada de datos.

Escriba un programa que pida al usuario un número entero. El programa debe 
determinar y perder si el número es:

Positivo, negativo o cero.
Par o impar.
Ejemplo: Si el usuario ingresa -4, el programa debe decidir: 
"El número es negativo y par".    
"""
numero = int(input('escribe un numero: '))


if numero > 0 and numero % 2 == 0:
    print(f'el numero que ingresaste {numero} es positivo y par')
elif numero > 0  and  numero % 2 != 0:
    print(f'el numero que ingresaste {numero} es positivo e impar')
elif numero < 0 and numero % 2 != 0:
    print(f'el numero que ingresaste {numero} es negativo e impar')
elif numero < 0 and numero % 2 == 0:
    print(f'el numero que ingresaste {numero} es negativo y par')
else:
    print(f'el numero que ingresaste {numero} es cero')


"""
    2. La Suma Acumulativa
Objetivo: Bucles Practicar while y acumuladores.
Crea un programa que pida números al usuario continuos. 
El programa debe ir sumando estos nuevos numeros. El núcleo debe contenerse cuando 
el usuario ingrese el número 0. Al final, muestre la suma total de todos los números 
ingresados (excluyendo el 0 final).
 """

suma = 0

numero = int(input('Ingresa un numero (0 para salir): '))
while numero != 0:
    suma = suma + numero
    numero = int(input('Ingresa otro numero (0 para salir): '))

print(f"La suma total de los numeros que ingresaste es: {suma}")

"""
3. Contador de Vocales
Objetivo: Practicar bucles for y manipulación de cadenas (strings).

Pide al usuario que ingrese una frase o palabra. El programa debe recorrer 
la cadena y contar cuántas vocales (a, e, i, o, u) contiene, 
sin importar si son mayúsculas o minúsculas.

Ejemplo: "Hola Mundo" -> Tiene 4 vocales.
"""
frase = input('Ingresa una frase: ').lower()

vocales = 'aeiou'
total = 0

for palabra in frase:
    if palabra in vocales:
        total += 1
print(total)

"""
4. La Tabla de Multiplicar
Objetivo: Practicar bucles for y formato de salida.

Pide al usuario un número entero positivo. El programa debe imprimir la 
tabla de multiplicar de ese número del 1 al 10.

Ejemplo: Si el usuario elige 5:
5 x 1 = 5
5 x 2 = 10
"""
numeros = int(input('Ingresa un numero: '))

for i in range(1, 11):
    resultado = numeros * i
    print(f"{numeros} X {i} = {resultado}")


"""
5. Adivina el Número (Mini Juego)
Objetivo: Practicar lógica, condicionales y la librería random.

El programa debe generar un número aleatorio entre 1 y 20 (necesitarás import random). 
Luego, dale al usuario 3 intentos para adivinarlo.

Si el usuario acierta, felicítalo y termina el programa.
Si falla, dile si el número secreto es mayor o menor que el que ingresó.
Si se agotan los intentos, revela cuál era el número secreto.
"""

import random 

def juego_adivinanza():
    numero_secreto = random.randint(1,20)
    intentos_maximos = 3
    ganaste = False
    print('He pensado en un numero entre 1 y 20. podras adivinar')
    print(f'Tienes {intentos_maximos} intentos para adivinarlo.')

    for i in range(intentos_maximos):
        print(f' \n Intento numero {i + 1}')
        usuario = int(input('¿cual es tu numero?: '))

        if usuario == numero_secreto:
            print(f'¡Felicidades! adivinaste el numero {numero_secreto}')
            ganaste = True
            break

        elif usuario < numero_secreto:
            print('El numero secreto es mayor.')
        else:
            print('El numero secreto es menor.')
        
    if not ganaste:
            print(f'\n ¡Game Over! Se acabaron los intentos.')
            print(f'El numero secreto era: {numero_secreto}')
juego_adivinanza()
