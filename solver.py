
def solve(bo):
    # finds next empty slot
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        # tries numbers 1-9 in that slot to check if its a valid move
        if valid_move(bo, i, (row, col)):
            # places it if its valid
            bo[row][col] = i

            # return true if no slots are left therefore it is complete
            if solve(bo):
                return True

            bo[row][col] = 0

    return False




def print_board(bo):
    for i in range(len(bo)):
        # for every third row place a line
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        # for every third column place a line
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    # iterates through to find an empty slot
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None



def valid_move(bo, num, pos):
    # Checks rows
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Checks column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Checks box (3x3)
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

