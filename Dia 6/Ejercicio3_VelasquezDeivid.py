## -----------------------
## ---- Ejercicio 3 ----
## -----------------------

## Mutable: Puede ser modificado después.

## (1) Listas

lista = [1, 2, 3, 4, 5]
print('Primer elemento:', lista[0])
print('Longitud de la lista:', len(lista))
lista.append(6)
lista.remove(4)
print('Lista después de modificaciones:', lista)

## (2) Diccionarios

diccionario={'Nombre: ': 'Deivid','Edad: ': '16', 'Ciudad: ':('Bucaramanga', 'Piedecuesta')}
print(diccionario)
print(diccionario['Nombre: '])
print(diccionario['Ciudad: '][0])

## Inmutable: No puede ser modificado después.

## (1)Cadenas

cadena = 'HoLa MunDo '
rta = cadena.lower()
print(rta)
rta2 = cadena.upper()
print(rta2)
rta3 = cadena.capitalize()
print(rta3)

## (2)Tuplas

tuple = ('Manzana', 'Pera', 'Banana', 'Mango')
print(tuple[2])
print(tuple[3])
print(tuple[0])
print(tuple[1])


## Desarrollado por DEIVID VELASQUEZ GUTIERREZ - 1096701633
