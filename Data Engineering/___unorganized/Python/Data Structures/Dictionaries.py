# ---- Accesing a dictionary value

fligth_prices = {
    "Chicago": 199,
    "SF" : 499,
    "Denver" : 296
}

# print(fligth_prices["Chicago"]) # Using the key

# -- Get method

# If the key exists → returns its value.
# If the key doesn’t exist → returns the default value given.
# Does not insert the key into the dictionary. (Not modifying the dictionary)

# dict_var.get(<key>, <default_value_if_key_is_absent>)
print(fligth_prices.get("SF", "Not exists")) 
print(fligth_prices.get("Colombo", "Not exists"))

# -- Setdefault method

# If the key exists → returns its value.
# If the key doesn’t exist → adds key: default to the dictionary and returns the default value.
# Modifies the dictionary if the key is missing.(Modifies the dict)

film_directors = {
    "Godfather" : "Francis Ford Coppola",
    "Transformers" : "Micheal Bay",
    "Batman" : "Christoper Noalan"
}

# print(film_directors.get("Tenet", "Does Not exists"))
film_directors.setdefault("Tenet", "Christoper Nolan")
# print(film_directors.get("Tenet", "Does Not exists"))




# -- Adding & Modifying Keys-Values
cricketers = {
    "SL" : ["Kumar", "Sanga", "Mahela"],
    "ENG" : ["Root", "Cook", "Ali"],
    "SA" : ["De Cock", "Kallis", "Makram"]
}

# print(cricketers)

# adding a new key-value pair
cricketers["IND"] = ["Kohli", "Jadeja", "Dravid"]

# print(cricketers)

# modifying a key-value pair
cricketers["IND"] = ["Dhoni", "SKY", "Raina", "Jaiswal"]
# print(cricketers)


# -- Setdefault method

# If the key exists → returns its value.
# If the key doesn’t exist → adds key: default to the dictionary and returns the default value.
# Modifies the dictionary if the key is missing.(Modifies the dict)

film_directors = {
    "Godfather" : "Francis Ford Coppola",
    "Transformers" : "Micheal Bay",
    "Batman" : "Christoper Noalan"
}

# print(film_directors.get("Tenet", "Does Not exists"))
film_directors.setdefault("Tenet", "Christoper Nolan")
# print(film_directors.get("Tenet", "Does Not exists"))


# ----------- Coding Exercises ---------------------------------------------------------------------------------------------------

# Define a length_counts function that accepts a list of strings. 
# The function should return a dictionary where the keys represent
# length and the values represent how many strings have that length.
#
# EXAMPLE:
# sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
# length_counts(sa_countries) => # {6: 1, 9: 2, 7: 2, 4: 1}
# There is 1 string with 6 letters, 2 strings with 9 letters, 
# 2 strings with 7 letters, and 1 string with 4 letters.

def length_counts(a:list) -> dict:
    lens = [len(i) for i in a]
    return  dict(zip(lens, [lens.count(i) for i in lens]))


# Define a to_dictionary function that accepts a list of strings. 
# The function should return a dictionary where the keys are the strings 
# and the values are their original index positions in the list.
#
# EXAMPLE:
# detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
# to_dictionary(detectives) => {'Sherlock Holmes': 0, 'Hercule Poirot': 1, 'Nancy Drew': 2}

def to_dictionary(a:list) -> dict:
    return dict(zip(a, [idx for idx, item in enumerate(a)]))

# -------------------------------------------------------------------------------------------------------------------------------


# --- Pop method
release_dts = {
    "Python" : 1991,
    "Java" : 1995,
    "Ruby" : 1995,
    "C#" : 2000
}

# print(release_dts)


release_dts.pop("Ruby")
# print(release_dts)


# import os

# path = os.curdir
# path = "C:\\Users\\Kisara Fernando\\Desktop/"

# files = os.listdir(path)

# for file in files:
#     if file.endswith(".txt"):
#         print(file)


# ----------- Coding Exercises ---------------------------------------------------------------------------------------------------

# Declare a delete_keys function that accepts two arguments:
# a dictionary and a list of strings. 
# For each string in the list, if the string exists as a dictionary key, 
# delete the key-value pair from the dictionary. 
#
# If the string does not exist as a dictionary key, avoid an error. 
# The return value should be the modified dictionary object.
#
# EXAMPLE:
# my_dict = {
#   "A": 1,
#   "B": 2,
#   "C": 3
# }
#
# strings = ["A", "C"]
# delete_keys(my_dict, strings) => {'B': 2}

def delete_keys(a:dict, b:list) -> dict:
    for i in b:
        if i in a:
            a.pop(i)
        else:
            pass
    return a

# -------------------------------------------------------------------------------------------------------------------------------


# ----- Clear a Dictionary

my_dict = {
  "A": 1,
  "B": 2,
  "C": 3
}

print(my_dict)
my_dict.clear()  # Clean the dictionary as a whole
print(my_dict)


# --- Update method (merging 2 dictionaries)
emp_salaries = {
    "Brandon" : 900000,
    "Guido" : 1000000,
    "Wallace" : 505000
}

emp_salaries_2 = {
    "Hero" : 490000,
    "Enrqiue" : 670000,
}

emp_salaries_3 = {
    "Nina" : 990000,
    "Elle" : 170000,
}

# print(emp_salaries)
emp_salaries.update(emp_salaries_2) # Merging emp_salaries_2 to emp_salaries. print emp_salaries and see
# emp_salaries.update(emp_salaries_2).update(emp_salaries_3) # Can't do this; No Chaining
# print(emp_salaries)

# If in case the second dictionary getting merges has the same key, it will overwrite that key with the new value

# -------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------Dictionary Looping---------------------------------------

chinese_food = {
    "Food_1" : 9.99,
    "Food_2" : 7.99,
    "Food_3" : 2.99
}

for food in chinese_food: #This is a basic way but shouldn't be practiced as it's called an anti-pattern. There are much better ways to do it
    # print(f"The food is {food} and price is {chinese_food[food]}")
    pass

# -- Using items() method
pounds_to_kg = {
    5 : round((5/2.2),2),
    10 : round((10/2),2),
    45 : round((45/2.2),2)
}

for k,v in pounds_to_kg.items():
    # print(f"{k} kg -> {v} lbs")
    pass


# ----------- Coding Exercises ---------------------------------------------------------------------------------------------------
# Declare an invert function that accepts a dictionary object. 
# The function should return a new dictionary where the keys and values from the original dictionary are inverted. 
# Each key should now be a value, and each value should be a key. 
# Assume both the keys and values of the dictionary are immutable.
#
# EXAMPLE:
# my_dict = {
#   "A": "B", 
#   "C": "D",
#   "E": "F"
# }
#
# invert(my_dict) => {'B': 'A', 'D': 'C', 'F': 'E'}

def invert(a:dict) -> dict:
    k_ls = [k for k,v in a.items()]
    v_ls = [v for k,v in a.items()]
    return dict(zip(v_ls, k_ls))



# Declare a count_of_value function that accepts a dictionary and an integer.
# It should return a count of the number of times the integer appears 
# as a value among the dictionary’s values.
#
# EXAMPLE:
# my_dict = { "a" : 5, "b" : 3, "c" : 5 }
#
# count_of_value(my_dict, 5) => 2
# count_of_value(my_dict, 3) => 1

def count_of_value(a:dict, b:str) -> int:
    return [v for k, v in a.items()].count(b)


# Declare a sum_of_values function that accepts a dictionary and a list of strings.
# The dictionary will have keys of strings and values of numbers.
#
# The function should return the sum of values for dictionary 
# keys that are also found in the list.
#
# NOTE: sum is a reserved keyword in Python. Don’t use it as a variable name.
#
# EXAMPLES:
# my_dict = { "a": 5, "b": 3, "c": 10 }
#
# sum_of_values(my_dict, ["a"])            => 5
# sum_of_values(my_dict, ["a", "c"])       => 15
# sum_of_values(my_dict, ["a", "c", "b"])  => 18
# sum_of_values(my_dict, ["z"])            => 0

def sum_of_values(a:dict, b:list) -> int:
    return sum([a[i] for i in b if i in a])


# Declare a common_elements function that accepts a dictionary
# It should return a list with all of the elements that are found
# as both a key and a value in the dictionary
#
# HINT: Use the in operation to check for inclusion in a view or list object
#
# EXAMPLE:
# my_dict = {
#   "A": "K",
#   "B": "D",
#   "C": "A",
#   "D": "Z"
# }
#
# common_elements(my_dict) => ["A", "D"]

def common_elements(a:dict) -> list:
    key_ls = [i for i in a.keys()]
    val_ls = [i for i in a.values()]
    
    return [i for i in key_ls if i in val_ls]


# -------------------------------------------------------------------------------------------------------------------------------


# -- Using **kwargs

def length_of_x(**kwargs):
    xx = kwargs
    return dict(zip([i for i in xx.keys()] , [len(i) for i in xx.values()]))
    # return type(kwargs)

print(length_of_x(hello = "Hello", hello_1 = "Hello_1", hello_2 = "Hello_22"))