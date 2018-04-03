# Compute partial sums in a list comprehension
#not available
values = [2, 3, 4, 5]
total = 0
partial_sums = [total := total + v for v in values]
print("Total:", total)


