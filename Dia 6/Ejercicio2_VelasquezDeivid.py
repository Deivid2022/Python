## -----------------------
## ---- Ejercicio 2 ----
## -----------------------

def negate(num):
    return -num

def large_num(num):
    return (num > 10000) ## No se deberia colocar en una variable, solo retornarla.

## Debe pedir un número para definir la variable b.
b = int(input(''))
neg_b = negate(b) ## remplazar num con negate(b) para que pueda dar el proceso de la función.
print('b: ', b, ' neg_b: ', neg_b) ## Debe tener parentesis para ejecutar correctamente.

big = large_num(b)
print('b is big: ', big ) ## Debe tener parentesis para ejecutar correctamente.

## Desarrollado por DEIVID VELASQUEZ GUTIERREZ - 1096701633