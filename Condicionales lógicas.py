x=input("Digite un número: ")
x=int(x)
if x%2 != 0:
    print("Extraño")
else:
    if 2<=x<=5:
            print("No es extraño")
    elif 6<=x<=20:
        print("Extraño")
    elif x>20:
        print("No es extraño")