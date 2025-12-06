# Higher Order Functions

A function that accepts another funtion as an argument is a higher order function.

```python
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def calculate(func, a, b):
    return func(a,b)
```

```python
print(calculate(add, 3, 4))  #-> // 7
```

```python
print(calculate(subtract, 4, 1))  #-> // 3
```

## Nested Higher Order Functions

The idea here is you get a function as a return value

```python
from typing import Callable

def calculator(op) -> Callable:
    def add(a , b) -> int:
        return a + b

    def sub(a, b) -> int:
        return a - b

    if op == 'add':
        return add
    elif op == 'sub':
        return sub

print(calculator('sub')(5,2))
```