
# validador de parentesis

def es_valida(cadena):
    pila = []
    mapa = {')': '(','}': '{', ']': '['}

    for caracter in cadena:
        if caracter in mapa:
            elemento_tope = pila.pop() if pila else '#'

            if mapa[caracter] != elemento_tope:
                return False
        else:
            pila.append(caracter)
    return not pila

print(es_valida('()[]{}'))
print(es_valida('([)]'))

# fiz-buz

for i in range(1,21):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('buzz')
    elif i % 3 == 0:
        print('Fizz')
    else :
        print(i)


def filtrar_aprobados(estudiantes, nota_minima=60):
    aprobados = []
    for estudiante in estudiantes:
        if estudiante >= nota_minima:
            aprobados.append(estudiante)
    return aprobados

notas = [45,70,85,50,90,65]
print(filtrar_aprobados(notas))
  