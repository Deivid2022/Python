## -------------------------
## ---- Ejercicio 1 ----
## -------------------------


def proceso(cantidad):
    # Se ejecuta la divición de la cantidad con el número definido con // y se optiene la cantidad que tiene de cada moneda
    # El residuo de la operación anterior se optiene con % y se vuelve a hacer con el siguiente número 
    # Asi hasta que no alla residuo en la divición, opteniendo la cantidad de cada moneda 
    return cantidad // 10, (cantidad % 10) // 5, (cantidad % 10) % 5
# ---------- Variable 1 ----- Variable 2 --------- Variable 3 ------

cantidad = int(input(''))

if cantidad>= 1 and cantidad<=1000:
    # Definición del resultado de las variables de la función 
    monedas_10, monedas_5, monedas_1 = proceso(cantidad)
    print( monedas_10 + monedas_5 + monedas_1)
    print(monedas_10 + monedas_5 + monedas_1, '= ',monedas_10,'+',monedas_5,'+',monedas_1)
else: 
    print('exceeds the software limit')
    cantidad = False

## Desarrollado por DEIVID VELASQUEZ GUTIERREZ - 1096701633