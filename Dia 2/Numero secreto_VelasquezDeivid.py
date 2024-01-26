## ----------------------------
## ----Ejercicio 2 ----
## ----------------------------
import random
def juego():
    nombre = input('Ingresa tu nombre ')
    print(f'¡Bienvenido {nombre}!, al juego de adivinar el número')
    print('Voy a pensar en un número del 1 al 100')
    print('Vas a tener 10 intentos para poder adivinar el número que estoy pensando')

    secreto = random.randint(1,100) 
    numIntentos = 0
    
    while numIntentos < 10:
        try:
            num = int(input('Ingresa un número '))
        except ValueError:
            print('Por favor, ingresa un número entero')
            continue
        numIntentos += 1
        
        if num == secreto:
            print(f'¡Felicitaciones!, el número {num} es justo el que estaba pensando, lo pudiste hacer en {numIntentos} intentos')
            print("¡Hasta luego! Gracias por usar mi sofware.")
            break
        elif num < secreto:
            print(f'El número es mayor al que estoy pensando, llevas {numIntentos} intentos')
        else:
            print(f'El número es menor al que estoy pensando, llevas {numIntentos} intentos')
        
    if numIntentos == 10:
        print(f'Te quedaste sin oportunidades, la proxima lo hacer mejor :)')
        print("¡Hasta luego! Gracias por usar mi sofware.")
if __name__ == '__main__':
    juego()
         
## Desarrollado por DEIVID VELASQUEZ GUTIERREZ - 1096701633