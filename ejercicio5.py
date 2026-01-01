
"""
Ejercicio 3: Inversión de Cadenas
Crea una función que reciba una palabra y la devuelva invertida, 
pero sin usar el método [::-1] de Python. 
El objetivo es que uses un bucle para entender cómo se reconstruye la cadena.
"""

palabra = 'python'
resultado = ''

for letra in palabra:
    resultado = letra + resultado 
print(resultado)



def encontrar_primer_duplicado(numeros):
    vistos = set()
    for num in numeros:
        if num in vistos:
            return num
        vistos.add(num)
    return None

listas = [3,1,4,2,1,5]
print(f"El duplicado es: {encontrar_primer_duplicado(listas)}")
    
    
    