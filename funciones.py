
# Esta función imprime un saludo
def saludar():
    print("¡Hola, mundo!")  # Muestra el mensaje en pantalla

# Llamamos a la función para que se ejecute
saludar()

# Esta función recibe un nombre y saluda a esa persona
def saludar_persona(nombre):
    print("Hola", nombre)

saludar_persona("Gerardo")  # Llamamos a la función con un argumento

# Esta función suma dos números y devuelve el resultado
def sumar(a, b):
    resultado = a + b
    return resultado  # Devuelve el valor al llamador

total = sumar(3, 4)  # Guardamos el valor retornado en una variable
print("La suma es:", total)

# Si no se pasa un valor, se usa el valor por defecto "Invitado"
def saludar(nombre="Invitado"):
    print(f"Hola, {nombre}!")

saludar()           # Usa el valor por defecto
saludar("Gerardo")  # Usa el valor dado

# Esta función devuelve la suma y la resta de dos números
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta  # Devuelve dos valores

x, y = operaciones(10, 5)  # Desempaquetamos los resultados
print("Suma:", x)
print("Resta:", y)

def cuadrado(x):
    return x * x

def suma_de_cuadrados(a, b):
    return cuadrado(a) + cuadrado(b)

resultado = suma_de_cuadrados(2, 3)
print("Suma de cuadrados:", resultado)

# Función lambda para multiplicar dos números
multiplicar = lambda x, y: x * y
print(multiplicar(4, 5))  # Resultado: 20


def aplicar_funcion(func, valor):
    return func(valor)
def doble(n):
    return n * 2
print(aplicar_funcion(doble, 5))  # Pasa la función 'doble' como argumento


# Calcula el factorial de un número usando recursión
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))  # Resultado: 120


# *args permite pasar cualquier número de argumentos posicionales
def suma_total(*args):
    return sum(args)
print(suma_total(1, 2, 3, 4))  # Resultado: 10


# **kwargs permite pasar argumentos con clave-valor
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
mostrar_info(nombre="Gerardo", edad=30)
