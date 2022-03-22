print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escribir una funcion que indique si el usuario es mayor de edad.
"""

def mayor_edad(usuario):
    return usuario.edad123 > 17

class Usuario:
    def __init__ (self, edad):
        self.edad123 = edad

usuario1 = Usuario(15)

print(mayor_edad(usuario1))

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")