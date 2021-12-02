
def dayOnePartOneAndTwo():

    horizontalPosition = 0
    depth = 0
    inputValues = []
    answer = 0
    aim = 0
    answerPartTwo = 0

    f = open("data.txt", "r")
    lines = f.readlines()

    i = 0
    while (i < len(lines)):

        inputValues = lines[i].split()

        if (inputValues[0] == "forward"):
            horizontalPosition += int(inputValues[1])
        
        elif (inputValues[0] == "down"):
            depth += int(inputValues[1])

        else:
            depth -= int(inputValues[1])
        
        i+=1

    answear = depth * horizontalPosition

    ### Part two #####
    horizontalPosition = 0
    depth = 0

    i = 0
    while (i < len(lines)):

        inputValues = lines[i].split()

        if (inputValues[0] == "forward"):
            horizontalPosition += int(inputValues[1])
            depth += (aim * int(inputValues[1]))
        
        elif (inputValues[0] == "down"):
            aim += int(inputValues[1])

        else:
            aim -= int(inputValues[1])
        
        i+=1

    ansanswerPartTwo = horizontalPosition * depth
    
    return ("Answer part one: " + str(answear) + "\n" + "Answer part two: " + str(ansanswerPartTwo))


def main():
    print(dayOnePartOneAndTwo())

if __name__ == "__main__":
    main()
