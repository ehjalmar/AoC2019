import math
#print(math.floor(143366/3) - 2)

file=open('day1input.txt', 'r')
lines = file.readlines()

totalFuelReq = 0

for line in lines:
    fuelReqInput = int(line)
    fuelReq = math.floor(fuelReqInput/3) - 2
    print(fuelReq)
    totalFuelReq = totalFuelReq + fuelReq

print('------------Fuel Required----------------')
print(totalFuelReq)