'''
Procesar el archivo con los nombres de los alumnos y sus notas, armar dos listas enlazadas, una con aquellos que hayan
aprobado y otra con los que hayan desaprobado. luego imprimir ambas listas con los nombres y las notas.
'''
class Nodo:
    def __init__(self,data):
        self.next=None
        self.data=data
class ListaEnlazada:
    def __init__(self,):
        self.head=None
    def insertarNodo(self,new_nodo):
        if self.head==None:    
            self.head=new_nodo
        else:
            last_nodo=self.head
            while last_nodo.next != None:
                last_nodo =last_nodo.next
            last_nodo.next=new_nodo
    def display(self):
        temp_nodo=self.head
        while temp_nodo != None:
            print(temp_nodo.data, end ='-> ')
            temp_nodo = temp_nodo.next
        print('NULL')
ListaNotasDesaprobadas=ListaEnlazada()
ListaNotasAprobadas=ListaEnlazada()
notas=open('alumnos.txt',"r")
for i in range(7):
    nota_actual=notas.readline()
    if int(nota_actual[-2])< 6: 
        ListaNotasDesaprobadas.insertarNodo(Nodo(nota_actual))
    else:
        ListaNotasAprobadas.insertarNodo(Nodo(nota_actual))

notas.close()


ListaNotasDesaprobadas.display()
ListaNotasAprobadas.display()