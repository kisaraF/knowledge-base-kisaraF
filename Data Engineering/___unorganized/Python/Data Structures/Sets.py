# Mutable, unordered data structure that prohibits duplicate values

myset = {1,1,3,5,2,51,1,5} # removes duplicates
print(myset)


#----- Creating an empty set
empty_set = set()


# --- Mutating by adding new (using Add and Update)
dc_heros = {
  "Batman",
  "Superman",
  "Wonder Woman"
} 

print(dc_heros)

dc_heros.add("Aquaman") # Adds individual elements
print(dc_heros)

dc_heros.update(["Flash", "Green Lantern"]) # Adds multiple passed as a list
print(dc_heros)


# ----- Remove and Discard Methods
dc_heros = {
  "Batman",
  "Superman",
  "Wonder Woman",
  "Flash",
  "Lantern"
} 

print(dc_heros)

dc_heros.remove("Superman") 
print(dc_heros)

dc_heros.discard("Manhunter") # Won't throw an error if nothing like the given value exists unlike `remove` method


# ------ Intersection Method 
candy_bars = {"milky way", "snickers", "100 grand"}
sweets = {"sour patch kids", "reese pieces", "snickers"}

print(candy_bars.intersection(sweets))
print(candy_bars & sweets) # Shortcut


# ------ Union Method
candy_bars = {"milky way", "snickers", "100 grand"}
sweets = {"sour patch kids", "reese pieces", "snickers"}

print(candy_bars.union(sweets))
print(candy_bars | sweets) # Shortcut


# ------- Difference between sets
candy_bars = {"milky way", "snickers", "100 grand"}
sweets = {"sour patch kids", "reese pieces", "snickers"}

print(candy_bars.difference(sweets)) #everything in `candy_bars` except for intersection and `sweets`
print(candy_bars - sweets)

print(sweets.difference(candy_bars)) #everything in `sweets` except for intersection and `candy_bars`
print(sweets - candy_bars)


# ------ Symmetric Difference between sets
candy_bars = {"milky way", "snickers", "100 grand"}
sweets = {"sour patch kids", "reese pieces", "snickers"}

print(candy_bars.symmetric_difference(sweets)) # Everything in both sets except for the intersection
print(candy_bars ^ sweets) #sortcut


# ------ `issubset` & `issuperset` methods
a = {1,2,3,4,5}
b = set([i for i in range(1,16)])

print(a.issubset(b))
print(b.issuperset(a))
print(a < b)
print(a <= b)


# ------- Frozen Set
# Makes an immutable set using `frozenset()`. Can't mutate with methods like add/ update/ remove/ discard
mr_freeze = frozenset(["Bailey", "Molly", "Ginger", "Naughty", "Ginger"])
print(mr_freeze)