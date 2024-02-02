def proceso(cantidad):
    # Se ejecuta la divición de la cantidad con el número definido con // y se optiene la cantidad que tiene de cada moneda
    # El residuo de la operación anterior se optiene con % y se vuelve a hacer con el siguiente número 
    # Asi hasta que no alla residuo en la divición, opteniendo la cantidad de cada moneda 
    return cantidad // 10, (cantidad % 10) // 5, (cantidad % 10) % 5
# ---------- Variable 1 ----- Variable 2 --------- Variable 3 ------