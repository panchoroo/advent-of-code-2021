# with open('/Users/amieeverett/Sites/advent-of-code-2021/day1/input-test.txt') as f:
with open('/Users/amieeverett/Sites/advent-of-code-2021/day1/input.txt') as f:
    sonarDepths = [int(i.strip()) for i in f.readlines()]
# print(sonarDepths)


def sumDepthIncreases(depths):
    NumberOfDepthIncreases = 0
    depth1 = None
    while len(depths) > 0:
        depth2 = depths.pop(0)
        if depth1 != None:
            if depth2 > depth1:
                NumberOfDepthIncreases += 1
        depth1 = depth2
    print(NumberOfDepthIncreases)

# Part One solution:
# sumDepthIncreases(sonarDepths)

# Part Two:

def sumDepthIncreases(depths):
    NumberOfSumIncreases = 0
    sum1 = depths[0] + depths[1] + depths[2]
    while len(depths) > 3: # change this 
        sum2 = depths[1] + depths[2] + depths[3]
        if sum2 > sum1:
            NumberOfSumIncreases += 1
        del depths[0]    
        sum1 = sum2

    print(NumberOfSumIncreases)


# Part Two solution:
sumDepthIncreases(sonarDepths)
