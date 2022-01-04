# We first need to import the package responsible for creating the pretty table.
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# This is to left align the data
table.align = "l"

print(table)

# Changing table style


