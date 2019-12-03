class Coord:
    def __init__(self, x, y, steps):
        self.x = int(x)
        self.y = int(y)
        self.steps = int(steps)
        self.distance = abs(self.x) + abs(self.y)

    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        return self.x, self.y == other.x, other.y

    def __ne__(self, other):
        return not self.__eq__(other)

class Crossing:
    def __init__(self, crossingOne, crossingTwo, x, y, steps):
        self.crossingOne = crossingOne
        self.crossingTwo = crossingTwo
        self.x = int(x)
        self.y = int(y)
        self.steps = int(steps)

def GetCoordsFromPath(path):
    coords = []
    stepsAlreadyTaken = 0

    for instruction in path:
        direction = instruction[:1]
        distance = int(instruction[1:])
        
        currentX = 0
        currentY = 0

        if len(coords) > 0:
            currentCoord = coords[-1]
            currentX = currentCoord.x
            currentY = currentCoord.y
            stepsAlreadyTaken = currentCoord.steps
        
        for foo in range(distance):
            stepsAlreadyTaken = stepsAlreadyTaken + 1
            newPos = foo + 1
            if direction == "R":
                x = currentX + newPos
                coords.append(Coord(x, currentY, stepsAlreadyTaken))
            elif direction == "L":
                x = currentX - newPos
                coords.append(Coord(x, currentY, stepsAlreadyTaken))
            elif direction == "U":
                y = currentY + newPos
                coords.append(Coord(currentX, y, stepsAlreadyTaken))
            elif direction == "D":
                y = currentY - newPos
                coords.append(Coord(currentX, y, stepsAlreadyTaken))

    return coords

file = open('day3.txt', 'r')

wireOnePath = file.readline().split(",")
wireTwoPath = file.readline().split(",")
file.close()

wireOneCoords = GetCoordsFromPath(wireOnePath)
wireTwoCoords = GetCoordsFromPath(wireTwoPath)

crossings = set(wireTwoCoords).intersection(wireOneCoords)

combinedCrossings = []

sortedCrossings = sorted(crossings, key=lambda x: x.steps, reverse=True)
for visit in wireTwoCoords:
    for crossingWireOne in sortedCrossings:
        if visit.x == crossingWireOne.x and visit.y == crossingWireOne.y:
            combinedCrossings.append(Crossing(visit, crossingWireOne, visit.x, visit.y, visit.steps + crossingWireOne.steps))
            #print("Sum of steps: " + str(visit.steps + crossingWireOne.steps))

sortedCrossingsTotal = sorted(combinedCrossings, key=lambda x: x.steps, reverse=True)
for combinedCrossing in sortedCrossingsTotal:
    print(str(combinedCrossing.x) + " " + str(combinedCrossing.y) + " " + str(combinedCrossing.steps))
print("Finished!")
        