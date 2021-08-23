# This program creates a list of floating point numbers and writes the list to a file in json format.
# Arguments:
# 1. The lower bound (inclusive)
# 2. The upper bound (exclusive)
# 3. The number of numbers to generate
# 4. The name of the file to save to.

import random
import json

lower = 0
upper = 0
numCount = 0
filename = ""

# Generate numbers
numRange = upper - lower
numbers = [(random.random()*numRange + lower) for _ in range(numCount)]

# Write data to file
with open(filename, 'w', encoding="utf-8") as file:
    json.dumps(numbers, file, ensure_ascii=False)
