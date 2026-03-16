import random
start_val= int(input("Enter the start value:\n"))
end_val= int(input("Enter the end value:\n"))

semilla= random.seed(123)
entero_aleatorio = random.randint(start_val, end_val)

print(f"Generated random number: {entero_aleatorio}")