# with open('/Users/amieeverett/Sites/advent-of-code-2021/day5/input-test.txt') as f:
with open('/Users/amieeverett/Sites/advent-of-code-2021/day5/input.txt') as f:
    input = [str(i.strip()) for i in f.readlines()]
# print(input)

def findOverlappingPoints(vents):
    def isNotDiagonal(ends):
        endpt1 = ends[0].split(",")
        endpt2 = ends[1].split(",")
        x, y = int(endpt1[0]), int(endpt1[1])
        x2, y2 = int(endpt2[0]), int(endpt2[1])
        same = "y"
        if x == x2:
            same = "x"
        return (x == x2 or y == y2, [x, y, x2, y2], same)

    def generatePointsInLine(line):
        stringOfPoints = ""
        endpoints = line.split("->")
        notDiagonal, points, sameXorY = isNotDiagonal(endpoints)
        startingIndexX = points[0]
        startingIndexY = points[1]
        xMultiplier, yMultiplier = 1, 1
        if points[2] < points[0]:
            startingIndexX = points[2]
            xMultiplier = -1
        if points[3] < points[1]:
            startingIndexY = points[3]
            yMultiplier = -1
        pointRange = abs((points[3]) - points[1])+1

        if notDiagonal:
            if sameXorY == "x": # vertical
                for i in range(pointRange):
                    stringOfPoints += str(points[0]) + \
                        ","+str(startingIndexY+i)+" "
            else: # horizontal 
                for i in range(abs((points[2]) - points[0])+1):
                    startingIndex = points[0]
                    stringOfPoints += str(startingIndexX+i) + \
                        ","+str(points[1])+" "
        else: # diagonal
            for i in range(pointRange):
                stringOfPoints += str(points[0]+i*xMultiplier) + \
                    ","+str(points[1]+i*yMultiplier)+" "

        return (stringOfPoints)
    
    pointsMarked = {}
    overlapCounter = 0
    for vent in vents:
        pointsString = generatePointsInLine(vent)
        # print(pointsString)
        if pointsString:
            for point in pointsString.split(" "):
                if point:
                    if point in pointsMarked.keys():
                        if pointsMarked[point] == 1:
                            overlapCounter += 1
                        pointsMarked[point] += 1
                    else:
                        pointsMarked[point] = 1
            
    print("overlapCounter", overlapCounter)

# Part One solution:
findOverlappingPoints(input)

# Part Two:

# Part Two solution:
