def model(t,y0,v0,a):
    return y0+v0*t+0.5*a*t**2
for i in [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]:
    print(model(i, 10, 25, -9.81))
    