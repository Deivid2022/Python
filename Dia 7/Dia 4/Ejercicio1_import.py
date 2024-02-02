## -------------------------
## ---- Ejercicio 1 ----
## -------------------------

import ModuloDia4

T = int(input(''))
for case in range(T):
    n,k = list(map(int, input().split()))
    T_n = list(map(int,input().split()))
rta = ModuloDia4.pares(T_n,n,k)
print('case{}:{}'.format(case+1,rta))

## Desarrollado por DEIVID VELASQUEZ GUTIERREZ - 1096701633