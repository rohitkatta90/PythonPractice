# Nesting Lists and Dictionaries

# dictionary1 = {
#     "key": "value",
#     "key2": [List], # A LIST can also be added as velue for any key in the dictionary.
#     "key3": {dictionary2} # A DICTIONARY can also be added as velue for any key in the dictionary.
# }

# Nesting
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

# Nesting a List in a Dictionary

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin","Hamburg","Stutgart"]
}

# Nesting a List inside a List
["A" , "B" , ["C","D"]]

# Nesting a dictionary in a dictinary
travel_log = {
    "France" : {
        "cities_visited" : ["Paris", "Lille", "Dijon"], 
        "total_visits" : 12
        },
    "Germany" : {
        "cities_visited" : ["Berlin","Hamburg","Stutgart"],
         "total_visits" : 10
         }
}

# Nesting Dictionary in a List

travel_log = [
    {
        "country_visited" : "France",
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visits" : 12
    },  
    {
        "country_visited" : "Germany"
        ,"cities_visited" : ["Berlin","Hamburg","Stutgart"],
        "total_visits" : 10
    }     
]
    