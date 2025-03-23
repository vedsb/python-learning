num = int(input("enter a num between 1-100"))

while num < 1 or num > 100 :
    print(f"{num} is not valid")
    num = int(input("enter a num between 1-100"))
print(f"u entered {num}")