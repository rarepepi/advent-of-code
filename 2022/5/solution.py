def get_ord(letter):
  # Get the ASCII value of the letter
  ascii_value = ord(letter)

  # If the letter is lowercase, return its ASCII value minus the value of 'a' plus 1
  if 'a' <= letter <= 'z':
    return ascii_value - ord('a') + 1

  # If the letter is uppercase, return its ASCII value minus the value of 'A' plus 27
  elif 'A' <= letter <= 'Z':
    return ascii_value - ord('A') + 27

  # Otherwise, return the ASCII value
  else:
    return ascii_value

def part1():
    problemInput = open("input.txt", "r")
    inputData = problemInput.read().splitlines()

    # Initialize the total priority
    total_priority = 0

    # For each rucksack
    for rucksack in inputData:
        # Split the rucksack into two compartments
        middle = len(rucksack) // 2

        comp1 = rucksack[:middle]
        comp2 = rucksack[middle:]

        # Find the common characters
        common = [c for c in comp1 if c in comp2]

        # If there is exactly one common character
        if len(common) >= 1:
            # Get the priority of the character
            priority = get_ord(common[0])

            # Add the priority to the total
            total_priority += priority

    # Print the total priority
    print(total_priority)


def part2():
    problemInput = open("input.txt", "r")
    inputData = problemInput.read().splitlines()

    # Initialize the total priority
    total_priority = 0

    # For each rucksack
    for i in range(0, len(inputData), 3):
        # Split the rucksacks into two compartments
        group_member_one = inputData[i]
        group_member_two = inputData[i + 1]
        group_member_three = inputData[i + 2]
   

        # Find the common characters
        common = [c for c in group_member_one if c in group_member_two and c in group_member_three]
        # If there is exactly one common character
        if len(common) >= 1:
            # Get the priority of the character
            priority = get_ord(common[0])

            # Add the priority to the total
            total_priority += priority

    # Print the total priority
    print(total_priority)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()