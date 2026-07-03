# BIBLIOTECA ALEJANDRIA
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


def validar_texto(mensaje):
    texto = input(mensaje).strip()

    while texto == "":
        print("Error: el campo no puede quedar vacío.")
        texto = input(mensaje).strip()

    return texto


def validar_stock():
    stock_total = int(input("Ingrese la cantidad de ejemplares: "))

    while stock_total <= 0:
        print("Error: el stock debe ser mayor a 0.")
        stock_total = int(input("Ingrese la cantidad de ejemplares: "))

    return stock_total


def libro_repetido(libros, titulo, autor):
    for datos_libro in libros:
        if (
            datos_libro["titulo"].lower() == titulo.lower()
            and datos_libro["autor"].lower() == autor.lower()
        ):
            return True

    return False


def registrar_libro(libros):
    print("\n--- REGISTRO DE LIBRO ---")

    id_libro = len(libros) + 1
    titulo = validar_texto("Ingrese el título del libro: ")
    autor = validar_texto("Ingrese el autor del libro: ")
    categoria = validar_texto("Ingrese la categoría del libro: ")

    if libro_repetido(libros, titulo, autor):
        print("\nError: ya existe un libro registrado con ese título y autor.")
    else:
        stock_total = validar_stock()

        datos_libro = {
            "id": id_libro,
            "titulo": titulo,
            "autor": autor,
            "categoria": categoria,
            "stock_total": stock_total,
            # Le asignamos la misma variable del total por el momento pero cuando desarrollemos la funcion de prestamos y devoluciones ese valor va a cambiar
            "stock_disponible": stock_total,
            "veces_prestado": 0
        }

        libros.append(datos_libro)

        print("\nLibro registrado correctamente.")
        print("ID asignado:", id_libro)


def listar_libros(libros):
    print("\n--- LISTADO DE LIBROS ---")

    if len(libros) == 0:
        print("No hay libros registrados.")
    else:
        for datos_libro in libros:
            print("\nID:", datos_libro["id"])
            print("Título:", datos_libro["titulo"])
            print("Autor:", datos_libro["autor"])
            print("Categoría:", datos_libro["categoria"])
            print("Stock total:", datos_libro["stock_total"])
            print("Stock disponible:", datos_libro["stock_disponible"])
            print("Veces prestado:", datos_libro["veces_prestado"])
            print("\n----------------------------------------")

    print("\nCantidad total de libros registrados:", len(libros))


def obtener_libro(libros, id_buscado):
    for datos_libro in libros:
        if datos_libro["id"] == id_buscado:
            return datos_libro
    return None


def buscar_libro(libros):
    print("\n--- BUSQUEDA DE LIBRO ---")

    if len(libros) == 0:
        print("No hay libros registrados.")
        return

    id_buscado = int(input("Ingrese el ID del libro a buscar: "))

    libro_encontrado = obtener_libro(libros, id_buscado)

    if libro_encontrado is None:
        print("No se encontró un libro con ese ID.")
    else:
        print("\nLibro encontrado:")
        print("ID:", libro_encontrado["id"])
        print("Título:", libro_encontrado["titulo"])
        print("Autor:", libro_encontrado["autor"])
        print("Categoría:", libro_encontrado["categoria"])
        print("Stock total:", libro_encontrado["stock_total"])
        print("Stock disponible:", libro_encontrado["stock_disponible"])
        print("Veces prestado:", libro_encontrado["veces_prestado"])


# Aprovechamos esta oportunidad de corregir errores para poder agregar la funcionalidad de obtener usuarios similar a la de obtener libros
def obtener_usuario(usuarios, dni_buscado):
    for datos_usuario in usuarios:
        if datos_usuario["dni"] == dni_buscado:
            return datos_usuario

    return None


def registrar_usuario(usuarios):
    print("\n--- REGISTRO DE USUARIO ---")

    dni = validar_texto("Ingrese el DNI del usuario: ")

    usuario_encontrado = obtener_usuario(usuarios, dni)

    if usuario_encontrado is not None:
        print("\nError: ya existe un usuario registrado con ese DNI.")
    else:
        nombre = validar_texto("Ingrese el nombre del usuario: ")
        apellido = validar_texto("Ingrese el apellido del usuario: ")

        datos_usuario = {
            "dni": dni,
            "nombre": nombre,
            "apellido": apellido
        }

        usuarios.append(datos_usuario)

        print("\nUsuario registrado correctamente.")
        print("DNI:", dni)

def realizar_prestamo(libros, usuarios, prestamos):
    print("\n--- REALIZAR PRÉSTAMO ---")

    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
        return

    if len(libros) == 0:
        print("No hay libros registrados.")
        return

    dni = validar_texto("Ingrese el DNI del usuario: ")
    usuario_encontrado = obtener_usuario(usuarios, dni)

    if usuario_encontrado is None:
        print("Error: no existe un usuario registrado con ese DNI.")
        return

    id_libro = int(input("Ingrese el ID del libro a prestar: "))
    libro_encontrado = obtener_libro(libros, id_libro)

    if libro_encontrado is None:
        print("Error: no existe un libro registrado con ese ID.")
        return

    dia_prestamo = int(input("Ingrese el día del préstamo: "))
    dia_limite = dia_prestamo + 7

    id_prestamo = len(prestamos) + 1

    datos_prestamo = {
        "id_prestamo": id_prestamo,
        "dni_usuario": dni,
        "id_libro": id_libro,
        "dia_prestamo": dia_prestamo,
        "dia_limite": dia_limite,
        "dia_devolucion": 0,
        "estado": "ACTIVO",
        "multa": 0
    }

    prestamos.append(datos_prestamo)

    print("\nPréstamo registrado correctamente.")
    print("ID del préstamo:", id_prestamo)
    print("Usuario:", usuario_encontrado["nombre"], usuario_encontrado["apellido"])
    print("Libro:", libro_encontrado["titulo"])
    print("Día del préstamo:", dia_prestamo)
    print("Día límite de devolución:", dia_limite)

def main():
    libros = []
    usuarios = []
    prestamos = []

    opcion = ""

    while opcion != "9":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_libro(libros)
        elif opcion == "2":
            registrar_usuario(usuarios)
        elif opcion == "3":
            listar_libros(libros)
        elif opcion == "4":
            buscar_libro(libros)
        elif opcion == "5":
            realizar_prestamo(libros, usuarios, prestamos)
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