lista_ingredientes = ['Azúcar', 'Agua', 'Limón'] 
diabetico = True

for ingrediente in lista_ingredientes: 
	if diabetico == True and ingrediente == 'Azúcar': 
		break  
	print(ingrediente) 

######################################################
#Definición de la función 
def mi_función_saludo(nombre, saludo = 'Hi,'): 

	print(saludo, nombre) 

#Llamada a la función 
resultado = mi_función_saludo ('Peter') 

#######################################################
lado = 5 
area_cuadrado = lambda x: x*x
print(area_cuadrado(lado))

"""
numeros = [1, 2, 3, 4, 5]
cuadrados = lambda x: x**2
print(cuadrados(5))
"""