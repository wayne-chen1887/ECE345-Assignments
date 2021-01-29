# !/usr/bin/env python3

# Counting Sort
# Worst Case - Theta(k + n)
# Average Case - Theta(k + n)
import sys
import csv
import time
import math
import matplotlib.pyplot as plt


sys.setrecursionlimit(10**9)
sysarg = False

if sysarg:
    InputFile = sys.argv[0]
else:
    InputFile = 'a1.large'


Data = []
with open(InputFile + '.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        Data.append(int(row[0]))

max_value = max(Data)


def DetermineInputSizeList(Data, buckets):
    InputSize = []
    i = int(len(Data)/buckets)
    for idx, value in enumerate(Data):
        if idx % i == 0 and idx != 0:
            InputSize.append(idx)
        if idx == len(Data) - 1:
            InputSize.append(idx)
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


InputSize = DetermineInputSizeList(Data, 10)
ExecTime = TimeAlgorithm(Data, InputSize, max_value)
Graph(InputSize, ExecTime)
