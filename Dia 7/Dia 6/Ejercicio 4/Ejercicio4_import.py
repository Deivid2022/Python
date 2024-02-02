## -----------------------
## ---- Ejercicio 4 ----
## -----------------------

import ModuloEj4
    
# casos de prueba
## bola1 = (3, 4, 4)
## bola2 = (6, 8, 3)
bola1 = map(int,input('Ingresa x, y, z de la bola 1: ').split())
bola2 = map(int,input('Ingresa x, y, z de la bola 2: ').split())
print(ModuloEj4.ball_collide(bola1, bola2))


## Desarrollado por DEIVID VELASQUEZ GUTIERREZ - 1096701633