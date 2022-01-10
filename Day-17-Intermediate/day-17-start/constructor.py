# In Python, the constructors are created by using the init function, and it is called as Initializing


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "rohit")
# print(user_1.id)
# print(user_1.username)
#
user_2 = User("002", "rani")
# print(user_2.id)
# print(user_2.username)

# Check this line, when the constructor has some default value then it's not needed to pass in as argument in function call.

# Adding methods to classes.

# Attributes are the things that the object has.
# Methods are the things that the object does.

# Functions inside the class are called methods.
user_1.follow(user_2)
print(f" User 1 followers: {user_1.followers}")
print(f" User 1 following: {user_1.following}")
print(f" User 2 followers: {user_2.followers}")
print(f" User 2 following: {user_2.following}")
