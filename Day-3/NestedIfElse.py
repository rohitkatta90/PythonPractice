print("Welecome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120: # Note different comparison operators > , < >=, <=, ==, !=
    age = int(input("What is your age? \n"))
    if age < 12:
        print("You have to pay $5")
    elif age <= 18:
        print("You have to pay $7")
    else:
        print("You have to pay $12")  
else:
    print("Sorry, you cannot buy a ticket")



# Coding challenge - BMI Calculator 2.0

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2) # The round()function will round the number to nearest whole number.

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")