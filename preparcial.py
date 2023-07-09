"""
1_Leer una frase 
2_General un archivo con la frase
3_Leer el archivo y cargar una lista
4-Leer lista y poner en una pila 
5_Imprimir pila invertida
"""
class Pila:
    def  __init__(self):
        self.lis= []
    def apilar(self,item):
        self.lis.append(item)
    def desapilar(self):
        return self.lis.pop()
    def mostrar(self):
        return self.lis

frase=str(input('Ingresar una frase: '))
print('Leer frase:', frase)
with open("preparcial.txt" ,"w") as file:
    file.write(str(frase))
with open('preparcial.txt',"r") as file:
    print("La frase escrita en el archivo es:" , file.read())

lista=[1,2,3,4,4,54,5,6,6,78,97]
with open('preparcial.txt',"w") as file:
    file.write(str(lista))
with open('preparcial.txt','r') as file:
    print("La lista en el archivo es: ", file.read())

pila1=Pila()
for i in lista:
    pila1.apilar(i)
print(pila1.mostrar())

pila2=Pila()
for i in range(len(pila1.mostrar())):
    pila2.apilar(pila1.desapilar())
print(pila2.mostrar())



