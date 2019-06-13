"""
fruta="Mi nombre es Alejandro Santoscoy Rivero"
indice=0
while indice<len(fruta):
    letra=fruta[indice]
    print(indice, letra)
    indice=indice+1
for i in range(len(fruta)):
    letra=fruta[i]
    print(i, letra)
for letra in fruta:
    print(letra)
    """
x=input("ingrese una palabra: ")
contador=0
for letra in x:
    if letra=="a" or letra=="A":
        contador=contador+1
print("Hay ", contador, " letras A o a")