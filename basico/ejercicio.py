
def mostrar_menu():
    print('\n=== MENU TAREAS ===')
    print('1. Agregar tareas')
    print('2. Listar tareas')
    print('3. Marcar tareas como completada')
    print('4. Salir')

def pedir_opcion():
    try:
        return int(input('Elige una opcion: '))
    except ValueError:
        print('Error: Ingresa un numero valido.')
        return None

def main():
    tareas = []

    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion is None:
            continue

        if opcion == 1:
            titulo = input('Titulo de la tarea: ')
            tareas.append({'titulo': titulo, 'completada': False})
        
        elif opcion == 2:
            if not tareas:
                print('No hay tareas.')
            for i, tarea in enumerate(tareas):
                estado = 'ok' if tarea['completada'] else 'X'
                print(f'{i}.[{estado}] {tarea['titulo']}')
        
        elif opcion == 3:
            try:
                indice = int(input('Indice de la tarea: '))
                tareas[indice]['completada'] = True
            except (ValueError, IndexError):
                print('Error: indice invalido.')
        
        elif opcion == 4:
            print('Saliendo...')
            break
        else:
            print('Opcion no valida.')


if __name__ == '__main__':
    main()
    