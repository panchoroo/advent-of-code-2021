# with open('/Users/amieeverett/Sites/advent-of-code-2021/day10/input-test.txt') as f:
with open('/Users/amieeverett/Sites/advent-of-code-2021/day10/input.txt') as f:
    input = [str(i.strip()) for i in f.readlines()]

def findCorruptedSum(data):
    corruptedSum = 0
    openingChars = ["(", "[", "{", "<"]
    closingChars = [")", "]", "}", ">"]
    incompleteSums = []
    for line in data:
        opened = ""
        sumOfIncompleted = 0
        for c in range(len(line)):
            if line[c] in openingChars:
                opened+=line[c]
            elif openingChars.index(opened[-1]) == closingChars.index(line[c]):
                opened = opened[:-1]
            else:
                print("corrupted")
                index = closingChars.index(line[c])
                corruptedPoints = [3, 57, 1197, 25137]
                corruptedSum += corruptedPoints[index]
                break
            if c == len(line)-1:
                print("string completed")
                while len(opened) > 0:
                    print("string NOT completed")
                    points = [1, 2, 3, 4]
                    sumOfIncompleted *= 5
                    sumOfIncompleted += points[openingChars.index(opened[-1])]
                    opened = opened[:-1]
        if sumOfIncompleted > 0:
            incompleteSums.append(sumOfIncompleted)
    incompleteSums.sort()
    medianSum = incompleteSums[int(len(incompleteSums)/2)]
    print("corruptedSum", corruptedSum)
    print("incompleteSums", incompleteSums)
    print("medianSum", medianSum)


# Part One solution:
findCorruptedSum(input)

# Part Two:
