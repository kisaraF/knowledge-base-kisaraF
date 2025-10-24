# Higher Order Functions

A function that accepts another funtion as an argument is a higher order function.

```
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def calculate(func, a, b):
    return func(a,b)
```

```
print(calculate(add, 3, 4))  -> // 7
```

```
print(calculate(subtract, 4, 1))  -> // 3
```