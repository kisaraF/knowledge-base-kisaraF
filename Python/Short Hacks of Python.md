# Short Hacks of Python

## Split a non-delimitered string in Python using list (string) 

```
def three_number_sum(a:str) -> int:
    new_ls = list(a)
    sum_ls = int(new_ls[0]) + int(new_ls[1]) + int(new_ls[-1])
    return sum_ls
```

* This will convert the string into a list without a delimiter, character by character