print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
Escriba un programa donde tenga una lista y que, a continuación, elimine los elementos repetidos, 
por último mostrar la lista.
"""

print("--------------------------Opción 1----------------------------")
mi_lista = ["facu", "jorge", "vivi", "tomas", "laucha", "juan", "gusti", "vivi", "laucha", "tomas",] 

indice = -1
while indice < len(mi_lista):
    indice += 1
    elemento = mi_lista[indice]
    cantidad = mi_lista.count(elemento)

    if (cantidad > 1):
        mi_lista.pop(indice)

print(mi_lista)


print("--------------------------Opción 2----------------------------")
mi_lista = ["facu", "jorge", "vivi", "tomas", "laucha", "juan", "gusti", "vivi", "laucha", "tomas",] 

mi_lista = list(set(mi_lista))
print(mi_lista)

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")