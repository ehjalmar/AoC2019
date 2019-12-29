from collections import defaultdict 

file = open("day6.txt")
puzzelInput = file.readlines()

graphInput = defaultdict(list) 

def findOrbits(inputDict, numberOfOrbits, currentObject, rootObject):
    currentOrbitTarget = inputDict[currentObject]
    if currentOrbitTarget in inputDict: # and inputDict[currentOrbitTarget] != []:
        print("Which orbits: " + str(inputDict[currentOrbitTarget]))
        numberOfOrbits[rootObject] += 1
        findOrbits(inputDict, numberOfOrbits, currentOrbitTarget, rootObject)

for mapPoint in puzzelInput:
    objects = mapPoint.split(")")
    leftPoint = objects[0].replace('\n', '').replace('\r', '')
    rightPoint = objects[1].replace('\n', '').replace('\r', '')
    graphInput[rightPoint] = leftPoint

numberOfOrbits = defaultdict(list)
for tempObject in graphInput:
    print(tempObject + " orbits: " + graphInput[tempObject])
    numberOfOrbits[tempObject] = 1
    findOrbits(graphInput, numberOfOrbits, tempObject, tempObject)
    print("Number of orbits: " + str(numberOfOrbits[tempObject]))

totalOrbits = 0
for currentNumber in numberOfOrbits:
    totalOrbits += numberOfOrbits[currentNumber]

print("Total number of orbits: " + str(totalOrbits))

