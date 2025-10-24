workers = ["Pam", "Oscar", "Charles", "Leclerc", "Max", "Isaac", "Carlos"]

print(workers)

# Changing last 3 workers names can be done using index based list slicing

workers[-3:] = ["Verstappen", "Luis", "Sainz"]
print(workers)


# Can expand the list too
workers[-3:] = ["Verstappen", "Luis", "Sainz", "Hadjar", "Alonso"]
print(workers)

# Or even remove some
workers[-3:] = ["Sainz"]
print(workers)

workers[-3:-1] = []
print(workers)


# ---------- A coding exercise that can be done with list comprehensions and with lambda funcs with map & filter ----------

# Declare a length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.
#
# EXAMPLES
# length_match(["cat", "dog", "kangaroo", "mouse"], 3))  => 2
# length_match(["cat", "dog", "kangaroo", "mouse"], 5))  => 1
# length_match(["cat", "dog", "kangaroo", "mouse"], 4))  => 0
# length_match([], 5))                                   => 0

# def length_match(a:list, b:int) -> int:
#     return len(list(filter(lambda x: len(x) == b,a)))
    #  return len([i for i in a if len(i) == b])

# --------------------------------------------------------------------------------------------------------------

powerball_nums = [4,8,15,16,23,42]

squared_powerball_nums = [i**2 for i in powerball_nums]

print(powerball_nums)
print(squared_powerball_nums)


# ---- Extending a list
mountains = ["Everest", "K2"]
print(mountains)

mountains.extend(["Adam's Peak", "Makalu", "Bagathale"])
print(mountains)


# ----- Inserting an element
plays = ["Hamlet", "Balloth ekka ba"]
print(plays)
plays.insert(len(plays)-1, "No Money No Girls")
print(plays)
plays.insert(2,"Just another drama")
print(plays)
plays.insert(len(plays)+10, "Romeo Juliet")
print(plays)


# ---------- Removing elements from lists -------------
# pop() initially removes last element but an index can be passed to remove a specific value in the list. 
# del do the same but you can use slicing to remove multiple elements in the list. 
# remove() simply remove the element by it's value name. 
# clear() will remove all from the list.




# ----------- Another Coding Exercise ----------
def delete_all(a:list, b:str) -> list:
    if b in a:
        a = list(set(a))
        a.remove(b)
        return a
    else:
        return a
    
# print(delete_all([1, 3, 5], 3)) 
# print(delete_all([5, 3, 5], 5))
# print(delete_all([4, 4, 4], 4))
# print(delete_all([4, 4, 4], 6))


def push_or_pop(a:list) -> list:
    just = []
    for i in a:
        if i > 5:
            just.append(i)
        else:
            just.pop()
    
    return just

# print(push_or_pop([10]))
# print(push_or_pop([10, 4]))
# print(push_or_pop([10, 20, 30]))
# print(push_or_pop([10, 20, 2, 30]))


#----------------------------- List Methods -----------------------------

# ----- Count
car_lot = ["Toyota", "Audi", "Audi", "Benz", "BMW", "BYD", "BYD", "BYD"]

# print(car_lot.count("BYD"))



# ----- Zip
breakfast = ["Eggs", "Cereal", "Banana"]
lunch = ["Sushi", "Chicken Teriyaki", "Soup"]
dinner = ["Steak", "Meatballs", "Pasta"]

# Each generator item needs to be unpacked with a seperate variable
for a, b, c in zip(breakfast, lunch, dinner):
    print(f"Breakfast : {a}  |  Lunch : {b}  |  Dinner : {c}")
    
# -------  Understanding nested list looping in list comprehension
meals = [["Eggs", "Cereal", "Banana"]
,["Sushi", "Chicken Teriyaki", "Soup"]
,["Steak", "Meatballs", "Pasta"]]

print([i for subls in meals for i in subls]) 

# Can be understood using this
for subls in meals:
    for i in subls:
        print(i)

#------ Another coding exercises for looping nested lists in comprehensions (good to understand conditions with if)

# Define a fancy_concatenate function that accepts a list of lists of strings
# The function should return a concatenated string
# The strings in a list should only be concatenated if the length of the list is 3
#
# EXAMPLES
# fancy_concatenate([["A", "B", "C"]])                        => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]])       => "ABCDEF"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]])  => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E"]])            => "ABC"
# fancy_concatenate([["A", "B"], ["C", "D"]])                 => ""

def fancy_concatenate(a:list) -> str:
    return "".join([i for subi in a if len(subi) == 3 for i in subi])


# ----------------------- Deep Copy vs Shallow Copy -------------------------------------

import copy

ls = [1, [2, 3], 4]

# --- Shallow Copy
ls_sp = copy.copy(ls)

ls_sp[-1] = 28 # Changing the 1 Dimensional data of the copy list won't affect it's corresponding original list
print(ls)
print(ls_sp)

print("\n")

ls_sp[1][0] = 34 # Changing the 2 Dimensional data of the copy list will affect it's corresponding original list
print(ls)
print(ls_sp)

print("\n")

# --- Deep Copy
ls = [1, [2, 3], 4]

ls_sp = copy.deepcopy(ls)

ls_sp[1][0] = 34 # Deep copies create independent list item copies unlike the shallow copying
print(ls)
print(ls_sp)


# -----------------------------  Max Split Parameter in SPLIT()  ---------------------------
text = "apple,banana,orange,grape"

# No maxsplit (or maxsplit=-1) - splits at all commas
result_all = text.split(',')
print(f"Split all: {result_all}")

# maxsplit=1 - splits only at the first comma
result_one_split = text.split(',', 1)
print(f"Split once: {result_one_split}")

# maxsplit=2 - splits at the first two commas
result_two_splits = text.split(',', 2)
print(f"Split twice: {result_two_splits}")