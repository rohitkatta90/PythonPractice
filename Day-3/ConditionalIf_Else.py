print("Welecome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120: # Note different comparison operators > , < >=, <=, ==, !=
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow little taller before you can ride.")


# Coding challenge - Check if the number is odd or even

number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")