for i in [5,4,3,2,1]:
    print (i)
print("Despegue!")

friends = ["Andrea", "Saul", "Catzin"]
for friend in friends:
    print("FELIZ AÑO NUEVO, ", friend, "!")
print("Done!")
"""
for i in range(1,50,2):
    print(i)
"""
maxim=0
contador=0
suma=0
for i in [9,41,12,3,74,15]:
    if i>maxim:
        maxim=i
    contador=contador+1
    suma=suma+i
print(maxim)
print(contador)
print("promedio: ", suma/contador)
