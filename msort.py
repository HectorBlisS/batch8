def separa(lista):
	result=[]
	if len(lista)>1:
		mita=int(len(lista)/2)
		izquierda=lista[:mita]
		derecha=lista[mita:]
		print(izquierda,derecha)
		result=junta(result,separa(izquierda),separa(derecha)) # Recursividad!
		return result
	else:
		return lista

def junta(result,izquierda,derecha):
	while izquierda and derecha:
		if izquierda[0]<derecha[0]:
			result.append(izquierda[0])
			izquierda.pop(0)
		else:
			result.append(derecha[0])
			derecha.pop(0)
		if not izquierda:
			for i in derecha:
				result.append(i)
		elif not derecha:
			for i in izquierda:
				result.append(i)

	return result

def main():
	lista=list(map(int,input("Dame una lista de numeros desordenados: ").split(" ")))
	print("el resultado: ",separa(lista))

main()

