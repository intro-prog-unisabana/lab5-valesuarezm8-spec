from utils_calc import*

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
        resultado = absolute(num)
        print(f"The result is: {resultado}")

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

if answer_user == "add":
    result= add(num1, num2)
elif answer_user =="subtract":
    result=sub(num1, num2)
elif answer_user =="multiply":
    result=multiply(num1, num2)
elif answer_user =="divide":
    result=divide(num1, num2)
elif answer_user =="exponent":
    result=exponent(num1, num2)
elif answer_user =="modulo":
    result=modulo(num1, num2)
elif answer_user =="floor_divide":
    result=floor_divide(num1, num2)

if isinstance(result, str):
    print(result)
else:
    print(f"The result is: {resultado}")


    


 
 