# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:08:10 2021

@author: fajardo
"""

commands  = {
  "forward": [1, 0],
  "down":    [0, 1],
  "up":      [0,-1]
}

def readInput(file):
    with open(file, 'r') as f:
        return f.readlines()

def getData(inputTxt):
    data = []
    for line in inputTxt:
        data.append(line.strip().split())
    return data
    
def processData(data):
    position = [0,0] #horizontal, depth
    for d in data:
        move = [m*int(d[1]) for m in commands[d[0]]]
        position = [sum(x) for x in zip(position, move)]
    return position


def processDataWithAim(data):
    position = [0,0,0] #horizontal, aim, depth
    for d in data:
        move = [c*int(d[1]) for c in commands[d[0]]]
        move.append(int(d[1])*position[1]*commands[d[0]][0])
        position = [sum(x) for x in zip(position, move)]
        
    return position

def solve(file):
    dataTxt = readInput(file)
    
    data = getData(dataTxt)
    
    position = processData(data)
    solution = position[0] * position[1]
    print(" * Final position (horizontal, depth) = {}. Solution = {}".format(position, solution)) #1507611
    
    position = processDataWithAim(data)
    solution = position[0] * position[2]
    print(" * Final position (horizontal, aim, depth) = {}. Solution = {}".format(position, solution)) #1880593125

if __name__ == "__main__":
    print("TEST")
    print("========================================================================================")
    solve("test.txt")
    print("========================================================================================")
    
    print("SOLUTION")
    print("========================================================================================")
    solve("input.txt")
    print("========================================================================================")

    