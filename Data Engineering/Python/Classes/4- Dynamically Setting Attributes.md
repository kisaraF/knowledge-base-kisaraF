# Dynamically Passing Attributes to Classes

## SETATTR & GETATTR

When you need to pass dynamic attributes to a class (which is not define for instantiation), you can use `setattr` to add those attributes. As well as `getattr` to get those attributes. And the same class could have different attributes and we wouldn't need to worry about setting attributes for instantiation manually when we can use setattr. And we can change attribute values like we normally do too.

```python
stats = {
    "name" : "BBQ Chicken",
    "price" : 19.9,
    "size" : "Extra Large",
    "ingredients" : ["Chicken", "Onions", "BBQ Sauce"]
}

class Pizza():
    def __init__(self, stats):
        for key, val in stats.items():
            setattr(self, key, val)


bbq = Pizza(stats)

print(bbq.size) # Extra Large
bbq.size = "Fatass Pizza"
print(bbq.size) # Fatass Pizza
print(bbq.price) # 19.9
print(bbq.ingredients)

for attr in ["price", "radius", "name", "size"]:
    print(getattr(bbq, attr, "Unknown"))
    # 19.9
    # Uknown
    # BBQ Chicken
    # Fatass Pizza
```

So when you have things like,
- API responses with evolving fields
```python
class ApiResponse:
    pass

data = {
    "id": 123,
    "status": "ok",
    "retry_after": 30
}

resp = ApiResponse()
for key, value in data.items():
    setattr(resp, key, value)

resp.status
resp.retry_after

```
- Configuration Objects like yaml

this method is super useful.

## HASATTR & DELATTR

`hasattr` can be used to see if a given attribute exists in an object

```python
stats = {
    "name" : "BBQ Chicken",
    "price" : 19.9,
    "size" : "Extra Large",
    "ingredients" : ["Chicken", "Onions", "BBQ Sauce"]
}

class Pizza():
    def __init__(self, stats):
        for key, val in stats.items():
            setattr(self, key, val)


bbq = Pizza(stats)

for stat in ["size", "spiciness"]:
    if hasattr(bbq, stat):
        print(getattr(bbq, stat))
```

`delattr` can delete the attribute

```python
stats = {
    "name" : "BBQ Chicken",
    "price" : 19.9,
    "size" : "Extra Large",
    "ingredients" : ["Chicken", "Onions", "BBQ Sauce"]
}

class Pizza():
    def __init__(self, stats):
        for key, val in stats.items():
            setattr(self, key, val)


bbq = Pizza(stats)

for stat in ["size", "spiciness"]:
    if hasattr(bbq, stat):
        delttr(bbq, stat)
```