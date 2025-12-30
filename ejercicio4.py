"""_summary_
Ejercicio 1: Números Pares e Impares
Crea un programa que reciba una lista de números y devuelva dos listas: 
una con los números pares y otra con los impares.
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(pares)  # [2, 4, 6, 8, 10]
print(impares)  #  [1, 3, 5, 7, 9]


"""
Ejercicio 2: Contador de Vocales
Crea una función que reciba una cadena de texto y 
cuente cuántas vocales tiene (sin importar mayúsculas o minúsculas).    
"""

def contador_vocales(texto):
    vocales = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    texto  = texto.lower()
    for letras in texto:
        if letras in vocales:
            vocales[letras] += 1
    for vocal, cantidad in vocales.items():
        print(f"{vocal}: {cantidad}")        
    total = sum(vocales.values())
    print(f"\nTotal de vocales: {total}")

contador_vocales('Python es genial ')

    
    
    

def son_vocales(texto):
    con_vocal = input("Ingresa un texto: ")
    vocales = 'aeiou'
    contador = []
    
    for letra in con_vocal.lower():
        if letra in vocales:
            contador.append(letra)
    return contador
texto = son_vocales('')
print(texto)
