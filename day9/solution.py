# with open('/Users/amieeverett/Sites/advent-of-code-2021/day9/input-test.txt') as f:
with open('/Users/amieeverett/Sites/advent-of-code-2021/day9/input.txt') as f:
    input = [str(i.strip()) for i in f.readlines()]


def findLowPointSum(smokeData):
    lowPointData = []

    def isValidLowPoint(potMin, index, lineIndex, data):
        potMin = int(potMin)
        up, down, left, right = 10, 10, 10, 10
        if lineIndex > 0:
            up = int(data[lineIndex - 1][index])
        if lineIndex + 1 < len(data):
            down = int(data[lineIndex + 1][index])
        if index + 1 < len(data[lineIndex]):
            right = int(data[lineIndex][index+1])
        if index > 0:
            left = int(data[lineIndex][index-1])
        if potMin < up and potMin < down and potMin < left and potMin < right:
            return True
        return False

    lowPointSum = 0
    for yIndex in range(len(smokeData)):
        lineLowPointSum = 0
        line = smokeData[yIndex]
        foundMin = False
        for xIndex in range(len(line)):
            minimum = int(line[xIndex])
            if isValidLowPoint(minimum, xIndex, yIndex, smokeData):
                lineLowPointSum += int(minimum)+1
                lowPointData.append([int(minimum), yIndex, xIndex])
        lowPointSum += lineLowPointSum
    return lowPointData


# Part One solution:
# findLowPointSum(input)

# Part Two:

def calculateBasins(smokeData):
    def basinFinder(lowPointSet, data):
        low = lowPointSet[0]
        xFirst = lowPointSet[1]
        yFirst = lowPointSet[2]
        pointsToCheck = [(xFirst, yFirst)]
        counter = 1
        basinCount = 0

        while low + counter <= 9 and len(pointsToCheck) > 0:
            newPointsToCheck = []
            for point in set(pointsToCheck):
                basinCount += 1
                x, y = point
                if x > 0 and int(data[x-1][y]) == low+counter:
                    newPointsToCheck.append((x-1, y))
                if x + 1 < len(data) and int(data[x+1][y]) == low+counter:
                    newPointsToCheck.append((x+1, y))
                if y + 1 < len(data[x]) and int(data[x][y+1]) == low+counter:
                    newPointsToCheck.append((x, y+1))
                if y > 0 and int(data[x][y-1]) == low+counter:
                    newPointsToCheck.append((x, y-1))
                #diagonals:
                if x > 0 and y > 0 and int(data[x-1][y-1]) == low+counter:
                    newPointsToCheck.append((x-1, y-1))
                if x + 1 < len(data) and y + 1 < len(data[x]) and int(data[x+1][y+1]) == low+counter:
                    newPointsToCheck.append((x+1, y+1))
                if y + 1 < len(data[x]) and x > 0 and int(data[x-1][y+1]) == low+counter:
                    newPointsToCheck.append((x-1, y+1))
                if y > 0 and x + 1 < len(data) and int(data[x+1][y-1]) == low+counter:
                    newPointsToCheck.append((x+1, y-1))
            counter += 1
            pointsToCheck = newPointsToCheck
        return basinCount
    lowPoints = findLowPointSum(input)

    biggestBasins = []
    for lowPoint in lowPoints:
        biggestBasins.append(basinFinder(lowPoint, smokeData))
    biggestBasins.sort()
    print("$$$", (biggestBasins[-1]+3) * (biggestBasins[-2]+1)*(biggestBasins[-3]+3))


# Part Two solution:
calculateBasins(input)
