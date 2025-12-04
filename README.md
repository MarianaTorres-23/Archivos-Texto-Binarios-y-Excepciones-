Desarrollarás un programa en Python que permita administrar una pequeña colección de objetos digitales (ej.: canciones, personajes anime, armas de videojuegos, libros, mascotas virtuales, etc.).
El usuario podrá agregar ítems, listarlos y buscarlos.

🔧 Requisitos obligatorios del programa
Tu programa debe incluir:

1️⃣ Archivo de Texto (.txt)
Debe almacenar información descriptiva de cada elemento.
Ejemplo: nombre, categoría, año, creador, calificación, etc.

Debe incluir funciones para:

Crear el archivo si no existe

Guardar un nuevo elemento (append)

Leer y mostrar la lista completa

Buscar por nombre

2️⃣ Archivo Binario (.bin)
Usarás un archivo binario para guardar datos numéricos o estadísticos del mismo elemento.
Ejemplos:

Nivel de poder

Popularidad

Número de vistas

Rareza (1-100)

Debe incluir funciones para:

Escribir datos binarios

Leerlos correctamente

Asociarlos al archivo de texto (por el mismo nombre o ID)

3️⃣ Manejo de Excepciones
Tu programa DEBE manejar excepciones reales, por ejemplo:

Archivo no encontrado

Error al convertir datos

Entrada vacía

Intento de leer archivo inexistente

Error al abrir archivo binario

Usa por lo menos:

try

except

finally

Un raise en algún lugar para validar datos

4️⃣ Menú interactivo
Debe aparecer algo como:

===== MI COLECCIÓN DIGITAL =====
1. Agregar elemento
2. Mostrar colección completa
3. Buscar elemento por nombre
4. Mostrar datos binarios
5. Salir

5️⃣ Mínimo de registros
Debe permitir capturar al menos 5 elementos.


