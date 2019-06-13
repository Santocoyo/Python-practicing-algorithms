lista=list()
while x != "done":
    x=input("Digite un número: ")
    if x=="done":
        break
    x=int(x)
    lista.append(x)
promedio=lista.sum()/lista.len()
print(promedio)