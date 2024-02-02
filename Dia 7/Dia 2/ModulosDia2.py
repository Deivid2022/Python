def fibonacci(n):
    if n < 2:
        return n
    else: 
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    
    while True:
        try:
            n = int(input("Ingrese hasta la posición que quieres observar la secuencia(Puedes ingresar el 0 si deseas salir) : "))

            if n < 0:
                print('')
                print('Por favor, ingrese un número entero.')
                continue
            if n == 0:
                print('')
                print('¡Hasta luego! Gracias por usar el software')
                print('')
                break
            print('')
            for x in range (n):
                print (f'#',x+1,': ',fibonacci(x))
            print('')
        except ValueError:
            print('')
            print('Por favor, ingrese un número entero.')
            continue
        decision = input('¿Desea continuar generando la secuencia de Fibonacci? (si/no): ').lower()
        print('')
        if decision == 'no':
            print("¡Hasta luego! Gracias por usar el software.")
            print('')
            break
        
        
