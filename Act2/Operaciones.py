import numpy as np

arreglo1 = np.array ([2, 4, 6, 8, 10]) 
arreglo3 = np.array ([1, 3, 5, 9, 11])

arreglo2 = np.ones((4,4))

for x in arreglo1:
    print(x)

print("Valor mayor: ", np.max(arreglo1))
print("Valor menor: ", np.min(arreglo1))

media = np.mean(arreglo1)
posmax = np.argmax(arreglo1)
posmin = np.argmin(arreglo1)

print("Media = ", media)
print("Media = ", posmax) #posicion
print("Media = ", posmin) #posicion 

arreglo6 = np.sum(arreglo1 * arreglo3)
print("Suma Arreglos = ", arreglo6)

#for x in arreglo2:
 #   print(x)