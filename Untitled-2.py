pelicula1 = "Orgullo y Prejuicio, 9 , 2002 , $10000"
pelicula2 = "Ema, 7 , 2019 , $17000"
pelicula3 = "Un lugar para sonar, 4 , 2012 , $23000"
pelicula4 = "Viviendo en el paraiso, 6 , 2020 , $19500"
pelicula5 = "Son commo ninos, 3 , 2019 , $35000"
Peliculas=[pelicula1,pelicula2,pelicula3,pelicula4,pelicula5]
'''menu="1) Filtrar las películas por año es decir mostrar todas las películas de un determinado año\n2) Mostrar los datos de la película que más recaudo\n3) Mostrar las películas con mayor valoración del público, puede ser más de una.\n4) Generar una pila con los nombres de las películas y mostrarla ordenada.\n5) Recorrer la lista y crear un archivo de texto con sus datos.\n6) Salir del Sistema"


def Sistema(eleccion=0):
    while eleccion <= 6:
        print(f"Posibles Tareas:\n{menu}")'''
eleccion=int(input("Ingrese numero de la tarea a realizar:"))
if eleccion==1:
    for i in Peliculas:
        while i != ",":
            Peliculas[i]+=1
        Peliculas[:i]
        print(Peliculas)
