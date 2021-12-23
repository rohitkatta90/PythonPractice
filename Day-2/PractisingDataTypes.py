# Below 2 times erros out. Please run and check the error. Error is: "TypeError: can only concatenate str (not "int") to str"

num_char = len(input("What is your name?\n"))
#print("Your name has " + num_char + " characters")

# checking the type of the variable or data in the variable.
# type() function is used for it
print(type(num_char)) 

# Type casting

new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters")

a = 123
print(type(a))
a = str(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))

