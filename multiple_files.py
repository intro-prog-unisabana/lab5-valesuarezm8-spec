from utils import*

mensaje=input("Please type your message\n")
mensaje_invertido= flip(mensaje)
canditad_de_a=count_letters(mensaje, 'a')
resultado = mensaje_invertido + str(canditad_de_a)
print(f"Your encoded message is: {resultado}")