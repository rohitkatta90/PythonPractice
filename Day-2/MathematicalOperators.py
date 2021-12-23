print(3+5)
print(3-5)
print(3*5)
print(10/5) # this always returns a float type value
print(2**3)

# PEMDASLR (LR here stands for Left to Right)
# Paranthesis ()
# Exponential **
# Multiplication *
# Division /
# Addition  +
# Subtraction - 

print(3 * 3 + 3 / 3 - 3)

print(3 * (3 + 3) / 3 - 3)

# Code Challenge - BMI Calculator Exercise

# BMI - weight(kgs) / height*height (m square)

#height = input("Enter your height in m: ")
#weight = input("Enter your weight in kg: ")
#bmi = int(weight)/(int(height)*int(height))
#print("Your BMI is: "+str(bmi))


#Rounding number

print(8/3)
print(round(8/3))
print(round(8/3 , 3)) # will give the result till 3 decimals only
print(8 / 2) # the result of this will be in floating type
print(8 // 2) # the result if this will be in int type

# f-string
score = 0
height = 1.8
isWinning = True
#Normal print way - Tedious job
print("Your score is : "+str(score) + " "+str(height)+ " "+ str(isWinning)) # this is tedious job to convert and then print

#f-string - Easy way
print(f"Your score is : {score}, you height is {height}, you are winning is {isWinning}")

# Coding challenge
# WAP using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 yeaars old.

# Assumptions - 1 year has 365 days, 52 weeks, and 12 months 

age = input("What is your current age?\n")
age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining}days, {weeks_remaining}weeks and {months_remaining}months left"
print(message)


