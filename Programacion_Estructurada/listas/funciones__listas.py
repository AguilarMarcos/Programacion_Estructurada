"""
List (array)
son cooleciones o conjunto de datos/valores bajo un mismos nombre, 
para acceder a los valores se hace con un indice numerico

Nota:sus valores si son modificables

La lista es una coleccion ordenada y modificable permite miembros 
duplicados

"""

import os
os.system("clear")

#funciones mas comunes en las listas

paises=["Mexico","brasil","españa","canada"]

numeros=[23,121,100,34]

varios=["Hola",True,33,3,12]

#ordenar las listas

print(numeros)
print(paises)
print(varios)

numeros.sort()
print(numeros)
paises.sort()
print(paises)

#agrerar,insertar,añadir un elemento a la lista
#1er forma
print(paises)
paises.append("honduras")
print(paises)

#2da forma
paises.insert(1,"honduras")
print(paises)

#eliminar,borrar,suprimir, un elemento a la lista
#1er forma
paises.sort()
print(paises)
paises.pop(4)
print(paises)

#2a forma
paises.remove("honduras")
print(paises)

#buscar un elemento dentro de la lista
#paises=["Mexico","brasil","españa","canada"]

print("brasil" in paises)

#contar el numero de veces que un elemento esta dentro de una lista
#numeros=[23,121,100,34]
print(numeros)
print(numeros.count(12))
numeros.insert(1,12)
print(numeros)
print(numeros.count(12))

#dar la vuelta a los elementos de una lista
print(paises)
print(numeros)
paises.reverse()
numeros.reverse()
print(numeros)
print(paises)

#conocer el indice o la posicion de un valor de la lista
posicion=paises.index("españa")

#unir el contenido de dos o mas listas en una
#numeros=(100,34,23,12,12)
numeros2=(300,500,100)

print(numeros)
print(numeros2)
numeros.extend(numeros2)
print(numeros)

paises.extend(numeros2)
print(paises)

