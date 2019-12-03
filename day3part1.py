class Coord:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.distance = abs(self.x) + abs(self.y)

    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        return self.x, self.y == other.x, other.y

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
        
        for newPos in range(distance + 1):
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

# crossings = []
# for coordOne in wireOneCoords:
#     for coordTwo in wireTwoCoords:
#         if(coordOne.x == coordTwo.x and coordOne.y == coordTwo.y):
#             crossings.append(coordOne)
#             print("Found intersection coord: " + str(coordOne.x) + " " + str(coordOne.y))

sortedCrossings = sorted(crossings, key=lambda x: x.distance, reverse=True)
for crossing in sortedCrossings:
    print(crossing.distance)