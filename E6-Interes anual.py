print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
    y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""

monto = float(input("Ingrese el monto a invertir: $"))
interés = float(input("Ingrese el interés anual: "))
años = int(input("Ingrese el numero de años: "))

for i in range(1, años + 1):
    monto += monto * interés / 100
    print("El monto total en", i, "años es de", round(monto, 2))

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")