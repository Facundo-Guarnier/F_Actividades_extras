fila = int(input("introduce el numero de filas: "))
colu = int(input("introduce el numero de columnas: "))

# creamos la primera matriz - definimos la matriz
A =[]
for i in range(fila):
	A.append ([0]*colu)
	print(A[i])

# creamos la segunda matriz	
B =[]
for i in range(fila):
	B.append ([0]*colu)
	print(B[i])
	
# creamos la matriz	resultado
C =[]
for i in range(fila):
	C.append ([0]*colu)
	print(C[i])
	
#Ingresamos la primera matriz
print("ingrese los valores de la primera matriz\n")
for i in range(fila):
	for j in range (colu):
		A[i][j] = int(input("Ingrese el componente (%d %d): " %(i,j)))
		
#Ingresamos la segunda matriz
print("ingrese los valores de la segunda matriz\n")
for i in range(fila):
	for j in range (colu):
		B[i][j] = int(input("Ingrese el componente (%d %d): " %(i,j)))
		
print("\nLa primera matriz es: ")
for i in range(fila):
	print(A[i])

print("\nLa segunda matriz es: ")	
for i in range(fila):
	print(B[i])	
	
#Sumamos las dos matrices

for i in range(fila):
	for j in range(colu):
		C[i][j] = A[i][j] + B[i][j]

#imprimimos la matriz resultante
print ("\nLa matriz resultante es: ")
for i in range (fila):
	R = []
	for j in range(colu):
		R.append(C[i][j])
	print (R)
	

