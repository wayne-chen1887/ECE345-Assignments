# !/usr/bin/env python3

# Heap Sort
# Worst Case - O(nlogn)
# Average Case - n/a
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
    InputFile = 'a1.small'


Data = []
with open(InputFile + '.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        Data.append(int(row[0]))


def Heapify(Data, i):
    Left = 2*i + 1  # Why plus 1?
    Right = 2*i + 2  # Why plus 2?
    # print(Left, Right, len(Data))
    # print(Left, Right, len(Data), i)
    if (Left < len(Data) and Data[Left-1] > Data[i]):
        Largest = Left
    else:
        Largest = i
    # print(Largest)
    # print(Right <= len(Data))
    # print(Data[Largest])
    if (Right < len(Data) and Data[Right-1] > Data[Largest]):
        Largest = Right

    if (Largest != i):
        Data[i], Data[Largest] = Data[Largest], Data[i]
        Heapify(Data, Largest)


def BuildHeap(Data):
    # Decrement from middle node to root node
    for i in range(math.floor(len(Data)/2) - 1, -1, -1):
        Heapify(Data, i)


def HeapSort(Data):
    BuildHeap(Data)
    # count = len(Data) - 1
    for i in range(len(Data)-1, 0, -1):  # Decrement from last element to second last element
        Data[i], Data[0] = Data[0], Data[i]
        # count -= 1
        # Data = Data[0:count]
        Heapify(Data, 0)


HeapSort(Data)
SortStatus = all(Data[i] <= Data[i+1]
                 for i in range(len(Data)-1))  # Check if Sorted
print(f'Is the Dataset Sorted: {SortStatus}')
