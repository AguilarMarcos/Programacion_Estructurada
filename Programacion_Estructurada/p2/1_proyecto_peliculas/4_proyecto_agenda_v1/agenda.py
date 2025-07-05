
# agenda=[
#   ["carlos","6181234567"],
#   ["alberto","6671234567"],
#   ["martin","6785678923"]
#   ]


def borrarPantalla():
  import os 
  os.system("cls")

def esperarTecla():
    input("Oprima cualquier tecla para continuar")  

def menu_principal():
   print(".:: Sistema de Gestión de agenda de contactos::.. \n1.-  Agregar contacto  \n2.- Mostrar los contactos \n3.- Buscar contacto \n4.- Modifcar contacto \n5.- Eliminar contacto \n6.- SALIR ")
   opcion=input("Elige una opción (1-4): ") 
   return opcion   

def Agregar_contactos(datos):
   borrarPantalla()
   print("Agregar Contactos")
   nombre = input("nombre").upper().strip()
   if nombre in datos:
      print("contacto existente")
   else:
    tel=input("Telefono").strip()
    email=input("Email").upper().strip()
    datos[nombre]=[tel,email]
    print("Accion Realizada Con Exito")
    
def Mostrar_Contactos(datos):
   borrarPantalla()
   print("Mostrar Contactos")
   if not datos:
      print("No Se Encuentra el contacto")
   else:
      print(f"{"nombre":<15}{"telefono":<15}{"email":<15}")
      print(f"-"*60)
      for nombre,datos in datos.items():
         print(f"{nombre:<15}{datos[0]:<15}{datos[1]:<15}")
         print(f"-"*60)

def Buscar_Contactos(datos):
   borrarPantalla()
   print("Buscar Contacto")
   if not datos:
          print("No Existe El Contacto")
   else:
    nombre=input("nombre: ").upper().strip()
   if nombre in datos:
       print(f"{"nombre":<15}{"telefono":<15}{"email":<15}")
       print(f"-"*60)
       print(f"{nombre:<15}{datos[nombre][0]:<15}{datos[nombre][1]:<15}")
       print(f"-"*60)
   else:
       print("No Existe el Contacto")

def Modificar_Contactos(datos):
       borrarPantalla()
       print("Modificar Contacto")
       if not datos:
             print("No Existe El Contacto")
       else:
             nombre=input("Nombre: ").upper().strip()
             if nombre in datos:
              print(f"{"nombre":<15}{"telefono":<15}{"email":<15}")
              print(f"-"*60)
              print(f"{nombre:<15}{datos[nombre][0]:<15}{datos[nombre][1]:<15}")
              print(f"-"*60)
              resp=input(f"Deseas modificar el contacto? (SI/No)").lower().strip()
              if resp=="si":
               tel=input("telefono").strip()
               email=input("email").upper().strip()
               datos[nombre]=[tel,email]
               print("Accion Realizada Con Exito")
             else:
              print("No Existe El Contacto")

def Eliminar_Contacto(datos):
   borrarPantalla()
   print("Eliminar Contacto")
   if not datos:
      print("No Hay Contactos En La Agenda")
   else:
      nombre=input("nombre del contacto a eliminar: ").upper().strip()
      if nombre in datos:
              print(f"{"nombre":<15}{"telefono":<15}{"email":<15}")
              print(f"-"*60)
              print(f"{nombre:<15}{datos[nombre][0]:<15}{datos[nombre][1]:<15}")
              print(f"-"*60)
              resp=input("Deseas Borrar Los Valores (SI/NO): ").lower().strip()
              if resp=="si":
                  datos.pop(nombre)
                  print("Accion Realizada Con Exito")
              else:
                   print("Este Contacto No Existe")
