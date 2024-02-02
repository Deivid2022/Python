## -------------------------
## ---- Ejercicio 1 ----
## -------------------------


import ModuloDia3

cantidad = int(input(''))

if cantidad>= 1 and cantidad<=1000:
    # Definición del resultado de las variables de la función 
    monedas_10, monedas_5, monedas_1 = ModuloDia3.proceso(cantidad)
    print( monedas_10 + monedas_5 + monedas_1)
else: 
    print('exceeds the software limit')
    cantidad = False

## Desarrollado por DEIVID VELASQUEZ GUTIERREZ - 1096701633