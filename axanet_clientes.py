import os
from datetime import datetime

# Directorio donde se guardarán los archivos de clientes
DIRECTORIO = "C:/Users/Roque/Documents/PROYECTOS SENCILLOS/axanet_clientes_python"

# en caso de no existir crear
if not os.path.exists(DIRECTORIO):
    os.makedirs(DIRECTORIO)
    print(f"📁 Directorio de clientes creado en: {DIRECTORIO}")

#  FUNCIONES 

def generar_id(nombre):
    """Genera un ID único basado en el nombre y la fecha/hora actual"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    id_cliente = nombre[:2].upper() + "_" + timestamp
    return id_cliente
#crear cliente
def crear_cliente():
    print("\n🧾 Crear nuevo cliente")
    nombre = input("Ingrese el nombre completo del cliente: ").strip()
    telefono = input("Ingrese el teléfono: ").strip()
    correo = input("Ingrese el correo electrónico: ").strip()
    primer_servicio = input("Ingrese la primera solicitud: ").strip()
#en caso de tener un cliente ya creado
    archivo = os.path.join(DIRECTORIO, f"{nombre.replace(' ', '_')}.txt")
    if os.path.exists(archivo):
        print("⚠️ El cliente ya existe.")
        return

    fecha_registro = datetime.now().strftime("%Y-%m-%d")
    id_cliente = generar_id(nombre)
#datos requeridos
    with open(archivo, "w", encoding="utf-8") as f:
        f.write(f"Nombre: {nombre}\n")
        f.write(f"ID_Cliente: {id_cliente}\n")
        f.write(f"Telefono: {telefono}\n")
        f.write(f"Correo: {correo}\n")
        f.write(f"FechaRegistro: {fecha_registro}\n")
        f.write("Servicios:\n")
        f.write(f"- {primer_servicio} ({fecha_registro})\n")

    print(f"✅ Cliente {nombre} creado correctamente.")
#listar os clientes ya creados desde el directorio
def listar_clientes():
    print("\n📋 Lista de clientes existentes:")
    archivos = os.listdir(DIRECTORIO)
    clientes = [a.replace(".txt", "") for a in archivos if a.endswith(".txt")]
    if clientes:
        for c in clientes:
            print("-", c)
    else:
        print("No hay clientes registrados ")
# ver el cliente de la misma manera desde el directorio ya creado
def ver_cliente():
    nombre = input("\nIngrese el nombre del cliente a visualizar: ").strip()
    archivo = os.path.join(DIRECTORIO, f"{nombre.replace(' ', '_')}.txt")
    if os.path.exists(archivo):
        print(f"\n📄 Información de {nombre}:")
        with open(archivo, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("El cliente no existe.")

def agregar_servicio():
    nombre = input("\nIngrese el nombre del cliente a modificar: ").strip()
    archivo = os.path.join(DIRECTORIO, f"{nombre.replace(' ', '_')}.txt")
    if os.path.exists(archivo):
        nueva_solicitud = input("Ingrese la nueva solicitud: ").strip()
        fecha = datetime.now().strftime("%Y-%m-%d")
        with open(archivo, "a", encoding="utf-8") as f:
            f.write(f"- {nueva_solicitud} ({fecha})\n")
        print("Solicitud agregada correctamente.")
    else:
        print("El cliente no existe.")

def eliminar_cliente():
    nombre = input("\nIngrese el nombre del cliente a eliminar: ").strip()
    archivo = os.path.join(DIRECTORIO, f"{nombre.replace(' ', '_')}.txt")
    if os.path.exists(archivo):
        confirmar = input(f"¿Está seguro de eliminar a {nombre}? (s/n): ").strip().lower()
        if confirmar == "s":
            os.remove(archivo)
            print(f"🗑️ Cliente {nombre} eliminado correctamente.")
        else:
            print("Eliminación cancelada.")
    else:
        print("El cliente no existe.")

# ======= MENÚ PRINCIPAL =======

def menu():
    while True:
        print("\n========= MENÚ AXANET PYTHON =========")
        print("1. Crear nuevo cliente")
        print("2. Listar clientes")
        print("3. Ver cliente")
        print("4. Agregar servicio a cliente")
        print("5. Eliminar cliente")
        print("6. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            ver_cliente()
        elif opcion == "4":
            agregar_servicio()
        elif opcion == "5":
            eliminar_cliente()
        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("Opción no válida intente de nuevo")

if __name__ == "__main__":
    menu()
