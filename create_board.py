
def visual_board(board):
    print("Let's take a closer look at our Sudoku board!")
    for row in range(len(board)): # row = 0,1,2,3...8
        if row % 3 == 0 and row != 0:
            print('- - - - - - - - - - - - - - - - - ')
        for col in range(len(board[0])):
            if col % 3 == 0:
                print('| ', end = '')
            if col == 8:
                print(f'{str(board[row][col])} | ')
            else:
                print(f'{str(board[row][col])} ', end=' ')

def text_to_list():
    fname = input('Enter the name of the txt file which contains your board: ')
    try:
        fhandler = open(fname, 'r')
        board = []
        for line in fhandler:
            stripped_line = line.strip()
            line_list = stripped_line.split(',')
            board.append(line_list)

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = int(board[i][j])
                if board[i][j] == 0:
                    board[i][j] = '*'
        fhandler.close()

        return board

    except:
        print('The file cannot be found. Are you sure it is in the working directory?')








