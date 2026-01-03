
""" Ejercicio 1: Contador de Números Pares e Impares """

numeros = [12,7,23,45,8,16,33,50,9,14]

total = {'pares': 0, 'impares': 0}

for num in numeros:
    if num % 2 == 0:
        total['pares'] += 1
    else:
        total['impares'] += 1

print(total)  # {'pares': 5, 'impares': 5}


# Ejercicio 2
# Filtrador de palabras
palabras = ["python", "sol", "programacion", "casa", "desarrollo", "luz", "computadora"]

mas_de_5 = []

for letra in palabras:
    if len(letra) > 5:
        mas_de_5.append(letra)
   
print(mas_de_5)
