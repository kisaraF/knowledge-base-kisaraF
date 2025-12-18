# Optional Blocks

`Else` and `Finally` are optional blocks. Their use cases are as below.

## `else` block

When the `try` block has run without an error the `else` block will run

```python
x = 5
try:
    print(x + 10)
except NameError:
    print("No variable name was given")
else:
    print("Everything ran successfully")
```

## `finally` block

This will run regardless an exception was caught or not

```python
try:
    print(x + 10)
except NameError:
    print("No variable name was given")
else:
    print("Everything ran successfully")
finally:
    print("Whatever happens above this will definetly happen")
```