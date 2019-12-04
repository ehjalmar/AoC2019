import math

rangeStart = "136818"
rangeEnd = 685979

# Bump up chars to apply with rule "Going from left to right, the digits never decrease"
currentChars = []
currentChars.append("1")
currentChars.append("3")
currentChars.append( "6")
currentChars.append("8")
currentChars.append("1")
currentChars.append("8")

for currentPos in range(5):
    if( int(currentChars[currentPos]) > int(currentChars[currentPos + 1])):
        currentChars[currentPos + 1] = currentChars[currentPos]

firstValidInt = ""

for char in currentChars:
    firstValidInt = int(str(firstValidInt) + char)

validPasswords = []
current = firstValidInt
while current < rangeEnd:
    isValid = True

    numbers = [(current//(10**i))%10 for i in range(int(math.ceil(math.log(current, 10)))-1, -1, -1)]
    hasAdjacent = False

    for index in range(5):
        if(numbers[index] > numbers[index + 1]): # Decreasing number?
            isValid = False
        
        if(numbers[index] == numbers[index + 1]): # Two adjacent digits are the same (like 22 in 122345).
            hasAdjacent = True

    if (isValid and hasAdjacent):
        validPasswords.append(current)
    current += 1

print("Number of possible passwords: " + str(validPasswords.__len__()))
print("Finished!")    

    
