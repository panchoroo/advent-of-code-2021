# with open('/Users/amieeverett/Sites/advent-of-code-2021/day4/input-test.txt') as f:
with open('/Users/amieeverett/Sites/advent-of-code-2021/day4/input.txt') as f:
    input = [str(i.strip()) for i in f.readlines()]
# print(input)


def playBingo(bingoData):
    numbersToDraw = bingoData.pop(0).split(',')
    bingoData.pop(0)
    bingoData = [','.join(bingoData)][0].split(',,')

    def generateBoardData(bingoBoards):
        boardsData = {}
        boardNumber = 0
        numberBoards = len(bingoBoards)
        boardSize = len(bingoBoards[0].split(','))
        for board in bingoBoards:
            xValue = 0
            for row in board.split(','):
                yValue = 0
                for number in row.split(' '):
                    if number:
                        index = int(number)
                        if number in boardsData.keys():
                            boardsData[number].append([boardNumber, (xValue, yValue)])
                        else:
                            boardsData[number] = [[boardNumber, (xValue, yValue)]]
                        yValue += 1
                xValue += 1
            boardNumber += 1
        return (boardsData, boardSize, numberBoards)

    def getSum(winningBoard, row, index, ignore):
        winningSum = 0
        xValue = 0
        for r in winningBoard.split(','):
            if row and xValue != index:
                for number in r.split(' '):
                    if number and number not in ignore:
                        winningSum += int(number)
            elif not row:
                yValue = 0
                for number in r.split(' '):
                    if number: 
                        if yValue != index and number not in ignore:
                            winningSum += int(number)
                        yValue += 1
            xValue += 1
        return winningSum
    
    generatedData, size, boards = generateBoardData(bingoData)

    # 0-4 rows, 5-9 columns 
    tallies = [[0 for r in range(size*2)] for b in range(boards)]
    drawnNumbers = []
    numberWon = [] 
    for draw in numbersToDraw:
        drawnNumbers.append(draw)
        if draw in generatedData.keys():
            for board in generatedData[draw]:
                row = board[1][0]
                column = board[1][1] + 5
                tallies[board[0]][row] += 1
                tallies[board[0]][column] += 1
                if tallies[board[0]][row] == 5 or tallies[board[0]][column] == 5:
                    print("BINGO!")
                    if board[0] not in numberWon:
                        numberWon.append(board[0])
                    if len(numberWon) == boards:
                        rowWon = False
                        winningIndex = board[1][1]
                        if tallies[board[0]][row] == 5:
                            rowWon = True
                            winningIndex = board[1][0]
                        print(int(draw)*getSum(bingoData[board[0]], rowWon, winningIndex, drawnNumbers))
                        return


# Part One solution:
playBingo(input)

# Part Two:
# figure out which board will win last and choose that one.

# Part Two solution:
