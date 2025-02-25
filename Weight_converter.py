weight = (float(input("enter your weight in (K/L)")))

unit = input("enter the unit K/L")

if unit == "K":
  weight = weight*2.205
  unit = "Lbs"

else :
  weight = weight/2.205
  unit = "kg"

print(f"the cover ted weight is{weight} {unit}")