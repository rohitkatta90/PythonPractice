# Dictionaries



programming_dictionary = {
    "bug": "An error in the program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over ad over again."
}

print(programming_dictionary)

# RETRIEVING VALUES FROM THE DICTIONARY
print(programming_dictionary["bug"])
# KEY AND VALUES BOTH NEEDS TO BE PUT IN THE DOUBLE QUOTATION MARKS.

# ADDING NEW ITES TO THE DICTIONARY
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

# CREATING EMPTY DICTIONARY
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}

#print(programming_dictionary)

# Edit an item in the dictionary
programming_dictionary["bug"] = "This is the edited line for bug key"

print(programming_dictionary["bug"])

# LOOP THROUGH A DICTIONARY

for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])

