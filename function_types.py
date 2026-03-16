


def list_shift(lista, valor):
    for i in range(len(lista)):
        lista[i] = lista[i] + valor
    
def calc_avg(lista):
    suma = 0.0
    for num in lista:
        suma = suma + num
        promedio= suma/len(lista)
        return(promedio)
    
def print_normalized(lista):
    print(lista)

numeros=[1.0, 2.0, 3.0, 4.0, 5.0]
promedio=calc_avg(numeros)
list_shift(numeros, -promedio)
print_normalized(numeros)