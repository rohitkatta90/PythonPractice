# Coding Exercise - Adding Evens

# Approach - 1
total = 0
for number in range(1,101):
    if number % 2 == 0:
        total = total + number
print(f"The addition of even numbers is {total}")


# Approach - 2

total1 = 0
for number in range(2,101,2):
        total1 = total1 + number
print(f"The addition of even numbers is {total1}")