import os
import math
print("CCurrent working directory: ", os.getcwd())
entero= int(input("Enter an integer: "))
valor_log = math.log2(entero) 
print(f"Log base 2 of {entero} is: {valor_log}")
print("Floor:",math.floor(valor_log))
print("Ceiling:",math.ceil(valor_log))