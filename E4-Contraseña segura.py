print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Realizar un programa donde el usuario introduzca una contraseña y se verifique que tiene mayúsculas, minúsculas 
    números, signos, repeticiones y espacios. 
    
    Condiciones de contraseña segura (Cantidades justas, no mas):
        2 Mayúsculas
        2 Números
        0 espacios
        0 signos
        0 repeticiones
    Si no, que muestre un aviso de contraseña insegura. 
"""
print("Cree una nueva contraseña que contenga: \n  2 Mayúsculas, 2 Números, 0 espacios, 0 signos y 0 repeticiones \n  Con un mínimo de 6 y máximo 12 caracteres. \n")
contraseña = str(input("Introduzca la contraseña:"))

longitud_correcta = False 
can_mayúsculas = 0
can_minúsculas = 0
can_números = 0
can_sígnos = 0
longitud_mínima = 6
longitud_máxima = 12
espacios = False
can_repetición = 0

if (len(contraseña) >= longitud_mínima and len(contraseña) <= longitud_máxima):
    #print("longitud correcta", len(contraseña))
    longitud_correcta = True


for caracter in contraseña:
    c_mayúscula = caracter.upper()
    c_minúscula = caracter.lower()
    if (caracter == c_mayúscula and caracter != c_minúscula):   #Mayúsculas
        #print("Tiene mayúscula", caracter)
        can_mayúsculas += 1

    if (caracter == c_mayúscula and caracter == c_minúscula):   #No letra
        #print("Tiene 'no letra':", caracter)

        numero = caracter in "1234567890"
        if (numero == True):                                    #Numero o símbolo.
            #print("Tiene un numero:", caracter)
            can_números += 1
        else:
            #print("Tiene un signos:", caracter)
            can_sígnos += 1
    
    if (caracter == " "):                                       #Espacios
        #print("Tiene espacio")
        espacios = True
 
    repetición = contraseña.count(caracter)
    if (repetición > 1):                                        #Repeticiones
        print(caracter)
        can_repetición += 1


if (longitud_correcta == True):                                 #Comparación de condiciones.
    if (can_mayúsculas == 2):                                       
        if (can_números == 2):
            if (espacios == False):
                if (can_sígnos == 0):
                    if (can_repetición == 0):
                        print("Contraseña segura")
                    else:
                        print("Contraseña insegura por tener", can_repetición, "repeticiones")
                else:
                    print("Contraseña insegura por tener", can_sígnos, "signos")
            else:
                print("Contraseña insegura por tener espacios")
        else:
            print("Contraseña insegura por tener", can_números, "números")
    else:
        print("Contraseña insegura por tener", can_mayúsculas, "mayúsculas")
else:
    print("Contraseña insegura por tener longitud incorrecta")


print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
