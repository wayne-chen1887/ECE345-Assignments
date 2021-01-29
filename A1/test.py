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
    InputFile = 'a1.small'

# Storing Data as nested list, where key is element 0 of nested list
Data = dict()
with open(InputFile + '.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        Data[row[0]] = list()
        for i in row[1:]:
            Data[row[0]].append(i)

print(Data.keys())
