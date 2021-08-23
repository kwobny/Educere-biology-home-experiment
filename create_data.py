# This program creates a list of floating point numbers and writes the list to a file in json format.
# Arguments:
# 1. The lower bound (inclusive)
# 2. The upper bound (exclusive)
# 3. The number of numbers to generate
# 4. The name of the file to save to.

import sys
import random
import json

# Setup variables
if len(sys.argv) < 5:
    raise RuntimeError("Not enough arguments provided.")
lower = float(sys.argv[1])
upper = float(sys.argv[2])
numCount = int(float(sys.argv[3]))
filename = str(sys.argv[4])

# Generate numbers
numRange = upper - lower
numbers = [round(random.random()*numRange + lower, 2) for _ in range(numCount)]

# Write data to file
with open(filename, 'w', encoding="utf-8") as file:
    json.dump(numbers, file, ensure_ascii=False)
