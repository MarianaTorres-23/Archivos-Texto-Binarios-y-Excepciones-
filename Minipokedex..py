import os
import struct

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TXT_FILE = os.path.join(BASE_DIR, "pokedex.txt")
BIN_FILE = os.path.join(BASE_DIR, "pokedex.bin")

def validar_texto(texto):
    texto = texto.strip()
    if texto == "":
        raise ValueError("El campo no puede estar vacío.")
    return texto


def validar_entero(valor):
    try:
        numero = int(valor)
        return numero
    except:
        raise ValueError("Debes ingresar un número válido.")

def crear_archivo_txt():
    """Crea el archivo TXT si no existe."""
    if not os.path.exists(TXT_FILE):
        with open(TXT_FILE, "w", encoding="utf-8") as f:
            f.write("NOMBRE|TIPO|REGION|AÑO\n")
        print(f"Archivo TXT creado en:\n{TXT_FILE}")
    else:
        print("Archivo TXT ya existe.")


def agregar_txt(nombre, tipo, region, anio):
    with open(TXT_FILE, "a", encoding="utf-8") as f:
        f.write(f"{nombre}|{tipo}|{region}|{anio}\n")
    print("Guardado en TXT ✔")


def leer_txt():
    try:
        with open(TXT_FILE, "r", encoding="utf-8") as f:
            lineas = f.readlines()

            if len(lineas) <= 1:
                print("No hay registros.")
                return

            print("\n===== POKÉDEX (TXT) =====")
            for linea in lineas[1:]:
                datos = linea.strip().split("|")
                print(f"- {datos[0]} | Tipo: {datos[1]} | Región: {datos[2]} | Año: {datos[3]}")

    except FileNotFoundError:
        print("ERROR: El archivo TXT no existe.")


def buscar_txt(nombre):
    try:
        with open(TXT_FILE, "r", encoding="utf-8") as f:
            for linea in f:
                if linea.startswith(nombre + "|"):
                    datos = linea.strip().split("|")
                    return datos
    except FileNotFoundError:
        print("ERROR: archivo TXT no encontrado.")
    return None

def agregar_binario(poder, rareza):
    """Guarda 2 enteros por registro."""
    try:
        with open(BIN_FILE, "ab") as f:
            f.write(struct.pack("ii", poder, rareza))
        print("Guardado en BINARIO ✔")
    except Exception as e:
        print("ERROR al escribir binario:", e)


def leer_binario():
    """Lee registros de 2 enteros (8 bytes cada uno)."""
    try:
        with open(BIN_FILE, "rb") as f:
            print("\n===== DATOS BINARIOS =====")
            index = 1
            while True:
                data = f.read(8)
                if not data:
                    break
                poder, rareza = struct.unpack("ii", data)
                print(f"Elemento {index}: Poder={poder}, Rareza={rareza}")
                index += 1

    except FileNotFoundError:
        print("ERROR: No existe el archivo binario.")

def menu():
    crear_archivo_txt()

    while True:
        print("\n===== MINI POKÉDEX =====")
        print("1. Agregar Pokémon")
        print("2. Mostrar colección")
        print("3. Buscar por nombre")
        print("4. Mostrar datos binarios")
        print("5. Salir")

        opc = input("Elige una opción: ")

        if opc == "1":
            try:
                nombre = validar_texto(input("Nombre: "))
                tipo = validar_texto(input("Tipo: "))
                region = validar_texto(input("Región: "))
                año = validar_entero(input("Año aparición: "))
                poder = validar_entero(input("Nivel de poder: "))
                rareza = validar_entero(input("Rareza: "))

                agregar_txt(nombre, tipo, region, año)
                agregar_binario(poder, rareza)

            except ValueError as e:
                print("ERROR:", e)

        elif opc == "2":
            leer_txt()

        elif opc == "3":
            nombre = input("Ingresa nombre: ").strip()
            resultado = buscar_txt(nombre)

            if resultado:
                print("\nRESULTADO:")
                print(f"Nombre: {resultado[0]}")
                print(f"Tipo: {resultado[1]}")
                print(f"Región: {resultado[2]}")
                print(f"Año: {resultado[3]}")
            else:
                print("No se encontró el Pokémon.")

        elif opc == "4":
            leer_binario()

        elif opc == "5":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
