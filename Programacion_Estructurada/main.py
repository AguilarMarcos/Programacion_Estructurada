import main2

# def main():
#     opcion = True
#     while opcion:
#         main2.borrarPantalla()
#         opcion = main2.menu_principal()
#         match opcion:
#             case "1":
#                 main2.registrar_videojuego()
#                 main2.esperarTecla()
#             case "2":
#                 main2.mostrar_inventario()
#                 main2.esperarTecla()
#             case "3":
#                 main2.vender_videojuego()
#                 main2.esperarTecla()
#             case "4":
#                 main2.rentar_videojuego()
#                 main2.esperarTecla()
#             case "5":
#                 opcion = False
#                 main2.borrarPantalla()
#                 print("Terminaste la ejecución del sistema.")
#             case _:
#                 print("Opción inválida, vuelve a intentarlo.")
#                 main2.esperarTecla()

# if __name__ == "__main__":
#     main()

import main2

def main():
    while True:
        main2.borrarPantalla()
        opcion = main2.menu_inicial()
        if opcion == "1":
            if main2.verificar_admin():
                main2.menu_admin()
            else:
                print("Contraseña incorrecta. Acceso denegado.")
                main2.esperarTecla()
        elif opcion == "2":
            main2.menu_cliente()
        elif opcion == "3":
            main2.borrarPantalla()
            print("Terminaste la ejecución del sistema.")
            break
        else:
            print("Opción inválida, vuelve a intentarlo.")
            main2.esperarTecla()

if __name__ == "__main__":
    main()