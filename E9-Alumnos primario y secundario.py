print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al 
    ingresar “x”. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar “x”.
        A) Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.<>
        B) Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
        C) Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
"""


primaria = ["11", "2", "3", "1", "55"]
secundaria = ["1", "55", "22", "11", "3"]
print(primaria)
print(secundaria)
"""
nombre = input("Ingrese los nombres de primaria (1 a la vez), finaliza con 'x': ")
while nombre != "x":
    primaria.append(nombre)
    nombre = input("Ingrese los nombres de primaria (1 a la vez), finaliza con 'x': ")

nombre = input("Ingrese los nombres de Secundaria (1 a la vez), finaliza con 'x': ")
while nombre != "x":
    secundaria.append(nombre)
    nombre = input("Ingrese los nombres de secundaria (1 a la vez), finaliza con 'x': ")
"""

print("----------Punto A-----------")

todos = secundaria
for i in primaria:
    if not(i in secundaria):
        todos.append(i)
print(todos)

print("----------Punto B-----------")

comunes = []
for i in primaria:
    if i in secundaria:
        comunes.append(i)
print(comunes)

print("----------Punto C-----------")

primaria_s_r = []
for i in primaria:
    if not(i in secundaria):
        primaria_s_r .append(i)
print(primaria_s_r )




print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")