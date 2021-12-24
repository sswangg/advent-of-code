def solution1(commands):
    horizontal_pos = 0
    depth = 0
    for command in commands:
        direction, distance = command
        if direction == "forward":
            horizontal_pos += distance
        elif direction == "up":
            depth -= distance
        elif direction == "down":
            depth += distance
    return horizontal_pos * depth


def solution2(commands):
    horizontal_pos = 0
    depth = 0
    aim = 0
    for command in commands:
        direction, amount = command
        if direction == "forward":
            horizontal_pos += amount
            depth += aim * amount
        elif direction == "up":
            aim -= amount
        elif direction == "down":
            aim += amount
    return horizontal_pos * depth


if __name__ == "__main__":
    with open("input.txt") as file:
        f_in = file.read().splitlines()
    my_commands = [(line.split()[0], int(line.split()[1])) for line in f_in]
    print(solution1(my_commands))
    print(solution2(my_commands))
