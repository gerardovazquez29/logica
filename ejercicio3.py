
suma_positivos = 0
cantidad_negativa = 0

while True:
    numero = int(input('Ingresa varios numeros (Ingresa 0 para salir): '))

    if numero == 0:
        break

    elif numero > 0:
        suma_positivos += numero

    else:
        cantidad_negativa += 1

print(f"Suma de positivos: {suma_positivos}")
print(f"Cantidad de negativos: {cantidad_negativa}")
