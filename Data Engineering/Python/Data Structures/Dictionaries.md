# Dictionaries

Dictionaries are mutable data structure which can be used to store `key - value` pairs.

Extremely useful to store data where a reference pointer is required. So that the value can be referred simply just by referring to the key.

## Methods, Attributes, Use Cases

The following will depict different methods, use cases of Dictionaries in Python

### Accesing a dictionary value

```python
fligth_prices = {
    "Chicago": 199,
    "SF" : 499,
    "Denver" : 296
}

print(fligth_prices["Chicago"]) # Using the key
```

### `Get` method

- If the key __exists__ → returns its value.
- If the key __doesn’t__ exist → returns the default value given.
- Does not insert the key into the dictionary. (__Not modifying__ the dictionary)

***Mental Model:***
`dict_var.get(<key>, <default_value_if_key_is_absent>)`

```python
fligth_prices = {
    "Chicago": 199,
    "SF" : 499,
    "Denver" : 296
}

print(fligth_prices.get("SF", "Not exists")) 
print(fligth_prices.get("Colombo", "Not exists"))
```

### `Setdefault` method

- If the key __exists__ → returns its value.
- If the key __doesn’t__ exist → __adds__ key: default to the dictionary and returns the default value.
- Modifies the dictionary if the key is missing.(__Modifies__ the dict)

```python
film_directors = {
    "Godfather" : "Francis Ford Coppola",
    "Transformers" : "Micheal Bay",
    "Batman" : "Christoper Noalan"
}

print(film_directors.get("Tenet", "Does Not exists"))
film_directors.setdefault("Tenet", "Christoper Nolan")
print(film_directors.get("Tenet", "Does Not exists"))
```

### Adding & Modifying Keys-Values

```python
cricketers = {
    "SL" : ["Kumar", "Sanga", "Mahela"],
    "ENG" : ["Root", "Cook", "Ali"],
    "SA" : ["De Cock", "Kallis", "Makram"]
}

print(cricketers)

# adding a new key-value pair
cricketers["IND"] = ["Kohli", "Jadeja", "Dravid"]

print(cricketers)

# modifying a key-value pair
cricketers["IND"] = ["Dhoni", "SKY", "Raina", "Jaiswal"]
print(cricketers)
```

### `Pop` method

Remove a key value pair by using the key

```python
release_dts = {
    "Python" : 1991,
    "Java" : 1995,
    "Ruby" : 1995,
    "C#" : 2000
}

print(release_dts)
release_dts.pop("Ruby")
print(release_dts)
```

### Clear a Dictionary

```python
my_dict = {
  "A": 1,
  "B": 2,
  "C": 3
}

print(my_dict)
my_dict.clear()  # Clean the dictionary as a whole
print(my_dict)
```

### Update method (merging 2 dictionaries)

Only 2 dictionaries at a time

```python
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

print(emp_salaries)
emp_salaries.update(emp_salaries_2) # Merging emp_salaries_2 to emp_salaries. print emp_salaries and see
emp_salaries.update(emp_salaries_2).update(emp_salaries_3) # Can't do this; No Chaining
print(emp_salaries)
```

If in case the second dictionary getting merges has the same key, it will overwrite that key with the new value

### Sorted Method

```python
salaries={
    "Executive Assistant" : 20,
    "CEO" : 100,
    "Janitor" : 4,
    "CFO" : 96
}

print(salaries)
print(sorted(salaries)) # Returns a sorted keys list
print(sorted(salaries.items())) # Returns a sorted dictionary
```

### Using `**kwargs` 

- *args sends a tuple whereas **kwargs sends a dict

```python
def length_of_x(**kwargs):
    xx = kwargs #kwargs=xx here is the dictionary
    return dict(zip([i for i in xx.keys()] , [len(i) for i in xx.values()])) #This just gets the length of value of each key

print(length_of_x(hello = "Hello", hello_1 = "Hello_1", hello_2 = "Hello_22")) #passing as a dictionary

# Run the following for a better understanding:
def args_kwargs(a, *args, **kwargs):
    reg = a
    print(f'{a} is {type(a)}')

    xx = args
    print(f'{xx} is {type(xx)}')

    xxx = kwargs
    print(f'{xxx} is {type(xxx)}')

args_kwargs("Hello", "Honey", "Bunney", "You are my", "Pumpkin Pumpkin!", who= "You", what="Mine", really=True)
```

## Dictionary Looping

### Anti Patterns

Anti patterns are not the most optimal way to do it even though the approach works.

```python
chinese_food = {
    "Food_1" : 9.99,
    "Food_2" : 7.99,
    "Food_3" : 2.99
}

for food in chinese_food:
    print(f"The food is {food} and price is {chinese_food[food]}")
    pass
```

### Using `items()` method

```python
pounds_to_kg = {
    5 : round((5/2.2),2),
    10 : round((10/2),2),
    45 : round((45/2.2),2)
}

for k,v in pounds_to_kg.items():
    print(f"{k} kg -> {v} lbs")
    pass
```

- What actually happens as `k, v in dict.items()` is that when you do `items()` method it gives dictionary elements as tuples
- Then k, v or any desired variable will unpack them