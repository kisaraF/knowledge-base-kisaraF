# Function Annotations in Python

* Python is dynamically typed but still the data types can be defined as below:

```python
def simple_multiplier(word:str, num:int) -> str:
    return word * num

print(simple_multiplier("Kisara", 3))
```

## Why use this:
* There are libraries kind of tools that supports static typing before running the code to make sure errors are not there, etc. (mypy, pytype, pyright)
* Better code readability. Easy for refactoring
* Provides a good function for static typing language learning

## Use of Library `typing`

Typing is a library in Python which has all the types of data structures which can be used to define function annotations. For example, have a look at the below higher order function.

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