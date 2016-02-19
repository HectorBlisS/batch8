def sort(array):
    menor = []
    igual = []
    mayor = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                menor.append(x)
            if x == pivot:
                igual.append(x)
            if x > pivot:
                mayor.append(x)
        
        return sort(menor)+igual+sort(mayor)  # Recursividad!
    else:  
        return array
def main():
    array=list(map(int,input("dame una lista de numeros: ").split(" ")))
    print(sort(array))
main()