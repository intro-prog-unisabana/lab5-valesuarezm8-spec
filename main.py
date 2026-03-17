from utils import*
opciones_validas= ["add", "subtract", "multiply", "divide", "exponent", "modulo", "floor_divide", "absolute"]

while True:
    answer_user= input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit").lower()
    if answer_user == "exit":
        break
    if answer_user not in opciones_validas:
        print("Invalid option!")
        continue
    if opciones_validas == "absolute":
        num1 = float(input("Enter the number:"))
        esto_da = absolute(num)
    



    else:

    


 
 