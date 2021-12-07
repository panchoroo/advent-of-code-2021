# with open('/Users/amieeverett/Sites/advent-of-code-2021/day6/input-test.txt') as f:
with open('/Users/amieeverett/Sites/advent-of-code-2021/day6/input.txt') as f:
    input = [str(i.strip()) for i in f.readlines()]
# print(input)


def numberOfLanternFish(lanternFish, days):
    fishList = lanternFish[0].split(",")
    for i in range(days):
        for f in range(len(fishList)):
            fish = int(fishList[f])
            if fish == 0:
                fishList[f] = 6
                fishList.append(8)
            else:
                fishList[f] = fish-1
        # print("fish", fishList)
    print("how many fish", len(fishList))


# Part One solution:
# numberOfLanternFish(input, 80)  # 5934

# Part Two:

# Part Two solution:

def numberOfLanternFishByFish(lanternFish, days):
    fishList = lanternFish[0].split(",")
    fishesArray = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in fishList:
        fishesArray[int(fish)] += 1

    for index in range(days):
        newFish = fishesArray.pop(0)
        fishesArray.append(newFish)
        fishesArray[6] += newFish  # increase 6's by that number
    print("fishesArray", fishesArray)
    print("how many fish", sum(fishesArray))

# numberOfLanternFishByFish(input, 18)
# numberOfLanternFishByFish(input, 80)
numberOfLanternFishByFish(input, 256) 
