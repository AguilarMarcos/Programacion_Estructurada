from paquete1 import modulos
import os

print(modulos.saludar("Daniel Contreras Ruano"))

modulos.borrarPantalla()
nom, tel=modulos.solicitarDatos2()
print(f"\n\t:: Agenda Telefónica ::\n\t\tNombre: {nom}\n\t\tTeléfono: {tel}")
