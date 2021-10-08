from create_board import visual_board, text_to_list


def solve(board):

    find = get_empty(board)
    if not find:
        return True

    for i in range(1,10):
        if validity(board, i, find):
            board[find['row']][find['column']] = i

            if solve(board):
                return True
            board[find['row']][find['column']] = '*'
    return False




#we have to check if the element added in the square is valid
def validity(board, nr, position):
    valid_row = True
    valid_col = True

    #Check row -> position = {row:index of the row, column: index of the column}
    for element in board[position['row']]:
        if element == nr and board[position['row']].index(element) != position['column']:
            valid_row = False

    #Check column
    for row in range(len(board)):
        if board[row][position['column']] == nr and row != position['row']:
            valid_col = False

    #Check box
    def check_box(nr, position):
        valid_box = True
        r = position['row']
        c = position['column']
        box_x = list()
        box_y = list()
        stop_loop = True
        while stop_loop:
            if r % 3 == 0:
                stop_loop = False
                for i in range(r,r+3):
                    box_x.append(i)
            else:
                r -= 1
        stop_loop = True
        while stop_loop:
            if c % 3 == 0:
                stop_loop = False
                for i in range(c, c+3):
                    box_y.append(i)
            else:
                c -= 1

        for i in box_x:
            for j in box_y:
                if board[i][j] == nr and (i != position['row'] or j != position['column']):
                    valid_box = False
        return valid_box

    valid_box = check_box(nr, position)

    if valid_box and valid_col and valid_row :
        return True



# first function -> find an empty square (a square which has * in it) and return its index because we are going to need it
def get_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == '*':
                return {'row':row, 'column':col}
                #position of the empty square

    return None


b = text_to_list()
# To see the board without any modificated square, executate these commands
visual_board(b)
print('\n')
solve(b)
visual_board(b)






