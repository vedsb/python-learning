principle = 0
rate = 0
time = 0
final_total = 0

# Input principle amount
principle = float(input("Enter the principle amount: "))
while principle < 0:
    print("Principle cannot be negative. Please enter again.")
    principle = float(input("Enter the principle amount: "))

# Input time
time = float(input("Enter the time (in years): "))
while time < 0:
    print("Time cannot be negative. Please enter again.")
    time = float(input("Enter the time (in years): "))

# Input rate
rate = float(input("Enter the rate of interest: "))
while rate < 0:
    print("Rate cannot be negative. Please enter again.")
    rate = float(input("Enter the rate of interest: "))


final_total = float(principle * pow((1+rate/100),time))
print(f"Final balance after{time} is {final_total}")