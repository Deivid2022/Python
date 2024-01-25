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
## Desarrollado por DEIVID VELASQUEZ GUTIERREZ - 1096701633