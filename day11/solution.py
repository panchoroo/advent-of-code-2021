# with open('/Users/amieeverett/Sites/advent-of-code-2021/day11/input-test.txt') as f:
with open('/Users/amieeverett/Sites/advent-of-code-2021/day11/input.txt') as f:
    input = [str(i.strip()) for i in f.readlines()]


def findFlashingOctopi(octopusData):
    data = octopusData
    def getAdjacentPoints(point):
        adjacentPoints=[]
        a, b = point
        for c in range(3):
            newY = a-1+c
            if 0 <= newY < 10:
                for d in range(3):
                    newX = b-1+d
                    if 0 <= newX < 10:
                        if newY != a or newX != b:
                            adjacentPoints.append((newY, newX))
        return adjacentPoints

    totalFlashes = 0
    allFlashes = []
    for k in range(10):
        allFlashes.append("0000000000")
    stepCounter = 0
    flashingSynched = False

    while flashingSynched == False:
    # for i in range(100):
        stepCounter += 1
        newData = []
        for y in range(10):
            newLine = ""
            for x in range(10):
                nines = int(data[y][x]) + 1
                if nines >= 10:
                    newLine += "X"
                else:
                    newLine += str(int(nines))
            newData.append(newLine)
        
        queue = []
        for y2 in range(len(newData)):
            for x2 in range(len(newData[y2])):
                if newData[y2][x2] == "X":
                    queue.append((y2, x2))
        
        # print("newData", newData)
        data = newData

        while len(queue) > 0:
            # as they are dealt with on the queue, set qPoint to 0 and add 1 to sum of flashes
            qPoint= queue.pop()
            totalFlashes += 1
            yQ, xQ = qPoint
            data[yQ]=data[yQ][:xQ] + "0" + data[yQ][xQ+1:]

            qAdjPoints = getAdjacentPoints(qPoint)
            # inc all adjacent by 1 (not 0's or X's)
            for qAdjPoint in qAdjPoints:
                qY, qX = qAdjPoint
                if data[qY][qX] != "0" and data[qY][qX] != "X":
                    newDigit = int(data[qY][qX])+1
                    if newDigit > 9:
                        # when next one goes X, add point to a queue
                        data[qY]=data[qY][:qX] + "X" + data[qY][qX+1:]
                        queue.append((qY, qX))
                    else:
                        data[qY]=data[qY][:qX] + str(newDigit) + data[qY][qX+1:]
        if data == allFlashes:
            print("data", stepCounter, data)
            flashingSynched = True
            break
    # print("totalFlashes", totalFlashes)


# Part One solution:
findFlashingOctopi(input) 