## ---------------------------------
## ---- Ejercicio 1 ----
## ---------------------------------

## Impresión en consola 

print('Hola mundo') 

# --- Datos primitivos ---

# 1 Sting

texto = 'Campus'
print(texto)
print(type(texto))

# 2 Int

numeroEntero = 1
print(numeroEntero) 

# 3 Float 

numeroDecimal = 4.5
print(numeroDecimal) 

# 4 Double

numeroDecimalLargo = 3.1456555455
print(numeroDecimalLargo)

# 5 Boolean

booleano = True
print(booleano)

# --- Entrada parte del usuario 

entradaUsuarioNombre = input('Ingresa tu nombre ')
print('Tu nombre es ', entradaUsuarioNombre)

# --- Entrada parte del usuario con definicion de tipo de dato primitivo ---

entradaNumero = input('Ingresa tu edad ')
numeroFinal = int(entradaNumero)
print('Tu edad es ', numeroFinal)

# --- Ciclos ---

# Ciclo for

for i in range(5,10,2): #for contador in range(desde,hasta,pasos):
    print(i)
    
# Ciclo while 

booleanito = True
while booleanito == True: #while condicion_a_cumplir:
    print('sigo vivo')
    booleanito = False

# ---- Condicionales ----

texto1 = 'campus'
if texto1 == 'campus':
    print('Soy campus')
else:
    print('No soy campus') 
    
# --- Funciones ---

# Sin parametros y sin retorno 

def saludar():
    print('Hola mundo')
saludar()

# Con parametros y sin retorno 

def saludar(nombre):
    print(f'Hola {nombre}, como estas?')
saludar('Deivid') 

# Con parametros y con retorno 

def suma(a, b):
    resultado = a + b
    return resultado
valor1 = int(input('num1 '))
valor2 = int(input('num2 '))
resultado_suma = suma(valor1, valor2)
print(f"La suma de {valor1} y {valor2} es: {resultado_suma}")

#Sin parametros y con retorno 

def obtener_mensaje():
    mensaje = "¡Hola, mundo!"
    return mensaje

# Ejemplo de uso de la función

saludo = obtener_mensaje()
print(saludo)

# ---- Arreglos ----

numeros = [1, 2, 3, 4, 5]
print("Secuencia inicial :", numeros)
numeros[2] = 13
print("secuencia modificada :", numeros)
numeros.append(6)
print("agregando nuevo numero :", numeros)
longitud = len(numeros)
print("Longitud :", longitud)
print("Digitos :")
for numero in numeros:
    print(numero)
    
## Desarrollado por DEIVID VELASQUEZ GUTIERREZ - 1096701633
