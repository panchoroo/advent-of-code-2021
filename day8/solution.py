# with open('/Users/amieeverett/Sites/advent-of-code-2021/day8/input-test.txt') as f:
with open('/Users/amieeverett/Sites/advent-of-code-2021/day8/input.txt') as f:
    input = [str(i.strip()) for i in f.readlines()]
# print(input)

def countIrregularLengths(outputData):
    # only consider output value after delimiter
    # count digits 1,4,7,8 (len != 5 or 6)
    irregularLengths=0
    for line in outputData:
        output = line.split("|")[1]
        for digit in output.split(" "):
            if digit:
                if len(digit) != 5 and len(digit) != 6:
                    irregularLengths += 1

    print("number of irregular digits", irregularLengths)


# Part One solution:
# countIrregularLengths(input)

# Part Two:

def decodeOutput(outputData):
    # find 1, 4, 7, 8 by their unique lengths
    # separate len 5's and 6's into array
    # use 1 to get c & f 
    # 3 = len 5 that contains both c and f
    # get b & d from 4 - 1
    # 5 = len 5 that contains both b and d
    # 2 = remaining len 5
    # 6 = len 6 that ! (contains both c and f)
    # 9 = len 6 that contains both b and d
    # 0 = remaining len 6

    sumTotal = 0
    for line in outputData:
        fives, sixes = [], []
        numInput, output = line.split("|")
        decodedNumbers=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for digit in numInput.split(" "):
            if digit:
                if len(digit) == 5:
                    fives.append(digit)
                elif len(digit) == 6:
                    sixes.append(digit)
                elif len(digit) == 2:
                    decodedNumbers[1] = "".join(sorted(digit))
                elif len(digit) == 4:
                    decodedNumbers[4] = "".join(sorted(digit))
                elif len(digit) == 3:
                    decodedNumbers[7] = "".join(sorted(digit))
                elif len(digit) == 7:
                    decodedNumbers[8] = "".join(sorted(digit))

        bd = decodedNumbers[4]
        c = decodedNumbers[1][0]
        f = decodedNumbers[1][1]
        bd = bd.replace(c, "")
        bd = bd.replace(f, "")

        for five in fives:
            if five.find(c) >= 0 and five.find(f) >= 0:
                decodedNumbers[3] = "".join(sorted(five))
            elif five.find(bd[0]) >= 0 and five.find(bd[1]) >= 0:
                decodedNumbers[5] = "".join(sorted(five))
            else:
                decodedNumbers[2] = "".join(sorted(five))
        
        for six in sixes:
            if six.find(c) < 0 or six.find(f) < 0:
                decodedNumbers[6] = "".join(sorted(six))
            elif six.find(bd[0]) >= 0 and six.find(bd[1]) >= 0:
                decodedNumbers[9] = "".join(sorted(six))
            else:
                decodedNumbers[0] = "".join(sorted(six))
        
        decodedOutput = ""
        for number in output.split(" "):
            if number:
                # print("sortedNum", "".join(sorted(number)))
                indexOfDecoded = decodedNumbers.index("".join(sorted(number)))
                if indexOfDecoded >= 0:
                    # print("indexOfDecoded", indexOfDecoded)
                    decodedOutput+=str(indexOfDecoded)
        sumTotal += int(decodedOutput)
    print(" sumTotal", sumTotal)

# Part Two solution:
decodeOutput(input)
