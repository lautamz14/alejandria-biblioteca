# Biblioteca Alejandría

## Integrantes

- Lautaro Hernan Mierez
- Dario Nicolas Godoy Pozzer
- Facundo Zapatero
- Facundo Acuña

## Comisión

Comisión: K1.2

## Descripción general del sistema

Biblioteca Alejandría es un sistema desarrollado en Python que permite gestionar operaciones básicas de una biblioteca desde la consola.

El sistema permite registrar libros, registrar usuarios, realizar préstamos, registrar devoluciones, controlar la disponibilidad de ejemplares, calcular multas por demora y visualizar estadísticas generales del funcionamiento de la biblioteca.

El proyecto fue desarrollado como Trabajo Integrador del Laboratorio de Python de la materia Algoritmos y Estructuras de Datos, aplicando contenidos trabajados durante el cursado, como estructuras condicionales, estructuras repetitivas, funciones, listas, diccionarios, validaciones, manejo básico de errores, acumuladores, contadores.

## Funcionalidades principales

El sistema cuenta con un menú principal que permite realizar las siguientes acciones:

1. Registrar libro.
2. Registrar usuario.
3. Listar libros.
4. Buscar libro por ID.
5. Realizar préstamo.
6. Registrar devolución.
7. Ver préstamos activos.
8. Ver estadísticas generales.
9. Salir del sistema.

## Estructuras utilizadas

El sistema utiliza principalmente listas y diccionarios para organizar la información.

Las listas principales son:

libros = []
usuarios = []
prestamos = []

Cada lista almacena diccionarios con los datos correspondientes.

### Datos de libros

Cada libro contiene:

{
    "id": id_libro,
    "titulo": titulo,
    "autor": autor,
    "categoria": categoria,
    "stock_total": stock_total,
    "stock_disponible": stock_disponible,
    "veces_prestado": veces_prestado
}

### Datos de usuarios

Cada usuario contiene:

{
    "dni": dni,
    "nombre": nombre,
    "apellido": apellido
}

### Datos de préstamos

Cada préstamo contiene:

{
    "id_prestamo": id_prestamo,
    "dni_usuario": dni_usuario,
    "id_libro": id_libro,
    "dia_prestamo": dia_prestamo,
    "mes_prestamo": mes_prestamo,
    "dia_limite": dia_limite,
    "mes_limite": mes_limite,
    "dia_devolucion": dia_devolucion,
    "mes_devolucion": mes_devolucion,
    "estado": estado,
    "multa": multa
}

##Archivos utilizados

Para conservar la información entre distintas ejecuciones del programa, el sistema utiliza archivos `.txt`.

Los archivos utilizados son:

- `libros.txt`
- `usuarios.txt`
- `prestamos.txt`

## Formato de los archivos

### libros.txt

Formato:

id|titulo|autor|categoria|stock_total|stock_disponible|veces_prestado

Ejemplo:

1|El principito|Antoine de Saint-Exupéry|Novela|4|3|1

### usuarios.txt

Formato:

dni|nombre|apellido

Ejemplo:

45678912|Juan|Pérez

### prestamos.txt

Formato:

id_prestamo|dni_usuario|id_libro|dia_prestamo|mes_prestamo|dia_limite|mes_limite|dia_devolucion|mes_devolucion|estado|multa

Ejemplo de préstamo activo:

1|45678912|1|10|5|17|5|0|0|ACTIVO|0

Ejemplo de préstamo devuelto:

2|40111222|3|10|5|17|5|20|5|DEVUELTO|15000

## Instrucciones de ejecución

Para ejecutar el sistema es necesario tener instalado Python.

Pasos para ejecutar:

1. Clonar o descargar el repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code o en una terminal.
3. Ejecutar el archivo principal:

python alejandria.py

En algunos sistemas también puede ejecutarse con:

py alejandria.py

El sistema se ejecuta por consola y muestra un menú interactivo. El usuario debe ingresar el número de la opción que desea utilizar.

##Validaciones implementadas

El sistema cuenta con distintas validaciones para evitar errores durante la ejecución y mejorar la confiabilidad del programa.

Algunas de las validaciones implementadas son:

- Control de campos vacíos.
- Validación de stock mayor a 0.
- Validación de entradas numéricas mediante manejo de errores.
- Validación de ID positivos.
- Validación de DNI con exactamente 8 dígitos numéricos.
- Control de usuarios repetidos mediante DNI.
- Control de libros repetidos mediante título y autor.
- Validación de días entre 1 y 30.
- Validación de meses entre 1 y 12.
- Control de disponibilidad antes de realizar un préstamo.
- Control de préstamos inexistentes.
- Control para evitar devolver dos veces el mismo préstamo.
- Validación para evitar el carácter `|` en textos, ya que se utiliza como separador en los archivos `.txt`.

## Manejo de fechas

Para el control de préstamos y devoluciones se utiliza un calendario simplificado.

El sistema considera que:

- Cada mes tiene 30 días.
- El año tiene 12 meses.
- El plazo de préstamo es de 7 días.
- El sistema solicita día y mes del préstamo.
- El sistema solicita día y mes de la devolución.

Esto permite calcular correctamente la demora incluso cuando la devolución ocurre en un mes distinto al del préstamo.

Ejemplo:

```text
Fecha de préstamo: 10/5
Fecha de devolución: 15/6
```

En este caso, el sistema interpreta que transcurrieron 35 días. Como el plazo permitido es de 7 días, se calcula una multa por los días de demora correspondientes.

##Multas

El sistema calcula multas cuando un libro se devuelve fuera del plazo establecido.

La multa diaria se define mediante una constante:

```python
MULTA_DIARIA = 5000
```

El cálculo se realiza de la siguiente manera:

```text
días de demora * multa diaria
```

Si el libro se devuelve dentro del plazo, no se aplica multa.

## Estadísticas generales

El sistema permite visualizar estadísticas generales de la biblioteca.

Entre ellas se incluyen:

- Cantidad de libros registrados.
- Cantidad de usuarios registrados.
- Cantidad de préstamos registrados.
- Cantidad de préstamos activos.
- Cantidad de préstamos devueltos.
- Stock total de ejemplares.
- Stock disponible total.
- Total acumulado en multas.
- Libro más solicitado.

Para calcular estas estadísticas se utilizan contadores, acumuladores y recorridos sobre las listas de datos.

## Casos de prueba realizados

Durante el desarrollo se realizaron pruebas manuales desde la consola para verificar el correcto funcionamiento del sistema.

Algunos casos probados fueron:

###Registro de libro válido

Se registró un libro ingresando título, autor, categoría y stock.

Resultado esperado:

- El libro se registra correctamente.
- Se asigna un ID.
- Se guarda en `libros.txt`.

### Registro de usuario válido

Se registró un usuario ingresando DNI, nombre y apellido.

Resultado esperado:

- El usuario se registra correctamente.
- Se guarda en `usuarios.txt`.

### Registro de usuario con DNI inválido

Se intentó registrar un usuario ingresando letras, menos de 8 dígitos o más de 8 dígitos en el DNI.

Resultado esperado:

- El sistema muestra un mensaje de error.
- El sistema vuelve a solicitar el DNI.

###Registro de usuario repetido

Se intentó registrar dos usuarios con el mismo DNI.

Resultado esperado:

- El sistema informa que ya existe un usuario registrado con ese DNI.

### Búsqueda de libro

Se buscó un libro mediante su ID.

Resultado esperado:

- Si el ID existe, el sistema muestra los datos del libro.
- Si el ID no existe, el sistema informa que no se encontró un libro con ese ID.

### Préstamo válido

Se realizó un préstamo con un usuario registrado y un libro con stock disponible.

Resultado esperado:

- El préstamo se registra correctamente.
- Se descuenta el stock disponible del libro.
- Aumenta el contador de veces prestado.
- Se guarda la información en `prestamos.txt`.

### Préstamo sin stock disponible

Se intentó prestar un libro sin ejemplares disponibles.

Resultado esperado:

- El sistema informa que no hay ejemplares disponibles.
- No se registra el préstamo.

### Devolución sin multa

Se registró una devolución dentro del plazo permitido.

Resultado esperado:

- El préstamo cambia su estado a `DEVUELTO`.
- Se aumenta el stock disponible del libro.
- No se aplica multa.

### Devolución con multa

Se registró una devolución fuera del plazo permitido.

Resultado esperado:

- El préstamo cambia su estado a `DEVUELTO`.
- Se calcula la multa correspondiente.
- Se actualiza el archivo `prestamos.txt`.

### Ingreso inválido en campos numéricos

Se ingresaron letras o símbolos en campos como stock, ID, día o mes.

Resultado esperado:

- El sistema muestra un mensaje de error.
- El programa no se interrumpe.
- El sistema vuelve a solicitar el dato.

## Organización del desarrollo

El proyecto fue desarrollado utilizando Git y GitHub como herramientas de control de versiones.

El repositorio evidencia el proceso de construcción del sistema mediante commits realizados durante el desarrollo, incorporando progresivamente distintas funcionalidades.

Algunas etapas del desarrollo fueron:

- Creación del menú principal.
- Registro de libros.
- Registro de usuarios.
- Listado de libros.
- Búsqueda de libros por ID.
- Implementación de préstamos.
- Control de disponibilidad.
- Registro de devoluciones.
- Cálculo de multas.
- Listado de préstamos activos.
- Estadísticas generales.
- Guardado de datos en archivos `.txt`.
- Carga de datos desde archivos `.txt`.
- Mejora del manejo de errores.
- Correcciones finales del sistema.

## Uso de Inteligencia Artificial

Durante el desarrollo del proyecto se utilizó Inteligencia Artificial como herramienta de apoyo al aprendizaje, a la programación y a la mejora general del sistema.

La herramienta utilizada fue:

GPT-5.5 Thinking

La IA fue utilizada principalmente para:

- Resolver dudas sobre sintaxis de Python.
- Corregir errores detectados durante el desarrollo.
- Analizar problemas de lógica dentro del sistema.
- Proponer estructuras de código más ordenadas.
- Colaborar en el diseño general del programa.
- Ayudar a modularizar el código mediante funciones.
- Mejorar validaciones y manejo de errores.
- Pulir detalles del sistema para lograr un resultado más profesional y elaborado.
- Asistir en el uso de archivos `.txt` para guardar y cargar información.
- Comprender conceptos que no conocíamos previamente, como el uso de `encoding="utf-8"` para trabajar correctamente con caracteres especiales en archivos de texto.

El uso de IA fue una herramienta de apoyo, pero no reemplazó el trabajo ni la comprensión del grupo. Las respuestas generadas fueron revisadas, adaptadas y probadas antes de incorporarse al proyecto.

Con los conocimientos básicos de programación que teníamos, la IA ayudó a comprender mejor ciertos conceptos, corregir errores y mejorar la calidad final del sistema. Sin embargo, los integrantes entendieron la lógica del programa, las estructuras utilizadas, las validaciones realizadas, el manejo de errores y el funcionamiento general del programa.

Muchas gracias por leer.
