# with open('/Users/amieeverett/Sites/advent-of-code-2021/day3/input-test.txt') as f:
with open('/Users/amieeverett/Sites/advent-of-code-2021/day3/input.txt') as f:
    input = [str(i.strip()) for i in f.readlines()]
# print(input)

def findGammaEpsilon(binaryData):
    gamma = ''
    epsilon = ''

    for count in range(len(binaryData[0])):
        zeroes = 0
        ones = 0
        for datum in binaryData:
            x= datum[count]
            if x == "0":
                zeroes += 1
            else:
                ones += 1
        if zeroes > ones:
            gamma+=("0")
            epsilon+=("1")
        else: 
            gamma+=("1")
            epsilon+=("0")

    # print(int(gamma, 2)*int(epsilon, 2))
    print("gamma", gamma, "epsilon", epsilon)
    return (gamma, epsilon)

# Part One solution:
# findGammaEpsilon(input)

# Part Two:

# lifeSupport = O2 * CO2

# O2: To find oxygen generator rating, determine the most common value(0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.


# CO2: To find CO2 scrubber rating, determine the least common value(0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.

def calculateLifeSupport(data):
    data.sort()
    O2 = data
    CO2 = data

    def findMostCommon(dataList, count, most):
        zeroes = 0
        ones = 0
        for datum in dataList:
            x = datum[count]
            if x == "0":
                zeroes += 1
            else:
                ones += 1
        if most:
            if (zeroes > ones):
                return "0"
            else:
                return "1"
        else:
            if (zeroes > ones):
                return "1"
            else:
                return "0"

    def findFirstOne(sortedData, i):
        splitIndex = 0
        for index in range(len(sortedData)): # TODO: start in middle, go up or down for more efficiency
            if sortedData[index][i] == "1":
                splitIndex = index
                return splitIndex
        return None # if there are none that have a 1 at that index
    
    def filterList(workinglList, gammaOrEpsilon):
        split = len(workinglList)
        for character in range(len(workinglList[0])):
            x = findMostCommon(workinglList, character, gammaOrEpsilon)
            if len(workinglList) > 1:
                split = findFirstOne(workinglList, character)
            else:
                split = None
            if x == "1" and split:
                workinglList = workinglList[split:]
            elif x == "0" and split:
                workinglList = workinglList[:split]
        return workinglList

    o2 = filterList(O2, True)
    co2 = filterList(CO2, False)
    # print("O2", o2)
    # print("CO2", co2)
    print(int(o2[0], 2)*int(co2[0], 2))

# Part Two solution:
calculateLifeSupport(input)
