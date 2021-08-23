# This program is the main sorting program.
# It sorts a set of data using different algorithms and times the algorithm.
# Arguments:
# Command line:
#   1. A json file containing the list of data to sort
# In program:
#   2. The sorting algorithm to use
#   3. Number of times to sort using the algorithm
# Only argument 1 will be given on the command line.
# Arguments 2 and 3 will be given in the program itself.

import sys
import json
import itertools

# This function prompts the user for the sorting algorithm to use, and the number of times to sort.
# Parameters: a dictionary with each key being the name of a sorting algorithm (string) and each associated value being an object containing the actual algorithm (function/object).
# Returns a tuple containing the sorting algorithm to use and the number of times.
def promptForArgs(algorithms):
    print("Which sorting algorithm?: \n")
    
    print("Options:")
    for i, name in zip(itertools.count(start=1), algorithms):
        print(f"{i}. {name}")
    
    userResponse = input("\n")

promptForArgs({'lol': object()})

if len(sys.argv) < 2:
    raise RuntimeError("Not enough arguments provided.")
dataFile = sys.argv[1]
with open(dataFile, 'r') as file:
    data = json.load(file)

