#!/usr/bin/env python3

# Counting Sort
# Worst Case - Theta(k + n)
# Average Case - Theta(k + n)
import sys
import csv
import time
import math
import matplotlib.pyplot as plt
import random

sys.setrecursionlimit(10**9)

Submission = True
InputFile = sys.argv[1]

# Storing Data as nested list, where key is element 0 of nested list
Data = dict()
with open(InputFile + '.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        Data[int(row[0])] = list()
        for i in row[1:]:
            Data[int(row[0])].append(i)
Arr = list(Data)

max_value = max(Arr)


def DetermineInputSizeList(Data):
    j = 1
    i = 2
    InputSize = []
    while i < len(Arr):
        InputSize.append(i)
        i = 2**(j)
        j += 1
    return InputSize


def CountingSort(Data, max_value):
    max_value = max_value + 1
    count = [0] * max_value

    item = 0
    for item in Data:
        count[item] += 1

    j = 0
    for value in range(max_value):
        for counter in range(count[value]):
            Data[j] = value
            j += 1

    return Data


def TimeAlgorithm(Data, InputSize, max_value):
    ExecTime = []
    for i in InputSize:
        StartTime = time.time()
        CountingSort(Data, max_value)
        ExecTime.append(time.time() - StartTime)
    return ExecTime


def Graph(InputSize, ExecTime):
    plt.plot(InputSize, ExecTime)
    plt.ylabel('Execution Time (s)')
    plt.xlabel('Input Size (n)')
    plt.title('Algorithm RunTime as a Function of Input Size')
    plt.show()


if Submission:  # Submission flag
    print(
        f'Running Counting Sort on Input Size of {len(Arr)}. Please be patient for large n inputs.')
    CountingSort(Arr, max_value)
    # Print the sorted array
    for i in Arr:
        Data[i].insert(0, i)
        print(Data[i])
    # Print the status of the dataset
    SortStatus = all(Arr[i] <= Arr[i+1]
                     for i in range(len(Arr)-1))  # Check if Sorted
    print(f'Is the Dataset Sorted: {SortStatus}')
else:
    print(f'Running Counting Sort on Input Size of {len(Arr)}')
    InputSize = DetermineInputSizeList(Arr)
    print(InputSize)
    ExecTime = TimeAlgorithm(Arr, InputSize, max_value)
    Graph(InputSize, ExecTime)
