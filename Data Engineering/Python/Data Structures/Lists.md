# Lists

Lists are a versatile data structure which are mutable. Can hold any type of data type or even a data structure like a dictionary or tuple. It is a one dimensional array by default but nested lists can be defined.

## Lists Methods

### Changing elements, Extending lists

```python
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
```

### Extending a list with `extend` method

```python
mountains = ["Everest", "K2"]
print(mountains)

mountains.extend(["Adam's Peak", "Makalu", "Bagathale"])
print(mountains)
```

### Inserting Elements

```python
# ----- Inserting an element
plays = ["Hamlet", "Balloth ekka ba"]
print(plays)
plays.insert(len(plays)-1, "No Money No Girls")
print(plays)
plays.insert(2,"Just another drama")
print(plays)
plays.insert(len(plays)+10, "Romeo Juliet")
print(plays)
```

### Removing elements from lists

- `pop()` initially removes last element but an index can be passed to remove a specific value in the list. 
- `del` do the same but you can use slicing to remove multiple elements in the list. 
- `remove()` simply remove the element by it's value name. 
- `clear()` will remove all from the list.

### `Count` Method

```python
car_lot = ["Toyota", "Audi", "Audi", "Benz", "BMW", "BYD", "BYD", "BYD"]

print(car_lot.count("BYD"))
```

### `Zip` Method

```python
breakfast = ["Eggs", "Cereal", "Banana"]
lunch = ["Sushi", "Chicken Teriyaki", "Soup"]
dinner = ["Steak", "Meatballs", "Pasta"]

# Each generator item needs to be unpacked with a seperate variable
for a, b, c in zip(breakfast, lunch, dinner):
    print(f"Breakfast : {a}  |  Lunch : {b}  |  Dinner : {c}")
```

### Understanding nested list looping in list comprehension
```python
meals = [["Eggs", "Cereal", "Banana"]
,["Sushi", "Chicken Teriyaki", "Soup"]
,["Steak", "Meatballs", "Pasta"]]

print([i for subls in meals for i in subls]) 

# Can be understood using this
for subls in meals:
    for i in subls:
        print(i)
```

### Max Split Parameter in SPLIT()

```python
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
```

## Deep Copy vs Shallow Copy

```python
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
```

