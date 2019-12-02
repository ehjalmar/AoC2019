def calculate(opCode, input1, input2, puzzelInput, outputPosition):
    if opCode == 1:
        calculatedValue = input1 + input2
        puzzelInput[outputPosition] = str(calculatedValue)
        if calculatedValue == 19690720 and outputPosition == 0:
            return False
        return True
    if opCode == 2:
        calculatedValue = input1 * input2
        puzzelInput[outputPosition] = str(calculatedValue)
        if calculatedValue == 19690720 and outputPosition == 0:
            return False
        return True
    
    print(puzzelInput)
    return False

def processList(puzzelInput, file):
    # start at pos 0
    opCodePosition = 0

    while opCodePosition < len(puzzelInput):
    # find OpCode
        opCode = int(puzzelInput[opCodePosition])

        if opCode == 99:
            break
        if opCode > 2:
            break  

        # Get Input vaules
        input1 = int(puzzelInput[int(puzzelInput[opCodePosition + 1])])
        input2 = int(puzzelInput[int(puzzelInput[opCodePosition + 2])])

        #Get  OutputPosition
        outputPosition = int((puzzelInput[opCodePosition + 3]))

        shouldContinue = calculate(opCode, input1, input2, puzzelInput, outputPosition)
        file.write(puzzelInput[0] + "\r")

        if shouldContinue:
            # Go to next section
            opCodePosition = opCodePosition + 4
        else:
            return False
    
    return True

puzzelInputOriginal = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,10,23,2,10,23,27,1,27,6,31,1,13,31,35,1,13,35,39,1,39,10,43,2,43,13,47,1,47,9,51,2,51,13,55,1,5,55,59,2,59,9,63,1,13,63,67,2,13,67,71,1,71,5,75,2,75,13,79,1,79,6,83,1,83,5,87,2,87,6,91,1,5,91,95,1,95,13,99,2,99,6,103,1,5,103,107,1,107,9,111,2,6,111,115,1,5,115,119,1,119,2,123,1,6,123,0,99,2,14,0,0".split(",")
puzzelInput = list(puzzelInputOriginal)
noun = 0
continueProccessing = True

file = open("day2.log", "a+")

while(noun < 100):
    puzzelInput = list(puzzelInputOriginal)
    
    if(processList(puzzelInput, file) == False):
        break
    puzzelInput[1] = str(noun)
    
    puzzelInput = list(puzzelInputOriginal)
    verb = 0
    
    while(verb < 100):
        if(processList(puzzelInput, file) == False):
            continueProccessing = False
            break
        verb += 1
        puzzelInput = list(puzzelInputOriginal)
        puzzelInput[1] = str(noun)
        puzzelInput[2] = str(verb)
    if continueProccessing == False:
        break
    noun += 1

file.close()

print(puzzelInput)
print(100 * int(puzzelInput[1]) + int(puzzelInput[2]))