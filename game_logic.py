import random
print("Enter a seed number:")
semilla= random.seed(input(int()))
entero_aleatorio = random.randint(1, 10)
count=0
guess=input("What is your guess: ")
count+=1
if guess >= entero_aleatorio:
    print("Too high! Try a lower number.")
elif guess <= entero_aleatorio:
    print("Too low! Try a higher number.")
else:
    ("Correct! You guessed the number!")
print(f"It took you {count} tries!")