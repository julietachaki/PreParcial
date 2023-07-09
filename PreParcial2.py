

'''
1_ realizar un programa que genere a la azar 50 numeros entre 0 y 100 y lo guarde en un archivo de texto.
2_ luego leer el archivo y guardarlo en una lista enlazada en forma ordenada
3_ posteriormente recorra la lista y genere otro archivo con los valores de la lista ordenada'''
import random 
class Nodo:
    def __init__(self,data):
        self.data=data
        self.next=None

class ListEnla:
    def __init__(self):
        self.head= None
    def insertar(self,new_nodo):
        if self.head:
            last_nodo=self.head
            while last_nodo.next != None:
                last_nodo=last_nodo.next
            last_nodo.next=new_nodo
        else:
            self.head=new_nodo
            
    def display(self):
        temp_nodo=self.head
        while temp_nodo != None:
            print(temp_nodo.data, end ='-> ')
            temp_nodo = temp_nodo.next
        print('NULL')

    def InsertarArchivo(self,name):
        archivo=open(name,'w')
        temp_nodo=self.head
        while temp_nodo != None:
            archivo.write(str(temp_nodo.data)+'\n')
            temp_nodo=temp_nodo.next
        archivo.close()

    

ld=open('listadesordenada.txt','w')
for i in range(50):
    num=random.randint(0,100)
    ld.write(str(num)+'\n')
    
ld.close()

ListaDesordenada=[]
ld=open('listadesordenada.txt','r')
linea=ld.readlines()
ld.close()

for i in linea:
    ListaDesordenada.append(int(i))
print('LISTA DESORDENADA')
print(ListaDesordenada)

def inseccion(lista): 
    for i in range(1,len(lista)):
        actual = lista[i]
        j = i
        while j>0 and lista[j-1]>actual:
            lista[j]=lista[j-1]
            j = j-1
        lista[j]=actual

ListaOrdenadaEnlazada=ListEnla()
print('\n')
inseccion(ListaDesordenada)

for i in ListaDesordenada:
    ListaOrdenadaEnlazada.insertar(Nodo(i))

print('LISTA ENLAZADA ORDENADA')
ListaOrdenadaEnlazada.display()

ListaOrdenadaEnlazada.InsertarArchivo('archivoOrdenado.txt')











