# with open('/Users/amieeverett/Sites/advent-of-code-2021/day7/input-test.txt') as f:
with open('/Users/amieeverett/Sites/advent-of-code-2021/day7/input.txt') as f:
    input = [str(i.strip()) for i in f.readlines()]
# print(input)


def leastFuelPoint(crabPositions):
    def calculateFuel(crabs, median):
        fuel = 0
        for crab in crabs:
            fuel += abs(crab - median)
        return fuel

    medianPoint=0
    crabPositions = crabPositions[0].split(",")
    map_object = map(int, crabPositions)
    sortedCrabs = list(map_object)
    sortedCrabs.sort()

    if len(sortedCrabs) % 2 == 0:
        medianPoint = sortedCrabs[int((len(sortedCrabs)-1)/2)]
    else:
        medianPoint = sortedCrabs[int(len(sortedCrabs)/2)]
    print("least fuel point", medianPoint)
    print("least amount of fuel", calculateFuel(sortedCrabs, medianPoint))


# Part One solution:
# leastFuelPoint(input)

# Part Two:
def leastGaussFuel(crabPositions):
    # ( n^2 + n ) / 2  ~ similar to root mean squared, gauss's formula
    # Gauss's formula: sum of first n integers

    def calculateFuel(crabs, median):
        fuel = 0
        for crab in crabs:
            distance = abs(crab - median)
            if distance > 0:
                fuel += int((distance**2 + distance) / 2)
        return fuel

    crabPositions = crabPositions[0].split(",")
    map_object = map(int, crabPositions)
    sortedCrabs = list(map_object)

    sortedCrabs.sort(reverse=True)

    medianIndex = int(len(sortedCrabs)/2)
    if len(sortedCrabs) % 2 == 0:
        medianIndex = int((len(sortedCrabs)-1)/2)
    
    leastFuel = calculateFuel(sortedCrabs, medianIndex)

    def increaseIndex(m):
        increment = 1
        incrementing = True
        while incrementing:
            incrementing = False
            decIndexFuel = calculateFuel(sortedCrabs, m-increment)
            incIndexFuel = calculateFuel(sortedCrabs, m+increment)
            if incIndexFuel < decIndexFuel:
                return True
            elif incIndexFuel > decIndexFuel:
                return False
            else:
                if m-increment >= 0 and m+increment < len(sortedCrabs):
                    incrementing = True
                    increment += 1
                else:
                    return None

    shouldIncrease = increaseIndex(medianIndex)

    if shouldIncrease == None:
        print("leastFuel is most efficient", leastFuel)
    else:
        inc = 1
        fuelIsDecreasing = True
        while fuelIsDecreasing and 0 <= medianIndex+inc < len(sortedCrabs):
            if shouldIncrease:
                newFuel = calculateFuel(sortedCrabs, medianIndex+inc)
            else:
                newFuel = calculateFuel(sortedCrabs, medianIndex+(inc*-1))
            
            if newFuel > leastFuel:
                fuelIsDecreasing = False
            else:
                leastFuel = newFuel
                inc += 1
        print("this is least fuel", leastFuel)

    # for c in range(len(sortedCrabs)):
    #     print(" * ", calculateFuel(sortedCrabs, sortedCrabs[c]))


# Part Two solution:
leastGaussFuel(input)
