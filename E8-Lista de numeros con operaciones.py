print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.
    B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un
    mensaje si no es posible eliminar.
    C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
    D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta 
    nueva lista, iterando por ella.
    E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista 
    original y la cantidad de veces que aparece en ella. Por ejemplo:
    si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]
"""

lista1 = ["3", "4", "5", "1", "6", "2", "99"]

print("--------Punto A---------")

lista1 = []
while True:
    numero = input("Ingrese numero para cargar en la lista, con cero finaliza: ")
    if (numero.isdigit()) == True:
        if numero != "0":
            lista1.append(numero)
        else:
            print(lista1)
            break
    else:
        print("Cadena de caracteres no valida")


print("--------Punto B---------")

while True:
    numero = input("Ingrese numero para buscar y eliminar: ")
    if (numero.isdigit()) == True:
        if numero in lista1:
            lista1.pop(lista1.index(numero))
            print(lista1)
            break
        else:
            print("No es posible eliminar el numero")
    else:
        print("Cadena de caracteres no valida")

print("--------Punto C---------")

suma = 0
for i in lista1:
    suma += int(i)
print(suma)

print("--------Punto D---------")

lista2 = []
while True:
    numero = (input("Ingrese un numero para mostrar los menores: "))
    if (numero.isdigit()) == True:
        while True:
            for i in lista1:
                if int(i) < int(numero):
                    lista2.append(i)
            break
        break
    else:
        print("Cadena de caracteres no valida")


print("--------Punto E---------")

lista3 = []
for i in lista1:
    if (i, lista1.count(i)) not in lista3:
        lista3.append((i, lista1.count(i)))
print(lista3)

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")