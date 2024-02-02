def pares(T_n,n,k):
    ## set(crear lista)
    pairs=set() 
    for i in range(n):
        for j in range(i+1,n):
            if(T_n[i]+T_n[j]) % k == 0:
                ## min(organiza los pares de menos a mayor),max(de mayor a menor)
                pairs.add((min(T_n[i],T_n[j]),max(T_n[i],T_n[j]))) 
        # len(retorna la cantidad de pares que son divisibles por k)
    return len(pairs) 
