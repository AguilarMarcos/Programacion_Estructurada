#ejemplo 1 crear una lista de numeros e imprimir el contenido
import os
os.system("cls")

numeros=[520,650,350]

#1er forma
print(numeros)

#2ed forma
for i in numeros:
    print(i)

#3er forma
for i in range(0,len(numeros)):
  print(numeros[i])

#ejemplo 2 crear una lista de palabras y posteriormente buscar la coincidencia de una palabra
os.system("cls")

palabras=("casa","carro","porche","ram","moto")

palabra_buscar=input("dame la palabra a buscar")

#1er forma
if palabra_buscar in palabras:
   print("se encontro la palabra")
else:
   print("no encuentro la palabra")

#2da forma
encontro=False
for i in palabras:
   if i==palabra_buscar:
        encontro=True

if encontro:
      print("se encontro la palabra")
else:
   print("no encuentro la palabra")

#3er forma
encontro=False
for i in range(0,len(numeros)):
   if palabras[i]==palabra_buscar:
        encontro=True

if encontro:
      print("se encontro la palabra")
else:
   print("no encuentro la palabra")

#ejemplo 3 añadir elemntos a una lista

opc="si"

while opc=="si":
    numero=float(input("dame un numero entero o decimal"))
    numeros.append(numero)
    opc=input("¿eseas utilizar otro numero (si/no)").lower()

print(numeros)

#ejemplo 4 crear una lista multidimensional (matriz) que almacene el nombre y telefono de 4 personas

agenda=[
  ["carlos","6181234567"],
  ["alberto","6671234567"],
  ["martin","6785678923"]
  ]

print(agenda)

for r in agenda:
 print(r)

for r in range(0,3):
 for c in range(0,2):
  print(agenda[r][c])

#["carlos","6181234567"],
#["alberto","6671234567"],
#["martin","6785678923"]
  
valores=""
for r in range(0,3):
     for c in range(0,2):
       valores+=f"[(agenda[r][c])]"
     valores=f"\n"
     print(valores)  
