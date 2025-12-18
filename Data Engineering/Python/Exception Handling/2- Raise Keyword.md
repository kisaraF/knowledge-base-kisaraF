# Usage of Raise keyword

Raise keyword can be used to raise an exception in a targeted way. Pay attention to the below,

```python
def add_positive_numbers(a,b):
    try:
        if a <0 or b 0:
            raise ValueError("One or both are negative")
        return a + b
    except ValueError as err:
        return f"Cught the ValueError: {err}"
```

