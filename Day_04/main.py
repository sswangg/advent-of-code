def solution1(draw_order, boards):
    boards_is_filled = [[[0]*5 for j in range(5)] for b in boards]
    for num in draw_order:
        for i in range(len(boards)):
            for j in range(5):
                for k in range(5):
                    if boards[i][j][k] == num:
                        boards_is_filled[i][j][k] = 1
        for b_i in range(len(boards_is_filled)):
            board_filled = boards_is_filled[b_i]
            board = boards[b_i]
            for i in range(5):
                if board_filled[i] == [1]*5 or [board_filled[j][i] for j in range(5)] == [1]*5:
                    score = 0
                    for x in range(5):
                        for y in range(5):
                            if board_filled[x][y] == 0:
                                score += board[x][y]
                    score *= num
                    return score


def solution2(draw_order, boards):
    boards_is_filled = [[[0]*5 for j in range(5)] for b in boards]
    not_won = [1]*len(boards)
    for num in draw_order:
        for i in range(len(boards)):
            for j in range(5):
                for k in range(5):
                    if boards[i][j][k] == num:
                        boards_is_filled[i][j][k] = 1
        for b_i in range(len(boards_is_filled)):
            board_filled = boards_is_filled[b_i]
            for i in range(5):
                if board_filled[i] == [1]*5 or [board_filled[j][i] for j in range(5)] == [1]*5:
                    not_won[b_i] = 0
                if sum(not_won) == 1:
                    last_board = boards[not_won.index(1)]
                if sum(not_won) == 0:
                    score = 0
                    for x in range(5):
                        for y in range(5):
                            if board_filled[x][y] == 0:
                                score += last_board[x][y]
                    score *= num
                    return score


if __name__ == "__main__":
    with open("input.txt") as file:
        first_line = file.readline()
        f_in = file.read()
    my_draw_order = list(map(int, first_line.split(",")))
    my_boards = [[list(map(int, s.split())) for s in chunk.split("\n")] for chunk in f_in[1:].split("\n\n")]
    print(solution1(my_draw_order, my_boards))
    print(solution2(my_draw_order, my_boards))
