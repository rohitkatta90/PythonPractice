# Learning Range in python

#Below is the syntax of the range function.
for number in range(0, 10): # this means that the number with have range from 0 to 10 but NOT INCLUDING 100
    print(number)

# IMPORTANT: SINCE WE DID NOT MENTION ABOVE BY HOW MUCH WE COULD WANT THE NUMBER TO INCREMENT, IT INCREMENTS BY 1 BY DEFAULT
# IF WE WANT IT TO INCREMENT BY ANY OTHER VALUE OTHER THAN 1 THEN BELOW IS HOW WE WRITE THE RANGE FUNCTION

for number in range(1, 11, 3):
    print(number)


total = 0
for number in range(1,101):
    total = total + number
print(total)
