""" 
crear un programa que calcule e imprima las tablas de multiplicar del 2

restricciones
1-sin estructuras e control
2-sin funciones
"""


#version 1
multi=2*1
print(f"2*1 = {multi}")
multi=2*2
print(f"2*2 = {multi}")
multi=2*3
print(f"2*3 = {multi}")
multi=2*4
print(f"2*4 = {multi}")
multi=2*5
print(f"2*5 = {multi}")
multi=2*6
print(f"2*6 = {multi}")
multi=2*7
print(f"2*7 = {multi}")
multi=2*8
print(f"2*8 = {multi}")
multi=2*9
print(f"2*9 = {multi}")
multi=2*10
print(f"2*10 = {multi}")


#version 2
""" 
crear un programa que calcule e imprima las tablas de multiplicar del 2

restricciones
1-con estructuras e control
2-sin funciones
"""

num=int(input("inserta el numero de la tabla de multiplicar"))
for i in range(1,11):
 multi=num*i
 print(f"{num} x {i} = {multi}")


 #version 3
 """ 
crear un programa que calcule e imprima las tablas de multiplicar del 2

restricciones
1-con estructuras e control
2-con funciones
"""
# Función que imprime la tabla de multiplicar de un número dado
def imprimir_tabla(numero):
    print(f"Tabla de multiplicar del {numero}")
    for i in range(1, 11):  # Estructura de control: bucle for
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Llamada a la función con el número 2
imprimir_tabla(2)

