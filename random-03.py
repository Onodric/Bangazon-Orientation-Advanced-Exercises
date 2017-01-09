#--------|---------|---------|---------|---------|---------|---------|---------
# Squared Randoms

## Instructions

# 1. Using the `random` module and the `range` method, generate a list of 20 random numbers between 0 and 49.
# 2. With the resulting list, use a list comprehension to build a new list that contains each number squared. For example, if the original list is `[2, 5]`, the final list will be `[4, 25]`.

import random
seeder = range(20)
randoms = [random.randint(0,49) for seed in seeder]
print(randoms)
square_randoms = [seed*seed for seed in randoms]
print(square_randoms)
