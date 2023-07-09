'''
Una RTO desea desarrollar un sistema para la gestion de los turnos de ingreso de los vehiculos'.
El dueno del establecimiento escribio un doc con las especificaciones, las cuales se resumen:
tiene que haber tres colas, una para motos, una para autos y otra para camionetas
el sistema debe mostraar un menu con las opciones disponibles: 
        encolar turnos motos
        encolar turnos autos
        encolar turnos camionetas
        LLamar clientes motos
        LLamar clientes autos
        LLamar clientes camioneta
        mostrar colas motos
        mostrar colas autos
        mostrar colas camionetas
        Salida
'''
'''
class Cola:
    def __init__(self):
        self.data=[]
    def encolar(self,obj):
        self.data.append(obj)
        print('Cola Actualizada',self.data)
    def desencolar(self):
        return self.data.pop(0) if self.data != [] else "La cola está vacía"
    def mostrar (self):
        return self.data

ColaAutos=Cola()
ColaMotos=Cola()
ColaCamionetas=Cola()


def Sistem(Accion = 0):
    while Accion < 10:

        print("Seleccionar numero accion a realizar: \n 1- Sumar auto a la cola \n 2- Sumar moto a la cola\n 3- Sumar camioneta a la cola \n 4-LLamar auto \n 5-LLamar moto\n 6-LLamar camioneta \n 7-Mostrar cola de autos \n 8-Mostrar cola de moto \n 9-Mostrar cola de camioneta \n 10-Salir ")
        Accion =int(input(" Accion a Realizar:"))


        if Accion==1:
            vehiculo= str(input("Ingresar nombre del dueno del auto: "))
            ColaAutos.encolar(vehiculo) 
            
        elif Accion == 2:
            vehiculo=str(input("Ingresar nombre del dueno de la moto"))
            ColaMotos.encolar(vehiculo)
            
        elif Accion == 3:
            vehiculo=str(input("Ingresar nombre del dueno de la camionta"))
            ColaCamionetas.encolar(vehiculo)
        
            
        elif Accion == 4:
            print(f'Es el turno del auto de : {ColaAutos.desencolar()}')
            
        elif Accion == 5:
            print(f'Es el turno de la moto de : {ColaMotos.desencolar()}')
        
            
        elif Accion == 6:
            print(f'Es el turno de la camioneta de : {ColaCamionetas.desencolar()}')
        
            
        elif Accion == 7:
            print(f"La cola de autos es : {ColaAutos.mostrar()}")
        
        
        elif Accion == 8:
            print(f"La cola de motos es : {ColaMotos.mostrar()}")
        
        
        elif Accion == 9:
            print(f"La cola de camionetas es : {ColaCamionetas.mostrar()}")
    print("Saliste del sistema")
        
Sistem()
'''

'''Dado un parrafo que que finaliza en un puntto,separar dicho parr en 3 pilas: vocales,consonantes,simbolos.
 Luego utilizando la operciones de pilas resolver las sig consignas::
 1-cant de caracteres de cada tipo
 2-cant de espacios en blanco
 3-cantidad de numeros
 4-determinar si la cantidad de vocales y otros caracteeres  son iguales
 5-determinar si existe al menos una z en la pila de consonantes'''
'''
class Pila:
    def __init__(self):
        self.data = []
    def apilar(self,obj):
        self.data.append(obj)
    def mostrar(self):
        return self.data
    def longitud(self):
        return len(self.data)
    
PilaVocales=Pila()
PilaConsonantes=Pila()
PilaRaros=Pila()
parrafo = "La teoría de lenguajes de programación es una rama de la ciencias de la computación que se encarga del diseño, implementación, análisis, caracterización y  clasificación de lenguajes de programación y sus características."
print(parrafo)
vocales=["a","e","i","o","ó","u","í",'á']
consonantes=["q","w","r","t","y","ñ","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
espacios=0 
for i in parrafo:
    if i in vocales:
        PilaVocales.apilar(i)
    elif i.lower() in consonantes:
        PilaConsonantes.apilar(i)
    elif i == " ":
        espacios+=1
    else:
        PilaRaros.apilar(i)
print(PilaConsonantes.mostrar())
print(PilaVocales.mostrar())
print(PilaRaros.mostrar())
print(f"La cantidad de espacios es {espacios}")

if PilaVocales.longitud()== PilaRaros.longitud():
    print("Misma cantidad de raros y vocales")

'''

'''
Una famrmacia desea desarrollar un sistema para gestion de turnos de ingreso de clientes.El dueno de la farmacia
escribeio un doc con las especificaciones:
1-Tiene que haber dos colas, una para clientes particulares y otra para clientes de obra social
2-Mostrar menu con las opciones disponibles:
1[Enciolar turno particular]
2[Encolar turno obra social]
3[Llamar cliente particular]
4[Llamar cliente obra social]
5[mostrar cola obra social]
6[mostrar cola particular]
7[cerrar]
'''
class Cola:
    def __init__(self):
        self.data=[]
    def encolar(self,obj):
        return self.data.append(obj)
    def desenncolar(self):
        return self.data.pop(0) if self.data != [] else 'Cola vacia'
    def MostrarCola(self):
        return self.data
#Clases
ColaObraSocial=Cola()
ColaParticular=Cola()
#Menu
menu="Operaciones:\n1_Encolar turno particular\n2_Encolar turno obra social\n3_Llamar cliente particular\n4_Llamar cliente obra social\n5_Mostrar cola obra social\n6_Mostrar cola particular\n7_Salir del Sistema"


def Sistem(eleccion=0):
    while eleccion <7:
        eleccion=int(input(f"{menu}\n \nIngresar el numero de la operacion a realizar:  "))

        if eleccion==1:
            turno= str(input("Ingresar nombre : "))
            ColaParticular.encolar(turno) 
            
        elif eleccion == 2:
            turno=str(input("Ingresar nombre: "))
            ColaObraSocial.encolar(turno)
            
        elif eleccion == 3:
            print(f'Es el turno de: {ColaParticular.desenncolar()}')      

        elif eleccion == 4:
            print(f'Es el turno de: {ColaObraSocial.desenncolar()}')
            
        elif eleccion == 6:
            print(ColaParticular.MostrarCola())
        
        elif eleccion == 5:
            print(ColaObraSocial.MostrarCola())

        elif eleccion == 7:
            print("Saliste del sistema")
        
Sistem()
