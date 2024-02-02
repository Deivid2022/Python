def ball_collide(bola1, bola2):
    import math
    x1, y1, r1 = bola1
    x2, y2, r2 = bola2 
    
    comparacion = math.sqrt((x1-x2)**2+(y1-y2)**2)
    suma = r1 + r2
    return (suma >= comparacion)