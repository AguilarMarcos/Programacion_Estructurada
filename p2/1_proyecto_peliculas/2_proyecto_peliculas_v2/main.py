#proyecto 1 crear un proyecto que permita  gestionar (administrar peliculas) colocar un menu de opciones para agregar: borrar, modificar, consultar, buscar y vaciar peliculas

#notas: 
# 1 utilizar funciones y mandar llamar desde otro archivo
#2 utilizar una lista para almacenar los nombres
import os
os.system("cls")
import peliculas



#peliculas=[
 # ["gran turismo"],
  #["rapidos y furiosos 5"],
  #["ted 2"],
  #["mad max"],
  #["conjuro 3"],
  #["lluvia de hambuerguesas"],
  #["star wars"],
  #]

#print(peliculas)

opcion=True
while opcion:
    peliculas.borrarpantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- crear \n 2.- borrar \n 3.- mostrar \n 4.-agregar caracteristica \n 5.- modificar caracteristica \n 6.- borrar caracteristica \n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.crearpeliculas()
            peliculas.esperartecla()
        case "2":
            peliculas.borrarpeliculas()
            peliculas.esperartecla()
        case "3":
            peliculas.mostrarpeliculas()
            peliculas.esperartecla()
        case "4":
            peliculas.agregarcaracteristicaspeliculas() 
            peliculas.esperartecla()
        case "5": 
            peliculas.modificarCaracteristicaPeliculas()
            peliculas.esperartecla()
        case "6": 
            peliculas.borrarcaracteristicaspeliculas()
            peliculas.esperartecla()
        case "7":
            opcion=False    
            print(f"\n\"Terminaste la ejecucion del SW")
        case _: 
            input(f"\n\"Opción invalida vuelva a intentarlo ... por favor")