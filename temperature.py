unit = input("enter the unit of convrsion C/F")
temperature=(float(input("enter the temperature")))


if unit == "C":
    temperature = round((9*temperature) / 5 + 32 , 2)
    unit = "farhenite"

elif unit== "F":
    temperature =round( (temperature-32) *5 /9 ,2)
    unit = "celcius"
else :
    print(f"invalid {unit}")

print (f"the coverted temperature is{temperature} {unit}")