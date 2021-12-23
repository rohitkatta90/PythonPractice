# Write a program that adds the digits in a two digit number Eg: if the inut was 35, then the output should be 3 + 5 = 8

two_digit_number = input("Type a two digit number\n")
print(type(two_digit_number))
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
sum = int(first_digit)+int(second_digit)
print(first_digit+ " + " +second_digit+" = "+str(sum))