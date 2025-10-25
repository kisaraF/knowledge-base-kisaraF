mystery = {

  "a": 2

}



mystery.setdefault("A", 5)

mystery.setdefault("a", 10)

mystery.setdefault("B", 30)

mystery.setdefault("B", 40)

print(mystery) 

text = "apple,banana,orange,grape"

# No maxsplit (or maxsplit=-1) - splits at all commas
result_all = text.split(',')
print(f"Split all: {result_all}")

# maxsplit=1 - splits only at the first comma
result_one_split = text.split(',', 1)
print(f"Split once: {result_one_split}")

# maxsplit=2 - splits at the first two commas
result_two_splits = text.split(',', 2)
print(f"Split twice: {result_two_splits}")

