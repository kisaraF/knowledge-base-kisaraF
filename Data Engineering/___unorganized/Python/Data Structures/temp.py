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