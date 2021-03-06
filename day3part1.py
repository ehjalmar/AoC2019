class Coord:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.distance = abs(self.x) + abs(self.y)

    def __hash__(self):
        return hash((("x" + str(self.x)), ("y" + str(self.y)), self.distance))
    
    def __eq__(self, other):
        return self.x, self.y, self.distance == other.x, other.y, other.distance

    def __ne__(self, other):
        return not self.__eq__(other)

def GetCoordsFromPath(path):
    coords = []

    for instruction in path:
        direction = instruction[:1]
        distance = int(instruction[1:])
        
        currentX = 0
        currentY = 0
        if len(coords) > 0:
            currentCoord = coords[-1]
            currentX = currentCoord.x
            currentY = currentCoord.y
        
        for foo in range(distance):
            newPos = foo + 1
            if direction == "R":
                x = currentX + newPos
                coords.append(Coord(x, currentY))
            elif direction == "L":
                x = currentX - newPos
                coords.append(Coord(x, currentY))
            elif direction == "U":
                y = currentY + newPos
                coords.append(Coord(currentX, y))
            elif direction == "D":
                y = currentY - newPos
                coords.append(Coord(currentX, y))
    
    return coords

file = open('day3.txt', 'r')

wireOnePath = file.readline().split(",")
wireTwoPath = file.readline().split(",")
file.close()

wireOneCoords = GetCoordsFromPath(wireOnePath)
wireTwoCoords = GetCoordsFromPath(wireTwoPath)

crossings = set(wireOneCoords).intersection(wireTwoCoords)

sortedCrossings = sorted(crossings, key=lambda x: x.distance, reverse=True)
for crossing in sortedCrossings:
    print(crossing.distance)