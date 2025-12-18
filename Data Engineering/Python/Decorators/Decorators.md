# Decorators

In higher order functions we pass a function into a function for invoking it. Imagine if we have a higher order function set like below.

```python
def be_nice(fn: str) -> Callable:
    def inner():
        print("Nice to meet you!")
        fn()
        print("It was my pleasure executing your function!\n")

    return inner


if __name__ == namespace_other:

    def complex_business_logic() -> str:
        print("Complex logic eh!!")

    be_nice(complex_business_logic)()
```

Here we'd have to invoke `complex_business_logic` function inside `be_nice` function. 

But what if we can use the `be_nice` function sort of as a __template__ and use that without complicating the . That's exactly what ___decorators___ lets' us achieve. This is known as `"syntactic sugar"` in programming which are extra syntax that makes code easier to read, write and understand.

The same code but with decorators:

```python
def be_nice(fn: str) -> Callable:
    def inner():
        print("Nice to meet you!")
        fn()
        print("It was my pleasure executing your function!\n")

    return inner

if __name__ == namespace_main:

    @be_nice
    def complex_business_logic() -> str:
        print("Complex logic eh!!")

    complex_business_logic()

    @be_nice
    def another_fancy_function():
        print("Goo goo gaga")

    another_fancy_function()
```

## Passing arguments (Positional/ Keyword)

When passing arguments to functions, the following can be done:

```python
def be_nice(fn: Callable) -> Callable:
    def inner(*args, **kwargs):
        print("Nice to meet you!")
        fn(*args, **kwargs)
        print("It was my pleasure executing your function!\n")

    return inner


if __name__ == namespace_main:
    @be_nice
    def complex_business_logic(stakeholder: str) -> str:
        print("Complex logic eh {}!!".format(stakeholder))

    complex_business_logic("Boris")
```

Since the decorators should serve a utilitary purpose, we have to get the positional arguments as "args" and keyword arguments as "kwargs"