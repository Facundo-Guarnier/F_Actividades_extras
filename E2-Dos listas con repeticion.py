print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escriba un programa que tenga dos listas y que, a continuación, cree las siguientes 
    listas (en las que no debe haber repeticiones):
        1) Lista de elementos que aparecen en las dos listas.
        2) Lista de elementos que aparecen en la primera lista, pero no en la segunda.
        3) Lista de elementos que aparecen en la segunda lista, pero no en la primera.
        4) Lista con la intersección de ambas listas.
"""

mi_lista1 = ["facu", "jorge", "vivi", "tomas", "laucha", "juan", "gusti", "vivi", "laucha", "tomas",] 
mi_lista2 = ["facu", "jorge", "lucas", "giovanni", "nico", "lucas", "giovanni", "messi", "pino"]

print("\n----------------------Punto 1)------------------------\n")

mi_conjunto1 = (set(mi_lista1))
mi_conjunto2 = (set(mi_lista2))
mi_lista_union = list(mi_conjunto2 | mi_conjunto1)

print( mi_lista_union)

print("\n----------------------Punto 2)------------------------\n")

mi_conjunto1 = (set(mi_lista1))
mi_conjunto2 = (set(mi_lista2))
mi_lista = mi_conjunto1 - mi_conjunto2
print(mi_lista)

print("\n----------------------Punto 3)------------------------\n")

mi_conjunto1 = (set(mi_lista1))
mi_conjunto2 = (set(mi_lista2))
mi_lista = mi_conjunto2 - mi_conjunto1
print(mi_lista)

print("\n----------------------Punto 4)------------------------\n")

mi_conjunto1 = (set(mi_lista1))
mi_conjunto2 = (set(mi_lista2))
mi_lista = mi_conjunto2 & mi_conjunto1
print(mi_lista)
print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")