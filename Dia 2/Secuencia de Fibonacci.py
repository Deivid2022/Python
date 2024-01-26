## ---------------------
## ---- Ejercicio 1 ----
## ---------------------
def fibonacci(n):
    secuencia  = [0, 1]

    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])

    return secuencia

def main():
    
    while True:
        try:
            # Solicitar al usuario ingresar un valor entero
            n = int(input("Ingrese hasta la posición que quieres observar la secuencia : "))

            if n < 0:
                print('Por favor, ingrese un número entero.')
                continue
            resultado = fibonacci(n)
            print(f'La Secuencia de Fibonacci hasta la posición {n} es: {resultado}')
        except ValueError:
            print('Por favor, ingrese un número entero.')
            continue
        decision = input('¿Desea continuar generando la secuencia de Fibonacci? (si/no): ').lower()
        if decision == 'no':
            decision2 = input('Coloca el 0 para salir del programa ')
            print("¡Hasta luego! Gracias por usar el sofware.")
            break
print('Bienvenido usuario a la Secuencia de Fibonacci.')
print('')
print('''    La Secuencia de Fibonacci es una operación matematica que 
    comienza con 0 y 1, y cada término subsiguiente es la suma 
    de los dos anteriores y asi hasta donde el usuario quiera.''')
print('')
if  __name__ == '__main__':
    main()
    
## Desarrollado por DEIVID VELASQUEZ GUTIERREZ - 1096701633
