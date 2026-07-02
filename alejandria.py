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

def main():
    libros = []
    usuarios = []
    
    opcion = ""

    while opcion != "9":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nFunción registrar libro en desarrollo...")
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