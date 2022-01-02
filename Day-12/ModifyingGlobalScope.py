# Modifying a variable in Global Scope
enemies = 1

def increase_enemies():
    global enemies # NOTE the "global" keyword here..
    enemies += 1
    print(f"enemies inside function: {enemies}")
    return enemies + 1

increase_enemies()
print(f"enemies outside function: {enemies}")

# we can also return the global variable and then return it with the function as below

enemies = increase_enemies()
print(f"The global varaible after incrementing is is {enemies}")