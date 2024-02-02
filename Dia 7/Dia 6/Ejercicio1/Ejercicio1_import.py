## -----------------------
## ---- Ejercicio 1 ----
## -----------------------


#REALIZAR UN PROGRAMA QUE USE UN DICCIONARIO PARA GESTIONAR LOS PRODUCTOS
#Y PRECIOS DE LA TABLA, DONDE SE LE PREGUNTE AL USUARIO POR UN PRODUCTO
#Y LA CANTIDAD. AL FINALIZAR MOSTRAR EN LA CONSOLA EL PRECIO TOTAL. SI
#EL PRODUCTO NO ESTA DEBE MOSTRAR UN MENSAJE INFORMANDO SOBRE ELLO
import ModuloEj1
print('Bienvenido a mi tienda virtual')
print('Tendras un listado con los productos disponibles')
productos = {"Productos": ('pan', 'leche', 'cafe','huevos'), "valor": (2000, 4500, 1500, 600)}
print(productos)
print(ModuloEj1.proceso(productos))


## Desarrollado por DEIVID VELASQUEZ GUTIERREZ - 1096701633