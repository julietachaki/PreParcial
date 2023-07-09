from math import sqrt
def FuncionProyectil(x,y):
    g=9.8
    y1=0
    t= sqrt(2*(y-y1)/(g))
    x1=0
    v1x=(x-x1)/t
    return v1x

def FuncionCaida(v,obj):
    g=9.8
    if obj== 2:
        h=(7*v**2)/(10*g)
        return h
    elif obj ==1:
        h= v**2/(2*g)
        return h 
print("1) Bloque\n2)Canica")
cuerpo=int(input("Ingrese el numero del objeto a cacular la altura: "))
ancho=int(input("Ingresar ancho del Foso: "))
alto=int(input("Ingresar altura del salto: "))
print(f"La altura desde que cae la esfera es de: {FuncionCaida(FuncionProyectil(ancho,alto),cuerpo): .2f} m")