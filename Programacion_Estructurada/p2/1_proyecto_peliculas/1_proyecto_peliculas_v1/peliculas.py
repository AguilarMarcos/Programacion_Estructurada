peliculas=[]

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    print("\n\t\tOprima cualquier tecla para continuar...")
    input() 

def agregarPeliculas():
    borrarPantalla()
    print("\n\t.:: Agregar Peliculas ::.")
    peliculas.append(input("Ingresa el nombre: ").upper().strip())
    input("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def consultarPeliculas():
    borrarPantalla()
    print("\n\t.:: Consultar o Mostrar las Peliculas ::. ")
    if len(peliculas)>0:
      for i in range(0,len(peliculas)):
        print(f"\t{i+1}: {peliculas[i]}")
    else:
       print("\n\t .:: No hay peliculas en el sistema en este momento ::.\n")

def vaciarPelicula():
   borrarPantalla()
   print("\n\t.:: Vaciar quitar Todas las Peliculas ::. ")
   resp=input("¿Deseas quietar TODAS las Peliculas del sitema? (Si/No)").lower().strip()
   
   if resp=="si":
      peliculas.clear()
      print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def buscarPeliculas():
   borrarPantalla()
   print("n\t.:: Buscar Peliculas ::. \n")
   pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
   encontro=0
   if not(pelicula_buscar in peliculas):
      print("\n\t\t ¡No se encuentra la pelicula!")
   else:
      for i  in range(0,len(peliculas)):
         if pelicula_buscar==peliculas[i]:
            print(f"\nLa pelicula {pelicula_buscar} si la tenemos y esta en la casilla: {i+1}")
            encontro+1
      print(f"\nTenemos {encontro} peliculas(s) con este titulo") 
      print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def eliminarPeliculas():
   borrarPantalla()
   print("n\t.:: Borrar Peliculas ::. \n")
   pelicula_buscar=input("Ingrese el nombre de la pelicula a borrar: ").upper().strip()
   encontro=0
   if not(pelicula_buscar in peliculas):
      print("\n\t\t ¡No se encuentra la pelicula!")
   else:
      resp="si"
      while pelicula_buscar in peliculas in peliculas and resp=="si":
         resp=input("¿Deseas borrar la pelicula del sistema? (Si/No) ")
         if resp=="si":
            posicion=peliculas.index(pelicula_buscar)
            print(f"\nLa pelicula que se borro es: {pelicula_buscar} y estaba en la casilla: {posicion+1}")
            peliculas.remove(pelicula_buscar) 
            encontro+1
            print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")
      print(f"\n\t\tSe borro {encontro} pelicula(s) con este titulo")