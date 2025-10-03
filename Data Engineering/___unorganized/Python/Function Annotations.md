# Function Annotations in Python

* Python is dynamically typed but still the data types can be defined as below:

```
def simple_multiplier(word:str, num:int) -> str:
    return word * num

print(simple_multiplier("Kisara", 3))
```

## Why use this:
* There are libraries kind of tools that supports static typing before running the code to make sure errors are not there, etc. (mypy, pytype, pyright)
* Better code readability. Easy for refactoring
* Provides a good function for static typing language learning