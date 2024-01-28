## ---------------------
## ---- Ejercicio 1 ----
## ---------------------
# Generador de la secuencia de Fibonacci
def fibonacci(n):
    if n < 2:
        return n
    else: 
        return fibonacci(n-1) + fibonacci(n-2)
# Proceso en el que se va a definir el tamaño de la secuencia y si quieres salir o seguir
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
# Bienvenida y Dato cusioso sobre la secuencia de Fibonacci 
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
# Desarrollo de la función
main() 
    
## Desarrollado por DEIVID VELASQUEZ GUTIERREZ - 1096701633
