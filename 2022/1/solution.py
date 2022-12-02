def part1():
    problemInput = open("input.txt", "r")
    inputData = problemInput.read().splitlines()
    maxCounter = 0
    counter = 0
    for i in inputData:
        if i != "":
            counter += int(i)
        else:
            if counter > maxCounter:
                maxCounter = counter
            counter = 0
    
    print(maxCounter)


def part2():
    problemInput = open("input.txt", "r")
    inputData = problemInput.read().splitlines()
    elfCalAmounts = []
    counter = 0
    for i in inputData:
        if i != "":
            counter += int(i)
        else:
            elfCalAmounts.append(counter)        
            counter = 0

    print(sum(sorted(elfCalAmounts)[-1:-4:-1]))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()