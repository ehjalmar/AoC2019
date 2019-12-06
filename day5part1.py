def processList(puzzelInput, file, userInput):
    # start at pos 0
    opCodePosition = 0

    while opCodePosition < len(puzzelInput):
        
        # find OpCode
        codeInput = puzzelInput[opCodePosition]
        opCode = int(codeInput[-2:])

        if opCode > 4:
            print("OpCode found:" + str(opCode) + " exiting program!")
            break

        paramMode1 = 0
        paramMode2 = 0
        paramMode3 = 0
        parameterModeCode = codeInput[:-2][::-1]
        if len(parameterModeCode) > 0:
            paramMode1 = int(parameterModeCode[0])
        if len(parameterModeCode) > 1:
            paramMode2 = int(parameterModeCode[1])
        if len(parameterModeCode) > 2:
            paramMode3 = int(parameterModeCode[2])
        
        if opCode == 1:
            # Get Input vaules
            param1 = int(puzzelInput[opCodePosition + 1])
            param2 = int(puzzelInput[opCodePosition + 2])

            if paramMode1 == 0:
                param1 = int(puzzelInput[param1])
            if paramMode2 == 0:
                param2 = int(puzzelInput[param2])
            calculatedValue = param1 + param2

            if paramMode3 == 0:
                outputPosition = int((puzzelInput[opCodePosition + 3]))
                puzzelInput[outputPosition] = str(calculatedValue)

            opCodePosition += 4
            
        elif opCode == 2:
             # Get Input vaules
            param1 = int(puzzelInput[opCodePosition + 1])
            param2 = int(puzzelInput[opCodePosition + 2])

            if paramMode1 == 0:
                param1 = int(puzzelInput[param1])
            if paramMode2 == 0:
                param2 = int(puzzelInput[param2])
            calculatedValue = param1 * param2

            if paramMode3 == 0:
                outputPosition = int((puzzelInput[opCodePosition + 3]))
                puzzelInput[outputPosition] = str(calculatedValue)

            opCodePosition += 4


        # Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example, the instruction 3,50 would take an input value and store it at address 50.
        elif opCode == 3:
            param1 = int(puzzelInput[opCodePosition + 1])
            puzzelInput[param1] = str(userInput)
            opCodePosition += 2

        # Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50.
        elif opCode == 4:
            param1 = int(puzzelInput[opCodePosition + 1])
            
            if paramMode1 == 0:
                param1 = int(puzzelInput[param1])

            print(str(param1))

            opCodePosition += 2

file = open("day5.txt")
puzzelInputOriginal = file.readline().split(",")
puzzelInput = list(puzzelInputOriginal)

print("Enter input value and press enter:")
userInput = input()

puzzelInput = list(puzzelInputOriginal)
    
processList(puzzelInput, file, userInput)
