## ----------------------------
## ----Ejercicio 2 ----
## ----------------------------
import random
import ModulosDia2Ej2
# Bienvenida del usuario
nombre = input('Ingresa tu nombre ')
print('')
print(f'¡Bienvenido {nombre}!, al juego de adivinar el número')
print('Voy a pensar en un número del 1 al 100')
print('Vas a tener 10 intentos para poder adivinar el número que estoy pensando')
print('')
secreto = random.randint(1,100) 
print(ModulosDia2Ej2.proceso(secreto))
         
## Desarrollado por DEIVID VELASQUEZ GUTIERREZ - 1096701633