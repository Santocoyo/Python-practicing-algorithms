def saludo(lang):
    if lang == "es":
        return("hola")
    elif lang == "fr":
        return("bonjour")
    else:
        return("hello")
print(saludo("en"), "Jake")
print(saludo("es"), "José")
print(saludo("fr"), "Jean")

def add(a, b):
    add=a+b
    return add
print(add(3,5))

def model(t, y0, v0, a):
    return y0+v0*t+0.5*a*t**2
y0=10
t=3
v0=20
a=-9.8
print(model(t,y0,v0,a))