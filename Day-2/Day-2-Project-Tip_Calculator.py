# Final Project - Day 2 - Tip Calculator

print("\n\n*** Welcome to the Tip Calculator! ***\n")
bill = float(input("What was the total bill? $ "))
tip = int(input("How much percentage tip would you like to give? 10, 12, 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = ((tip/100) *  bill) + bill

bill_per_person =  bill_with_tip/people

#final_amount = round(bill_per_person,2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"\nEach person should pay ${final_amount}\n")

# for the input - 150, 12 percent and people to split between  is 5 then the answer we get does not have value rounded
# to 2 decimals inspite of have round() function???

#Soution for it is to use some formatting as below

final_amount = "{:.2f}".format(bill_per_person) # this formatting is used in above code.