# with open('/Users/amieeverett/Sites/advent-of-code-2021/day2/input-test.txt') as f:
with open('/Users/amieeverett/Sites/advent-of-code-2021/day2/input.txt') as f:
    input = [str(i.strip()) for i in f.readlines()]
# print(input)

# def multiplyPosition(instructions):
#     xPosition = 0
#     yPosition = 0
#     while len(instructions) > 0:
#         instruction = (instructions.pop(0)).split(" ")
#         direction = instruction[0]
#         value = int(instruction[1])
#         if direction == "forward":
#             xPosition += value
#         elif direction == "down":
#             yPosition += value
#         else:
#             yPosition -= value
#     print(xPosition*yPosition)

# Part One solution:
# multiplyPosition(input)

# Part Two:

def multiplyPosition(instructions):
    aim = 0
    xPosition = 0
    yPosition = 0
    while len(instructions) > 0:
        instruction = (instructions.pop(0)).split(" ")
        direction = instruction[0]
        value = int(instruction[1])
        if direction == "forward":
            xPosition += value
            yPosition += aim*value
        elif direction == "down":
            aim += value
        else:
            aim -= value
    print(xPosition*yPosition)


# Part Two solution:
multiplyPosition(input)
