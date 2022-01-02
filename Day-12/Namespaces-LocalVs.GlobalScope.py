# Namespaces - Local vs. Global Scope

##################### SCOPE #########################


enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# LOCAL SCOPE

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()

# GLOBAL SCOPE

# player_health = 10

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(f"Inside nested function: {player_health}")
#     drink_potion()

# game()
# print(player_health)

# There is no block scope in Python

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

