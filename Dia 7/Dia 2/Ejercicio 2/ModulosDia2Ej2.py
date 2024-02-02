def proceso(secreto): 
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
            break