## ---------------------
## ---- Ejercicio 1 ----
## ---------------------
def fibonacci(n):
    if n < 2:
        return n
    else: 
        return fibonacci(n-1) + fibonacci(n-2)
    
def main():
    
    while True:
        try:
            n = int(input("Ingrese hasta la posición que quieres observar la secuencia : "))

            if n < 0:
                print('')
                print('Por favor, ingrese un número entero.')
                continue
            print('')
            for x in range (n):
                print(fibonacci(x))
        except ValueError:
            print('')
            print('Por favor, ingrese un número entero.')
            continue
        
        print('')
        print('Coloca cualquier número diferente al 0 si quieres seguir')
        print('')
        decision2 = int(input('Coloca el 0 para salir del programa '))
        print('')
        if decision2 == 0:
            decision2 = 0
            print('')
            print('¡Hasta luego! Gracias por usar el sofware.')
            print('')
            break
        decision = input('¿Desea continuar generando la secuencia de Fibonacci? (si/no): ').lower()
        print('')
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
print('Dato curioso:')
print('')
print('''    La sucesión de Fibonacci puede verse en múltiples elementos 
    de la naturaleza. Uno de los ejemplos más claros se observa en la 
    concha de un nautilus, un tipo de molusco cefalópodo marino que dio 
    nombre al submarino más importante de la literatura universal en 
    «Veinte mil leguas de viaje submarino» de Julio Verne.''')
print('')
if  __name__ == '__main__':
    main()
    
## Desarrollado por DEIVID VELASQUEZ GUTIERREZ - 1096701633
