
palabra = input('Ingresa una palabra a tu eleccion: ')
vocales = 'aeiou'
contador = 0

for letra in palabra.lower():
    if letra in vocales:
        contador += 1

print(f"La palabra {palabra} tiene: {contador} vocales")

print('-'*30)

frase = input('Ingresa una palabra: ').lower()

vocales1 = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0 }
for vocal in frase:
    if vocal in vocales1:
        vocales1[vocal] += 1

print(f"la palabra: {frase} contiene: {vocales1} vocales")
print(f"Total: {sum(vocales1.values())}")

