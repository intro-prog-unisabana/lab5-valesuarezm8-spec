
def list_shift(lista2, numero):
    numero=float(numero)
    for i in range(len(lista2)):
        lista2[i]=lista2[i]+numero

def calc_avg(lista2):
    
    for num in lista2:
        
        promedio= sum(lista2)/len(lista2)
        return promedio
    
def print_normalized(lista2):
    print(lista2)

datos = [2.0, 4.0, 6.0, 8.0]

prom = calc_avg(datos)         # 5.0
list_shift(datos, -prom)       # datos se convierte en [-3.0, -1.0, 1.0, 3.0]
print_normalized(datos)        # imprime [-3.0, -1.0, 1.0, 3.0]