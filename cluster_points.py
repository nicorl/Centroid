import math
import numpy as np
muestra = [[1,10],[1,15],[20,20],[20,25],[30,80],[4,18],[3,18],[2,18],[30,30],[80,80],[30,75],[85,85],[85,85]]
#print(muestra)
limite = 10
lista_trues = []

def distancia(punto_a, punto_b):
    dist = int(math.sqrt( (punto_b[0] - punto_a[0])**2 + (punto_b[1] - punto_a[1])**2 ))
    return dist

def comprobar_limite(dist, i, j):
    if dist < limite:
        lista_trues.append(j)
    else:
        pass

    return lista_trues

def calcula_distancias(array):
    distancias = []
    array_dists = []
    for i in range(0,len(array)):
        del distancias[:]
        for j in range(0,len(array)):
            distancias.append(distancia(array[i], array[j]))
        array_dists.append(np.array(distancias))
    return(array_dists)

########################################################################
distancias = calcula_distancias(muestra)

lista_trues_final = []
la_ultima = []
for i in range(0,len(distancias)):
    del lista_trues_final[:]
    for j in range(0,len(distancias)):
            lista_trues_final = comprobar_limite(distancias[i][j], i, j)
    la_ultima.append(np.array(lista_trues_final))


la_real = []
for i in range(0,len(la_ultima)):
    la_real.append(la_ultima[i][0])
print(la_real)

# La_real contiene los indices que se deben coger para hacer un promedio de valores de muestra
