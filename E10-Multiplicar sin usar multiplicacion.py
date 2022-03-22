print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Multiplicar sin utilizar el simbolo *.
"""

numero1 = False
numero2 = False
resultado = 0

while numero1 == False:                                         #Comprobar si es int.
    numero1 = input("Introducta un numero: ")

    try: 
        numero1 = int(numero1)
    except:
        numero1 = False

    if numero1 == False:
        print("No se ingreso una cadena de caracteres correcta (letras o simbolos)")


while numero2 == False:                                         #Comprobar si es int.
    numero2 = input("Introducta un numero: ")

    try: 
        numero2 = int(numero2)
    except:
        numero2 = False

    if numero2 == False:
        print("No se ingreso una cadena de caracteres correcta (letras o simbolos)")


for i in range(numero1):                                        #Calcular suma reiterada (multiplicacion)
    resultado += numero2

print(resultado) 


print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")