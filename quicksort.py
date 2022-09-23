string = str(input("Digite os números separados por virgulas: "))
lista = string.split(',')
lista = [int(i) for i in lista]

def quicksort(lista):
    if(len(lista)>1):        
        pivo=int(len(lista)/2)
        valor=lista[pivo]
        res=quicksort([i for i in lista if i<valor]) + [i for i in lista if i==valor] + quicksort([i for i in lista if i>valor])
        return res
    else:
        return lista
print(quicksort(lista))