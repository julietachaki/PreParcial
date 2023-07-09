'''Generar una lista enlazada de películas con los siguientes datos:  nombre, valoración del público es un valor 
comprendido entre 0-10, año de estreno y recaudación.

Debe mostrar un menú que le permita realizar las siguientes tareas:

a.     filtrar las películas por año es decir mostrar todas las películas de un determinado año

b.     mostrar los datos de la película que más recaudo

c.     mostrar las películas con mayor valoración del público, puede ser más de una.

d.    generar una pila con los nombres de las películas y mostrarla ordenada.

e.    recorrer la lista y crear un archivo de texto con sus datos.'''
#Clase Pila
class Pila:
    def __init__(self):
        self.data=[]
    def Enpilar(self,item):
        self.data.append(item)
        return f"Pila Actualizada {self.data}"
    def Desapilar(self):
        return self.data.pop()
    def OrdenarPila(self):
        pilaOrdenada=self.data.sort()
        return pilaOrdenada
    def MostrarPila(self):
        print(self.data)
#Clase Lista Entazada
class Nodo:
    def __init__(self,nombre,valor,ano,precio):
        self.nombre=nombre
        self.valor=valor
        self.ano=ano
        self.precio=precio
        self.next=None
class ListaEnlazada:
    def __init__(self):
        self.head=None

    def InsertarNodo(self,new_nodo):
        if self.head:
            last_nodo=self.head
            while last_nodo.next != None:
                last_nodo=last_nodo.next
            last_nodo.next=new_nodo
        else:
            self.head=new_nodo
    def MostrarLista(self):
        temp_nodo=self.head
        while temp_nodo != None:
            print(temp_nodo.nombre,temp_nodo.ano,temp_nodo.valor,temp_nodo.precio, end ='-> ')
            temp_nodo = temp_nodo.next
        print('NULL')
    def get_data(self,dato):
        temp_nodo = self.head
        while temp_nodo != None:
            if temp_nodo.ano == dato:
                return f'Pelicula encontrada {temp_nodo.nombre}'
                break
            else: 
                
                temp_nodo=temp_nodo.next
        if temp_nodo== None:
            return ('Pelicula no encontrada' )
    def CompararPrecios(self):
        temp_nodo=self.head
        mayorprecio=temp_nodo.precio
        pelimascara=temp_nodo.nombre
        while temp_nodo !=None:
            if mayorprecio < temp_nodo.precio:
                mayorprecio=temp_nodo.precio
                pelimascara=temp_nodo.nombre,temp_nodo.valor,temp_nodo.ano,temp_nodo.precio
                temp_nodo=temp_nodo.next
            else:
                temp_nodo=temp_nodo.next
        return pelimascara
    def CompararValor(self):
        temp_nodo=self.head
        mayorvalor=temp_nodo.valor
        pelimayorvalor=temp_nodo.nombre
        while temp_nodo !=None:
            if mayorvalor < temp_nodo.valor:
                mayorvalor=temp_nodo.valor
                pelimayorvalor=temp_nodo.nombre
                temp_nodo=temp_nodo.next
            else:
                temp_nodo=temp_nodo.next
        return pelimayorvalor
    def AgregarNodoAPila(self,pila):
        pila=Pila()
        temp_nodo = self.head
        while temp_nodo != None:
            pila.Enpilar(temp_nodo.nombre)
            temp_nodo=temp_nodo.next
        pila.OrdenarPila()
        return pila.MostrarPila()
    def InsertarArchivo(self,name):
        archivo=open(name,'w')
        temp_nodo=self.head
        while temp_nodo != None:
            archivo.write(str(temp_nodo.nombre)+'\n')
            temp_nodo=temp_nodo.next
        archivo.close()
#Lista Enlazada con Peliculas
ListaPeliculas=ListaEnlazada()
pelicula1 = "Orgullo y Prejuicio"
valoracion1=9
ano1= 2002
precio1= "$10000"
pelicula2 = "Ema"
valoracion2=7 
ano2=2019 
precio2="$17000"
pelicula3 = "Un lugar para sonar"
valoracion3=4 
ano3=2012 
precio3="$23000"
pelicula4 = "Son como ninos"
valoracion4=3 
ano4=2019 
precio4="$35000"
ListaPeliculas.InsertarNodo(Nodo(pelicula1,valoracion1,ano1,precio1))
ListaPeliculas.InsertarNodo(Nodo(pelicula2,valoracion2,ano2,precio2))
ListaPeliculas.InsertarNodo(Nodo(pelicula3,valoracion3,ano3,precio3))
ListaPeliculas.InsertarNodo(Nodo(pelicula4,valoracion4,ano4,precio4))
ListaPeliculas.MostrarLista()
#Menu
menu="1) Filtrar las películas por año\n2) Mostrar los datos de la película que más recaudo\n3) Mostrar las películas con mayor valoración del público.\n4) Generar una pila con los nombres de las películas y mostrarla ordenada.\n5) Recorrer la lista y crear un archivo de texto con sus datos.\n6) Salir del Sistema"
#Sistema
def Sistema(eleccion=0):
    while eleccion <= 5:
        print(f"Posibles Tareas:\n{menu}")
        eleccion=int(input("INGRESAR NUMERO DE TAREA QUE DESEA REALIZAR:"))
        if eleccion==1:
            ano=int(input("Ingresar ano a buscar: "))
            print(f"RESULTADO\n{ListaPeliculas.get_data(ano)}")
        elif eleccion==2:
            print(f"La pelicula que mas recaudo junto: {ListaPeliculas.CompararPrecios()}")
        elif eleccion==3:
            print(f"La peli mas valorada : {ListaPeliculas.CompararValor()}")
        elif eleccion==4:
            PilaPelis=""
            print(f"Pila de peliculas ordenadas: {ListaPeliculas.AgregarNodoAPila(PilaPelis)}")
        elif eleccion==5:
            ListaPeliculas.InsertarArchivo("ArchivoPeliculas.txt")    
            print("Se creo el archivo con las peliculas\nNombre del Archivo: ArchivoPeliculas.txt")
    print('Saliste del Sistema')        
Sistema()









