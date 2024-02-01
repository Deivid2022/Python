## -----------------------
## ---- Ejercicio 4 ----
## -----------------------
import math
def ball_collide(bola1, bola2):
    
    x1, y1, r1 = bola1
    x2, y2, r2 = bola2 
    
    comparacion = math.sqrt((x1-x2)**2+(y1-y2)**2)
    suma = r1 + r2
    return (suma >= comparacion)
    
# casos de prueba
## bola1 = (3, 4, 4)
## bola2 = (6, 8, 3)
bola1 = map(int,input().split())
bola2 = map(int,input().split())
print(ball_collide(bola1, bola2))


## Desarrollado por DEIVID VELASQUEZ GUTIERREZ - 1096701633