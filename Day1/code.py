# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 21:22:43 2021

@author: fajardo
"""


def readInput():
    data = []
    with open("input.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            data.append(int(line.strip()))
    return data

    
def getNumIncrements(data, n):
    assert(len(data) > n)
    count = 0
    prevValue = sum(data[0:n])
    for i in range(1, len(data)-n+1):
        value = sum(data[i:i+n])
        if (value > prevValue):
            count = count + 1;
        prevValue = value
    return count

if __name__ == "__main__":
    # data = [199,200,208,210,200,207,240,269,260,263] # Test data
    data = readInput()
    n = 1
    count = getNumIncrements(data, n)
    print("Window size {}: Number of increments {}".format(n, count)) #1521

    n = 3
    count = getNumIncrements(data, n)
    print("Window size {}: Number of increments {}".format(n, count)) #1543
