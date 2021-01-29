#!/usr/bin/env python3

# HEAPSORT
# Worst Case - O(nlogn)
# Average Case - n/a
import sys
import csv
import time
import math
# import matplotlib.pyplot as plt
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


def DetermineInputSizeList(Arr):
    j = 1
    i = 2
    InputSize = []
    while i < len(Arr):
        InputSize.append(i)
        i = 2**(j)
        j += 1
    return InputSize


def Heapify(Arr, n, i):
    Largest = i
    Left = 2*i + 1  # Why plus 1?
    Right = 2*i + 2  # Why plus 2?

    if (Left < n and Arr[Left] > Arr[i]):
        Largest = Left

    if (Right < n and Arr[Right] > Arr[Largest]):
        Largest = Right

    if Largest != i:
        Arr[i], Arr[Largest] = Arr[Largest], Arr[i]
        Heapify(Arr, n, Largest)


def HeapSort(Arr):
    n = len(Arr)

    for i in range(math.floor(n/2) - 1, -1, -1):
        Heapify(Arr, n, i)

    for i in range(n-1, 0, -1):  # Decrement from last element to second last element
        Arr[i], Arr[0] = Arr[0], Arr[i]
        Heapify(Arr, i, 0)


def TimeAlgorithm(Arr, InputSize):
    ExecTime = []
    for i in InputSize:
        StartTime = time.time()
        HeapSort(Arr[0:i])
        ExecTime.append(time.time() - StartTime)
    return ExecTime


def Graph(InputSize, ExecTime):
    plt.plot(InputSize, ExecTime)
    plt.ylabel('Runtime (s)')
    plt.xlabel('Input Size (logn)')
    plt.title('Algorithm RunTime of HEAP SORT as a Function of Input Size')
    plt.show()


if Submission:  # Submission flag
    print(f'Running HeapSort on Input Size of {len(Arr)}')

    StartTime = time.time()

    HeapSort(Arr)

    Total = time.time() - StartTime

    # Print the sorted array
    for i in Arr:
        Data[i].insert(0, i)
        print(Data[i])
    # Print the status of the dataset
    SortStatus = all(Arr[i] <= Arr[i+1]
                     for i in range(len(Arr)-1))  # Check if Sorted
    print(f'Is the Dataset Sorted: {SortStatus}')
    print(Total)
else:
    print(f'Running HeapSort on Input Size of {len(Arr)}')
    InputSize = DetermineInputSizeList(Arr)
    ExecTime = TimeAlgorithm(Arr, InputSize)
    Graph(InputSize, ExecTime)
