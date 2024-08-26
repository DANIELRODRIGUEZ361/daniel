def crear_persona():
    nombre = input("Ingrese el nombre de la persona: ")
    personas.append(nombre)
    print("Persona agregada:", nombre)
    print("Lista de personas:", personas)
    menu()

def eliminar_persona():
    if len(personas) == 0:
        print("No hay personas en la lista")
    else:
        print("Lista de personas:")
        for i, persona in enumerate(personas):
            print(f"{i+1}. {persona}")
        indice = int(input("Ingrese el índice de la persona a eliminar: ")) - 1
        if 0 <= indice < len(personas):
            personas.pop(indice)
            print("Persona eliminada")
        else:
            print("Índice inválido")
    menu()

def listar_personas():
    print("Lista de personas:")
    for persona in personas:
        print(persona)
    menu()

def buscar_persona():
    nombre = input("Ingrese el nombre de la persona a buscar: ")
    print("Persona encontrada" if nombre in personas else "Persona no encontrada")
    menu()

def menu():
    print("Menú:")
    print("1. Crear persona")
    print("2. Eliminar persona")
    print("3. Listar personas")
    print("4. Buscar persona")
    print("5. Salir")
    opcion = input("Ingrese una opción: ")
    {
        "1": crear_persona,
        "2": eliminar_persona,
        "3": listar_personas,
        "4": buscar_persona,
        "5": lambda: print("Adiós")
    }.get(opcion, lambda: print("Opción inválida"))()

personas = ["Juan", "Maria", "Carlos", "Ana", "Pedro", "Sofia", "Luis", "Isabel"]
menu()
