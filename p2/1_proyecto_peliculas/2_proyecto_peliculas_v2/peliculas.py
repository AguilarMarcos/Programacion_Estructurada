# disct u objeto para almacenar (nombre,categoria,clasificacion,genero,idioma) y sus valores 
peliculas={}

def borrarpantalla():
    import os
    os.system("cls")

def esperartecla():
    print("\n\t  oprima cualquier tecla para continuar...")
    input()

def crearpeliculas():
     borrarpantalla()
     print("\n\t.:: agregar peliculas ::. \n")
     peliculas.update({"nombre":input("ingresa el nombre:").upper().strip()})
     peliculas.update({"categoria":input("ingresa la categoria:").upper().strip()})
     peliculas.update({"clasificacion":input("ingresa la clasificacion:").upper().strip()})
     peliculas.update({"genero":input("ingresa el genero:").upper().strip()})
     peliculas.update({"idioma":input("ingresa el idioma:").upper().strip()})
     print("n\t\t:::¡la operacion se realizo con exito¡:::")

#def consultarpeliculas():
 #   borrarpantalla()
  #  print("\n\t :: consultar o modificar las peliculas ::. \n")
   # if len(peliculas)>0:   
    # for i in range(0,len(peliculas)):
     # print(f"\t{i + 1} : {peliculas[i]}")
    #else:
     #   print("\n\t.:: no hay peliculas en el sistema en este momento ")

def mostrarpeliculas():
   borrarpantalla()
   print("\n\t :: consultar o mostrar la pelicula :: \n ")
   if len(peliculas)>0:
        for i in peliculas:
           print(f"\t {(i)} : {peliculas[i]}")
       
# # def borrarpeliculas():
#     borrarpantalla()
#     print("\n\t :: quitar o borrar todas las peliculas :: \n ")
#     resp=input(" deseas borrorar o quitar todas las peliculas del sistemas (Si/No) ")
#     if resp=="si":
#        peliculas.clear()
# input("\n\t\t ::: la operacion se realizo con exito ::: ")
   
def agregarpeliculas():
    borrarpantalla()
    print("\n\t :: Agregar una nueva película :: \n")
    

    print("\n\t::: ¡Película agregada exitosamente! :::")

def agregarcaracteristicaspeliculas():
     borrarpantalla()
     print("\n\t.:: Agregar caracteristicas a peliculas ::. \n")
     atributo=input("Ingresa la nueva caracteriztica de la pelicula: ").lower().strip()
     valor=input("Ingresa el valor de la caracteriztica de la pelicula: ").lower().strip()
     # pelicula.update({atributo:valor})
     peliculas[atributo]=valor
     print("\n\t\t ::: !LA OPERACION SE REALIZO CON EXITO! :::")

def modificarCaracteristicaPeliculas():
    borrarpantalla()
    print("\n\t:: Modificar Características a Películas ::\n")
    if len(peliculas) > 0:
        print("\n\tValor actuales:\n")
        for i in peliculas:
            print(f"\t({i}): {peliculas[i]}")
            resp = input(f"\t¿Deseas cambiar el valor de {i}? (Sí/No): ")
            if resp == "si":
                peliculas.update({f"{i}": input(f"\u0001F501 El nuevo valor: ").upper().strip()})
                print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
                esperartecla()
                borrarpantalla()
    else:
        print("\t::: No hay películas en el sistema :::")
        esperartecla()

def borrarcaracteristicaspeliculas():
    borrarpantalla()
    print("\n\t.:: Borrar características de películas ::.\n")
    if len(peliculas) == 0:
        print("\n\t.:: No hay películas en el sistema ::.")
        input("\n\tPresiona Enter para continuar...")
        return
    opcion = input("\t¿Deseas borrar una característica de la película? (SI/NO): ").lower().strip()
    if opcion == "SI":
        BCP= input("\n\tque característica deseas eliminar o quitar: ").lower().strip()

        if BCP in peliculas:
            resp = input(f"\n\t¿Estás seguro de que deseas eliminar esta característica '{BCP}'? (SI/NO): ").lower().strip()
            if resp == "SI":
                del peliculas[BCP]
                print("\n\t\t::: ¡OPERACIÓN EXITOSA! característica eliminada. :::")
            else:
                print("\n\t\t::: Operación cancelada por el usuario. :::")
        else:
            print(f"\n\t.:: La característica '{BCP}' no fue encontrada en la película. ::.")
    else:
        print("\n\t.:: Operación cancelada. ::.")
    input("\n\tPresiona enter para continuar...")

    

def borrarpeliculas():
    borrarpantalla()
    print("\n\t :: Borrar todas las películas :: \n")
    resp = input("¿Deseas borrar todas las películas del sistema? (Si/No): ").strip().lower()
    if resp == "si":
        peliculas.clear()
        print("\n\t::: ¡Películas eliminadas con éxito! :::")
    else:
        print("\n\t::: Operación cancelada :::")


#def vaciarpeliculas():
   # borrarpantalla()
   # print("\n\t :: vaciar o quitar todas las peliculas ::. \n")
    #resp=input("¿desas quitar todas las peliculas del sistema (si/no) ").lower().strip()
    #if resp=="si":
       # peliculas.clear()
        #input("n\t\t:::¡la operacion se realizo con exito¡:::")

#def buscarpeliculas():
  # borrarpantalla()
   #print("\n\t.:: buscar peliculas ::. \n")
   #pelicula_buscar=input("ingrese el nombre de la pelicula a buscar: ").upper().strip()
   #encontro=0
   #if not (pelicula_buscar in peliculas):
    #  print("\n\t\t 'no se encontro la pelicula")
   #else:
    #  for i in range(0,len(peliculas)):
     #    if pelicula_buscar==peliculas[i]:
      #      print(f"\nla pelicula {pelicula_buscar} si la tenemos y esta en la casilla {i+1}")
       #     encontro+=1
        #    print(f"\ntenemos {encontro} pelicula(s) con este titulo")
        # print("n\t\t:::¡la operacion se realizo con exito¡:::")

#def eliminarpeliculas():
# borrarpantalla()
 #print("\n\t.:: borrar peliculas ::. \n")
#pelicula_buscar=input("ingrese el nombre de la pelicula a borrar: ").upper().strip()
#encontro=0
#if not (pelicula_buscar in peliculas):
    #  print("\n\t\t 'no se encontro la pelicula")
#else:
 #    resp="si"
  #   while pelicula_buscar in peliculas and resp=="si":
   #     resp=input("¿desas borrar la pelicula del sistema (si/no)")
    #    if resp=="si":
     #     peliculas.remove(pelicula_buscar)
      #  encontro+=1
       # print("n\t\t:::¡la operacion se realizo con exito¡:::")

        #print(f"\n\tse borro {encontro} pelicula(s) con este titulo")