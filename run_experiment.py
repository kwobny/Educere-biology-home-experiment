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
import os
import timeit
import functools
import sorting

def clearScreen():
    os.system('clear')

# This function prompts the user for the sorting algorithm to use, and the number of times to sort.
# Arguments: A list of tuples. The tuple's first element should be the name (string) of the sorting algorithm. The second element should be the associated sorting function/object
# Returns a tuple containing the sorting algorithm to use (function/object) and the number of times (in that order).
def promptForArgs(algorithms):
    print("Which sorting algorithm?: \n")
    
    print("Options:")
    for i, (name, _) in enumerate(algorithms):
        print(f"{i+1}. {name}")
    
    userResponse = input("\nType the number corresponding to an algorithm:\n")
    while True:
        try:
            algToUse = algorithms[int(userResponse)-1][1]
            break
        except (IndexError, ValueError) as err:
            print("Invalid input. Error:")
            print(err)
            userResponse = input("\nTry again:\n")
    
    clearScreen()
    userResponse = input("How many trials?:\n")
    while True:
        try:
            numberOfTrials = int(userResponse)
        except ValueError:
            userResponse = input("Input is not a number. Try again:\n")
            continue
        if numberOfTrials < 0:
            userResponse = input("Input cannot be less than 0. Try again:\n")
        else:
            break
    
    return algToUse, numberOfTrials

# This function executes the actual time test / experiment.
# Arguments:
# 1. A reference to the data (list)
# 2. Sorting function to use (should have one argument, which should be a list to sort)
# 3. Number of trials
# 4. Amount of times to run per trial.
# The function repeats the test <trials> number of times, and each time, it measures the total amount of time taken to execute the sorting <repsPerTrial> times.
# Yields the times taken for each trial of sorting to complete.
def executeExperiment(data, sortingFunction, trials, repsPerTrial = 1):
    callback = functools.partial(sortingFunction, data)
    for i in range(trials):
        yield timeit.timeit(callback, number=repsPerTrial)

# This function prints the results of the trials.
# Arguments: a list of times taken to sort, or an iterator returning times taken to sort.
def printResults(times):
    for i, timeOfTrial in enumerate(times):
        print(f"Trial {i+1}: {'%.5g' % timeOfTrial} seconds")

sortingAlgorithms = [
    ("Merge sort", sorting.merge),
    ("Quicksort", sorting.quick),
    ("Heapsort", sorting.minheap),
    ("Insertion sort", sorting.selection),
    ("Bubble sort", sorting.bubble),
]

if len(sys.argv) < 2:
    raise RuntimeError("Not enough arguments provided.")
dataFile = sys.argv[1]
with open(dataFile, 'r') as file:
    data = json.load(file)
print(f"There are {len(data)} data entries in the loaded dataset.\n")

while True:
    algorithmToUse, numberOfTrials = promptForArgs(sortingAlgorithms)

    clearScreen()
    print("Running trials...\n")
    trials = executeExperiment(data, algorithmToUse, numberOfTrials)
    printResults(trials)
    print("\nDone")

    userInput = input("\nType q to exit the program. Type any other key (or none) to restart the program.\n")
    if userInput == 'q':
        break
    else:
        clearScreen()
