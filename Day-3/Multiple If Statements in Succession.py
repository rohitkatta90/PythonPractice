# Multiple If Statements in Succession

print("Welecome to the rollercoaster!")
bill = 0
height = int(input("What is your height in cm? "))
if height >= 120: # Note different comparison operators > , < >=, <=, ==, !=
    age = int(input("What is your age? \n"))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")  

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you cannot buy a ticket")


# Coding challenge - Pizza order program.

