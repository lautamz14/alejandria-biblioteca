# BIBLIOTECA ALEJANDRIA 
# Por cuestiones organizativas de primera instancia vamos a separar el coddigo en ambiente y proceso para tener una estructura mas clara
# Ambiente

def mostrar_menu():
    print("\n========================================")
    print("       ALEJANDRÍA - BIBLIOTECA")
    print("========================================")
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Listar libros")
    print("4. Buscar libro")
    print("5. Realizar préstamo")
    print("6. Registrar devolución")
    print("7. Ver préstamos activos")
    print("8. Ver estadísticas")
    print("9. Salir")
    print("========================================")

def registrar_libro(libros):
    print("\n--- REGISTRO DE LIBRO ---")

    id_libro = len(libros) + 1
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    categoria = input("Ingrese la categoría del libro: ")
    stock_total = int(input("Ingrese la cantidad de ejemplares: "))

    libro = {
        "id": id_libro,
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "stock_total": stock_total,
        "stock_disponible": stock_total, # Le asignamos la misma variable del total por el momento pero cuando desarrollemos la funcion de prestamos y devoluciones ese valor va a cambiar
        "veces_prestado": 0 
    }

    libros.append(libro)

    print("\nLibro registrado correctamente.")
    print("ID asignado", id_libro)

def main():
    libros = []
    usuarios = []
    
    opcion = ""

    while opcion != "9":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_libro(libros)
        elif opcion == "2":
            print("\nFunción registrar usuario en desarrollo...")
        elif opcion == "3":
            print("\nFunción listar libros en desarrollo...")
            print("Cantidad de libros registrados:", len(libros))
        elif opcion == "4":
            print("\nFunción buscar libro en desarrollo...")
        elif opcion == "5":
            print("\nFunción realizar préstamo en desarrollo...")
        elif opcion == "6":
            print("\nFunción registrar devolución en desarrollo...")
        elif opcion == "7":
            print("\nFunción ver préstamos activos en desarrollo...")
        elif opcion == "8":
            print("\nFunción ver estadísticas en desarrollo...")
            print("Cantidad de libros registrados:", len(libros))
            print("Cantidad de usuarios registrados:", len(usuarios))
        elif opcion == "9":
            print("\nSaliendo del sistema Alejandría...")
        else:
            print("\nOpción inválida. Intente nuevamente.")

# Proceso

main()