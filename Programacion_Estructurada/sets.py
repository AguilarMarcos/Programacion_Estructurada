"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
import os
os.system("clear")

#paises={"Mexico","Brasil","España","Canada"}
#print(paises)

#Funciones u operaciones 
#for i in paises:
 #   print(i)

#paises.add("México")
#print(paises)

#paises.pop()
#print(paises)

#paises.remove("México")
#print(paises)

#ejemplo crear un programa que solicite los email de los alumnos de la utd, almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados
email=[]
resp="si"

while resp=="si":
      email.append(input("ingrese correo institucional: " ))
      resp=input("deseas ingresar otro correo?").lower()

email_set=set(email)
email=list(email_set)
print(email)








  



