print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

cadena = "AAAAA"

j = len(cadena) - 1
i = 0
palind = True
while i < len(cadena) / 2:          
    inicial = (cadena [i])
    i += 1
    final = (cadena [j])
    j -= 1
    if (final != inicial):
        palind = False
if (palind == True):
    print("Si es palíndromo")
else:
    print("No es palíndromo")

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")