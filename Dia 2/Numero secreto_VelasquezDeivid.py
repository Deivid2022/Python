## ----------------------------
## ----Ejercicio 2 ----
## ----------------------------
import random
# Bienvenida del usuario
nombre = input('Ingresa tu nombre ')
print('')
print(f'¡Bienvenido {nombre}!, al juego de adivinar el número')
print('Voy a pensar en un número del 1 al 100')
print('Vas a tener 10 intentos para poder adivinar el número que estoy pensando')
print('')
# Generador del numero random 
secreto = random.randint(1,100) 
# Conteo de intentos e ingreso de número 
numIntentos = 0
while numIntentos < 10:
    try:
        num = int(input('Ingresa un número '))
        print('')
    except ValueError:
        print('')
        print('Por favor, ingresa un número entero')
        print('')
        continue
    numIntentos += 1
    # Pistas y terminacion del juego 
    if num == secreto:
        print(f'¡Felicitaciones!, el número {num} es justo el que estaba pensando, lo pudiste hacer en {numIntentos} intentos')
        print('')
        print('¡Hasta luego! Gracias por usar mi sofware.')
        print('')
        break
    elif num < secreto:
        print(f'El número {num} es menor al que estoy pensando, llevas {numIntentos} intentos')
        print('')
    else:
        print(f'El número {num} es mayor al que estoy pensando, llevas {numIntentos} intentos')
        print('')
        
    if numIntentos == 10:
        print(f'Te quedaste sin oportunidades, la proxima lo hacer mejor :)')
        print('')
        print('¡Hasta luego! Gracias por usar mi sofware.')
        print('')

         
## Desarrollado por DEIVID VELASQUEZ GUTIERREZ - 1096701633