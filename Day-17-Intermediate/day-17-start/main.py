# Creating Class

class User:
    pass
    # pass actually tells python to continue with the code and do not throw error inspite of not having any code
    # inside it.


user_1 = User()
user_1.id = "001"
user_1.username = "rohit"
print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "rani"
print(user_2.username)


# Pascal Case is used for naming the class

class ThisIsTheClassName:
    pass


# Camel case is where the first letter is small.
camelCase = 0

# snake case
this_is_the_snake_case = 0

