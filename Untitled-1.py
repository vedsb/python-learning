operator = (input("enetr the operation"))
num1 = float(input("Enter num 1: "))
num2 = float(input("Enter num 2: "))

if operator=="+" :
    print(float(num1 + num2))

elif operator=="-" :
    print(float(num1 - num2))

elif operator=="*" :
    print(float(num1 * num2))

elif operator=="/" :
    print(float(num1 / num2))

else  :
    print("wrong num")