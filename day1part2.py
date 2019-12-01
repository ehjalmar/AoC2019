import math

def getFuleReq(input):
    fuelReq = math.floor(input/3) - 2
    if fuelReq > 0:
        return fuelReq
    else:
        return -1

file=open('day1input.txt', 'r')
lines = file.readlines()

totalFuelReq = 0

for line in lines:
    massInput = int(line)
    fuelReq = getFuleReq(massInput)
    fuelReqForModule = fuelReq

    while fuelReq > 0:
        fuelReq = getFuleReq(fuelReq)
        if fuelReq > 0:
            fuelReqForModule += fuelReq
            print(fuelReq)
    totalFuelReq += fuelReqForModule

print('------------Fuel Required----------------')
print(totalFuelReq)