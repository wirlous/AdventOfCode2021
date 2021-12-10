# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 09:53:55 2021

@author: fajardo
"""

def readInput(file):
    with open(file, 'r') as f:
        return f.readlines()

def getData(inputTxt):
    data = []
    for line in inputTxt:
        data.append(line.strip())
    return data
    
def processData1(data):
    n = len(data[0])
    gamma = getGamma(data, n)
    epsilon = getEpsilon(gamma, n)
    return (gamma, epsilon)

def processData2(data):
    n = len(data[0])
    oxigen = getOxigen(data, n)
    co2 = getCO2(data, n)
    return (oxigen, co2)
    
def getGamma(data, n):
    dataSize = len(data)
    gamma = ""
    for pos in range(n):
        count = 0
        for d in data:
            count = count + int(d[pos])
        if ((2*count) > dataSize):
            gamma = gamma + "1"
        else:
            gamma = gamma + "0"
    return int(gamma,2)

def getEpsilon(gamma, n):
    return ((1<<n)-1)-gamma

def getOxigen(data, n):
    for pos in range(n):
        (dataOnes, dataZeros) = splitData(data, pos)
        # Most common, 1 over 0
        if (len(dataOnes) >= len(dataZeros)):
            data = dataOnes
        else:
            data = dataZeros
        if (len(data) == 1):
            return int(data[0],2)
    return int(data[0],2)

def getCO2(data, n):
    for pos in range(n):
        (dataOnes, dataZeros) = splitData(data, pos)
        # Least common, 0 over 1
        if (len(dataZeros) <= len(dataOnes)):
            data = dataZeros
        else:
            data = dataOnes
        if (len(data) == 1):
            return int(data[0],2)
    return int(data[0],2)


def splitData(data, pos):
    dataOnes = []
    dataZeros = []
    for d in data:
        (dataOnes,dataZeros)[d[pos]=='0'].append(d)
    return (dataOnes, dataZeros)



def solve(file):
    dataTxt = readInput(file)
    data = getData(dataTxt)
    (gamma, epsilon) = processData1(data)
    (oxigen, co2) = processData2(data)
    
    print("Power consumption ({}, {}) = {}".format(gamma, epsilon, gamma*epsilon))
    print("Life support ({}, {}) = {}".format(oxigen, co2, oxigen*co2))
    
if __name__ == "__main__":
    print("TEST")
    print("========================================================================================")
    solve("test.txt") # (22, 9) = 198
    print("========================================================================================")
    
    print("SOLUTION")
    print("========================================================================================")
    solve("input.txt") # (177, 3918) = 693486
    print("========================================================================================")

    