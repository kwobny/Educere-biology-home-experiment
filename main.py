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
# Parameters: A list of tuples. The tuple's first element should be the name (string) of the sorting algorithm. The second element should be the associated sorting function/object
# Returns a tuple containing the sorting algorithm to use (function/object) and the number of times.
def promptForArgs(algorithms):
    print("Which sorting algorithm?: \n")
    
    print("Options:")
    for i, (name, _) in enumerate(algorithms):
        print(f"{i}. {name}")
    
    userResponse = input("\n")
    while True:
        try:
            algToUse = algorithms[int(userResponse)][1]
        except (IndexError, ValueError) as err:
            print("Invalid input. Error:")
            print(err)
            userResponse = input("\nTry again:\n")
            continue;
        break;

promptForArgs([('lol', object())])

if len(sys.argv) < 2:
    raise RuntimeError("Not enough arguments provided.")
dataFile = sys.argv[1]
with open(dataFile, 'r') as file:
    data = json.load(file)

