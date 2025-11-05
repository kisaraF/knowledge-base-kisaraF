# The idea here is you get a function as a return value
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