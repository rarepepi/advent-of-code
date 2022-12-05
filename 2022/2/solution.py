choiceScore = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

roundOutcomeScore = {
    "W": 6,
    "D" : 3,
    "L": 0,
}

opponentMoveTranslator = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}


def ifIWinRockPaperScissors(player1, player2):
    if player1 == "A" and player2 == "Y":
        return True
    elif player1 == "B" and player2 == "Z":
        return True
    elif player1 == "C" and player2 == "X":
        return True
    else:
        return False

def whatDoIChoose(player1, expectedResult):
    if player1 == "A":
        if expectedResult == "X":
            return "Z"
        elif expectedResult == "Y":
            return "X"
        elif expectedResult == "Z":
            return "Y"
    if player1 == "B":
        if expectedResult == "X":
            return "X"
        elif expectedResult == "Y":
            return "Y"
        elif expectedResult == "Z":
            return "Z"
    if player1 == "C":
        if expectedResult == "X":
            return "Y"
        elif expectedResult == "Y":
            return "Z"
        elif expectedResult == "Z":
            return "X"

def part1():
    problemInput = open("input.txt", "r")
    inputData = problemInput.read().splitlines()

    totalScore = 0
    
    for i in inputData:
        theirMove, myMove = i.split(" ")
        if ifIWinRockPaperScissors(theirMove, myMove):
            totalScore += roundOutcomeScore["W"]
            totalScore += choiceScore[myMove]

        elif opponentMoveTranslator[theirMove] == myMove:
            totalScore += roundOutcomeScore["D"]
            totalScore += choiceScore[myMove]
        
        else:
            totalScore += roundOutcomeScore["L"]
            totalScore += choiceScore[myMove]
    
    print(totalScore)


def part2():
    problemInput = open("input.txt", "r")
    inputData = problemInput.read().splitlines()

    totalScore = 0
    
    for i in inputData:
        theirMove, myExpectedWinResult = i.split(" ")
        myMove = whatDoIChoose(theirMove, myExpectedWinResult)
        # print(theirMove, myMove)
        # print(ifIWinRockPaperScissors(theirMove, myMove))
        if ifIWinRockPaperScissors(theirMove, myMove):
            totalScore += roundOutcomeScore["W"]
            totalScore += choiceScore[myMove]

        elif opponentMoveTranslator[theirMove] == myMove:
            totalScore += roundOutcomeScore["D"]
            totalScore += choiceScore[myMove]
        
        else:
            totalScore += roundOutcomeScore["L"]
            totalScore += choiceScore[myMove]
    
    print(totalScore)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()