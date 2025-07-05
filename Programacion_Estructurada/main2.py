import os

# Lista global para almacenar los videojuegos
videojuegos = []

def borrarPantalla():
    os.system("cls")  # cls para Windows

def esperarTecla():
    input("Presiona Enter para continuar...")

def menu_inicial():
    print("\n=== Bienvenido al Sistema de Gestión de Videojuegos ===")
    print("1. Modo Administrador")
    print("2. Modo Cliente")
    print("3. Salir")
    opcion = input("Elige una opción (1-3): ")
    return opcion

def verificar_admin():
    contraseña = input("Ingresa la contraseña del administrador: ")
    return contraseña == "1234"

def menu_admin():
    opcion = True
    while opcion:
        borrarPantalla()
        print("\n=== Menú Administrador ===")
        print("1. Registrar videojuego")
        print("2. Mostrar inventario")
        print("3. Volver al menú inicial")
        opcion = input("Elige una opción (1-3): ")
        match opcion:
            case "1":
                registrar_videojuego()
                esperarTecla()
            case "2":
                mostrar_inventario()
                esperarTecla()
            case "3":
                opcion = False
            case _:
                print("Opción inválida, vuelve a intentarlo.")
                esperarTecla()

def menu_cliente():
    opcion = True
    while opcion:
        borrarPantalla()
        print("\n=== ¡Bienvenido a la Tienda de Videojuegos! ===")
        print("1. Ver catálogo de videojuegos")
        print("2. Comprar un videojuego")
        print("3. Rentar un videojuego")
        print("4. Salir de la tienda")
        opcion = input("¿Qué deseas hacer? (1-4): ")
        match opcion:
            case "1":
                mostrar_inventario()
                esperarTecla()
            case "2":
                comprar_videojuego()
                esperarTecla()
            case "3":
                rentar_videojuego(es_admin=False)
                esperarTecla()
            case "4":
                opcion = False
                print("¡Gracias por visitar la tienda! Vuelve pronto.")
            case _:
                print("Opción inválida, por favor elige una opción válida.")
                esperarTecla()

def registrar_videojuego():
    borrarPantalla()
    print("Registrar Videojuego")
    nombre = input("Nombre del videojuego: ").strip().title()
    tipo = input("Tipo (venta/renta): ").lower()
    while tipo not in ["venta", "renta"]:
        print("Tipo inválido. Por favor, ingresa 'venta' o 'renta'.")
        tipo = input("Tipo (venta/renta): ").lower()
    precio = float(input("Precio: "))
    stock = int(input("Cantidad disponible: "))
    
    juego = {
        "nombre": nombre,
        "tipo": tipo,
        "precio": precio,
        "stock": stock
    }
    videojuegos.append(juego)
    print(f"{nombre} registrado correctamente.")

def mostrar_inventario():
    borrarPantalla()
    print("--- Catálogo de Videojuegos ---")
    if len(videojuegos) == 0:
        print("No hay videojuegos disponibles en la tienda.")
    else:
        for i, juego in enumerate(videojuegos, start=1):
            print(f"{i}. {juego['nombre']} | Tipo: {juego['tipo']} | Precio: ${juego['precio']} | Stock: {juego['stock']}")
    print("--------------------------")

def mostrar_inventario_renta():
    borrarPantalla()
    print("--- Videojuegos Disponibles para Renta ---")
    disponibles = [juego for juego in videojuegos if juego["tipo"] == "renta" and juego["stock"] > 0]
    if len(disponibles) == 0:
        print("No hay videojuegos disponibles para renta.")
    else:
        for i, juego in enumerate(disponibles, start=1):
            print(f"{i}. {juego['nombre']} | Precio: ${juego['precio']} | Stock: {juego['stock']}")
    print("--------------------------")

def vender_videojuego(es_admin=False):
    borrarPantalla()
    if es_admin:
        mostrar_inventario()
    nombre = input("Nombre del videojuego a vender: ").strip()
    for juego in videojuegos:
        if es_admin:
            if juego["nombre"].lower() == nombre.lower():
                if juego["stock"] > 0:
                    print(f"El precio de {juego['nombre']} es ${juego['precio']}.")
                    try:
                        pago = float(input("Ingresa el monto a pagar: $"))
                        if pago >= juego["precio"]:
                            juego["stock"] -= 1
                            cambio = pago - juego["precio"]
                            print(f"¡Venta realizada! Has vendido {juego['nombre']}.")
                            if cambio > 0:
                                print(f"Cambio: ${cambio:.2f}.")
                            print(f"Stock restante: {juego['stock']}.")
                        else:
                            print("Monto insuficiente. La venta no se realizó.")
                    except ValueError:
                        print("Por favor, ingresa un monto válido.")
                else:
                    print("No hay stock disponible para venta.")
                return
        else:
            if juego["nombre"].lower() == nombre.lower() and juego["tipo"] == "venta":
                if juego["stock"] > 0:
                    print(f"El precio de {juego['nombre']} es ${juego['precio']}.")
                    try:
                        pago = float(input("Ingresa el monto a pagar: $"))
                        if pago >= juego["precio"]:
                            juego["stock"] -= 1
                            cambio = pago - juego["precio"]
                            print(f"¡Compra realizada! Has comprado {juego['nombre']}.")
                            if cambio > 0:
                                print(f"Tu cambio es ${cambio:.2f}.")
                            print(f"Stock restante: {juego['stock']}.")
                        else:
                            print("Monto insuficiente. La compra no se realizó.")
                    except ValueError:
                        print("Por favor, ingresa un monto válido.")
                else:
                    print("No hay stock disponible para comprar este videojuego.")
                return
    print("Videojuego no encontrado o no disponible para venta.")

def comprar_videojuego():
    borrarPantalla()
    mostrar_inventario()
    nombre = input("Nombre del videojuego a comprar: ").strip()
    for juego in videojuegos:
        if juego["nombre"].lower() == nombre.lower() and juego["tipo"] == "venta":
            if juego["stock"] > 0:
                print(f"El precio de {juego['nombre']} es ${juego['precio']}.")
                try:
                    pago = float(input("Ingresa el monto a pagar: $"))
                    if pago >= juego["precio"]:
                        juego["stock"] -= 1
                        cambio = pago - juego["precio"]
                        print(f"¡Compra realizada! Has comprado {juego['nombre']}.")
                        if cambio > 0:
                            print(f"Tu cambio es ${cambio:.2f}.")
                        print(f"Stock restante: {juego['stock']}.")
                    else:
                        print("Monto insuficiente. La compra no se realizó.")
                except ValueError:
                    print("Por favor, ingresa un monto válido.")
            else:
                print("No hay stock disponible para comprar este videojuego.")
            return
    print("Videojuego no encontrado o no disponible para compra.")

def rentar_videojuego(es_admin=False):
    borrarPantalla()
    if es_admin:
        mostrar_inventario()
    else:
        mostrar_inventario_renta()
    nombre = input("Nombre del videojuego a rentar: ").strip()
    for juego in videojuegos:
        if es_admin:
            if juego["nombre"].lower() == nombre.lower():
                if juego["stock"] > 0:
                    print(f"El precio de renta de {juego['nombre']} es ${juego['precio']}.")
                    try:
                        pago = float(input("Ingresa el monto a pagar: $"))
                        if pago >= juego["precio"]:
                            juego["stock"] -= 1
                            cambio = pago - juego["precio"]
                            print(f"¡Renta realizada! Has rentado {juego['nombre']}.")
                            if cambio > 0:
                                print(f"Tu cambio es ${cambio:.2f}.")
                            print(f"Stock restante: {juego['stock']}.")
                        else:
                            print("Monto insuficiente. La renta no se realizó.")
                    except ValueError:
                        print("Por favor, ingresa un monto válido.")
                else:
                    print("No hay stock disponible para renta.")
                return
        else:
            if juego["nombre"].lower() == nombre.lower() and juego["tipo"] == "renta":
                if juego["stock"] > 0:
                    print(f"El precio de renta de {juego['nombre']} es ${juego['precio']}.")
                    try:
                        pago = float(input("Ingresa el monto a pagar: $"))
                        if pago >= juego["precio"]:
                            juego["stock"] -= 1
                            cambio = pago - juego["precio"]
                            print(f"¡Renta realizada! Has rentado {juego['nombre']}.")
                            if cambio > 0:
                                print(f"Tu cambio es ${cambio:.2f}.")
                            print(f"Stock restante: {juego['stock']}.")
                        else:
                            print("Monto insuficiente. La renta no se realizó.")
                    except ValueError:
                        print("Por favor, ingresa un monto válido.")
                else:
                    print("No hay stock disponible para renta.")
                return
    print("Videojuego no encontrado o no disponible para renta.")