def solution1(depths):
    result = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i-1]:
            result += 1
    return result


def solution2(depths):
    three_sums = []
    for i in range(len(depths)-2):
        three_sums.append(sum(depths[i:i+3]))
    return solution1(three_sums)


if __name__ == "__main__":
    with open("input.txt") as file:
        f_in = file.read().splitlines()
    my_depths = list(map(int, f_in))
    print(solution1(my_depths))
    print(solution2(my_depths))
