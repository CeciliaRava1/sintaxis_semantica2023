# Dados dos conjuntos A={1,2,3,4,5,6,7,} y B={8,9,10,11} la unión de estos conjuntos
# será A∪B={1,2,3,4,5,6,7,8,9,10,11}

#Ingreso y comprobacion conjunto A
correcto = 0
while correcto != 1:
	conjunto_a = input('Ingrese el conjunto a encerrado entre llaves y con sus elementos separados por comas')
	if conjunto_a[0] == '{' and conjunto_a[-1] == '}':
		correcto = 1
correcto = 0

#Ingreso y comprobacion conjunto B
while correcto != 1:
	conjunto_b = input('Ingrese el conjunto a encerrado entre llaves y con sus elementos separados por comas')
	if conjunto_b[0] == '{' and conjunto_b[-1] == '}':
		correcto = 1
correcto = 0

#Union de conjuntos
def union_conjuntos(conjunto_a, conjunto_b):
	conteo = 0
	longitud_b = len(conjunto_b)-1
	nueva_cadena = '{'
	for i in conjunto_a:
		if i != '{' and i != '}' and i != ',':
			nueva_cadena += i
			nueva_cadena += ','

	for i in conjunto_b:
		conteo += 1
		if i != '{' and i != '}' and i != ',':
			if i not in nueva_cadena and conteo != longitud_b:
				nueva_cadena += i
				nueva_cadena += ','
			elif conteo == longitud_b:
				nueva_cadena += i
	nueva_cadena += '}'
	return nueva_cadena


#Interseccion de conjuntos
def interseccion_conjuntos(conjunto_a, conjunto_b):
	nueva_cadena = '{'
	nueva_cadena2 = ''
	conteo = 0
	for i in conjunto_b:
		if i != '{' and i != '}' and i != ',':
			if i in conjunto_a:
				nueva_cadena += i
				nueva_cadena += ','
	for i in nueva_cadena:
		conteo +=1
		if conteo < len(nueva_cadena):
			nueva_cadena2 += i
	nueva_cadena2 += '}'
	return f' La INTERSECCION entre los dos conjuntos es {nueva_cadena2}'

#Diferencia de conjuntos
def diferencia_conjuntos(conjunto_a, conjunto_b):
	nueva_cadena = '{'
	nueva_cadena2 = ''
	conteo = 0
	for i in conjunto_a:
		if i != '{' and i != '}' and i != ',':
			if i not in conjunto_b:
				nueva_cadena += i
				nueva_cadena += ','
	for i in nueva_cadena:
		conteo +=1
		if conteo < len(nueva_cadena):
			nueva_cadena2 += i
	nueva_cadena2 += '}'
	return f' La DIFERENCIA entre los dos conjuntos es {nueva_cadena2}'


#Complemento de un conjunto
def complemento_conjunto(conjunto_a, conjunto_b):
	nueva_cadena = '{'
	nueva_cadena = '{'
	nueva_cadena2 = ''
	conteo = 0
	for i in conjunto_a:
		if i != '{' and i != '}' and i != ',':
			if i not in conjunto_b:
				nueva_cadena += i
				nueva_cadena += ','
	for i in nueva_cadena:
		conteo +=1
		if conteo < len(nueva_cadena):
			nueva_cadena2 += i
	nueva_cadena2 += '}'
	return f' El COMPLEMENTO entre los dos conjuntos es {nueva_cadena2}'

#Tamanio de un conjunto
def tamanio_conjunto(conjunto_a):
	cantidad_llaves_apertura = -1
	for i in conjunto_a:
		if i == '{':
			cantidad_llaves_apertura += 1
	return f'El TAMANIO del conjunto es {cantidad_llaves_apertura}'

#Operacion a realizar
while correcto != 1:
	operacion = int(input('Que operacion desea realizar? 1.Union; 2.Interseccion 3.Diferencia 4.Complemento 5.Tamanio'))
	if operacion == 1:
		correcto = 1
		resultado = union_conjuntos(conjunto_a, conjunto_b)
		print(resultado)

	elif operacion == 2:
		correcto = 1
		resultado = interseccion_conjuntos(conjunto_a, conjunto_b)
		print(resultado)

	elif operacion == 3:
		correcto = 1
		resultado = diferencia_conjuntos(conjunto_a, conjunto_b)
		print(resultado)

	elif operacion == 4:
		correcto = 1
		resultado = complemento_conjunto(conjunto_a, conjunto_b)
		print(resultado)

	elif operacion == 5:
		correcto = 1
		resultado = tamanio_conjunto(conjunto_a)
		print(resultado)

	else:
		print('Lo ingresado no corresponde a una operacion, intenta otra vez')
