# !/usr/bin/env python3

# QUICKSORT
# Worst Case - Theta(n^2)
# Average Case - Theta(nlogn)
import sys
import csv
import time
import math
import matplotlib.pyplot as plt

sys.setrecursionlimit(10**9)
sysarg = False
test = True

if sysarg:
    InputFile = sys.argv[0]
else:
    InputFile = 'a1.large'

# Storing Data as nested list, where key is element 0 of nested list
Data = []
with open(InputFile + '.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        Data.append(int(row[0]))


def DetermineInputSizeList(Data, buckets):
    InputSize = []
    i = int(len(Data)/buckets)
    for idx, value in enumerate(Data):
        if idx % i == 0 and idx != 0:
            InputSize.append(idx)
        if idx == len(Data) - 1:
            InputSize.append(idx)
    return InputSize


def Partition(Data, p, r):
    pivot = Data[r]

    i = p - 1

    for j in range(p, r):
        if Data[j] <= pivot:
            i += 1
            Data[i], Data[j] = Data[j], Data[i]
    Data[i+1], Data[r] = Data[r], Data[i+1]  # Swap Elements
    return (i+1)  # Return element q


def QuickSort(Data, p, r):

    if (p < r):
        q = Partition(Data, p, r)
        QuickSort(Data, p, q - 1)
        QuickSort(Data, q + 1, r)


def TimeAlgorithm(Data, InputSize, p, r):
    ExecTime = []
    for i in InputSize:
        StartTime = time.time()
        QuickSort(Data[0:i], p, i-1)
        ExecTime.append(time.time() - StartTime)
    return ExecTime


def Graph(InputSize, ExecTime):
    plt.plot(InputSize, ExecTime)
    plt.ylabel('Execution Time (s)')
    plt.xlabel('Input Size (n)')
    plt.title('Algorithm RunTime as a Function of Input Size')
    plt.show()


p = 0
r = len(Data) - 1

if test:
    QuickSort(Data, p, r)
    SortStatus = all(Data[i] <= Data[i+1]
                     for i in range(len(Data)-1))  # Check if Sorted
    print(f'Is the Dataset Sorted: {SortStatus}')
else:
    print(f'Running QuickSort on Input Size of {len(dataset)}')
    InputSize = DetermineInputSizeList(dataset, 5)
    ExecTime = TimeAlgorithm(dataset, InputSize, p, r)
    Graph(InputSize, ExecTime)
