import os, math, random, msvcrt
board = []

def initialBoard():
    # generate the empty 2d grid
    for i in range(4):
        board.append([])
        for j in range(4):
            board[i].append(0)
    
    # create 2 tiles to begin
    for i in range(2):
        create_tile()
    
    # create an obstacle
    create_obstacle()

    print_board(board)

def print_board(a):
    # definitely dont fit 4 digit nums
    # i=0
    # print("┌───┬───┬───┬───┐")
    # while True:
    #     print("│",end=" ")
    #     for j in range(4):
    #         print(a[i][j],end=" ")
    #         print("│",end=" ")
    #     print()
    #     i+=1
    #     if i > 3:
    #         break
    #     print("├───┼───┼───┼───┤")
    # print("└───┴───┴───┴───┘")

    # alt board format:
    # ┌─────┐
    # │     │
    # └─────┘
    # repeat 16 times

    # just bad
    for i in range(4):
        for j in range(4):
            print(a[i][j],end="\t")
            print("|",end="")
        print()
        print("--------------------")

# create a tile of either value 2 or 4 on an empty space
def create_tile():
    row, col = pick_emptytile()
    board[row][col] = random.choice([2, 4])
    # board[a[0]][a[1]] = pow(2,random.randint(1,2)) # 2^1=2; 2^2=4
    
# create an obstacle
# obstacle values are 2^x-1 to differenciate from tiles which are 2^x
def create_obstacle():
    row, col = pick_emptytile()
    board[row][col] = pow(2,random.randint(5,7))-1 # value of 31, 63, 127 for testing purpose

# pick a random empty tile
# return empty tile coord
def pick_emptytile():
    empty_cells = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                empty_cells.append((i, j))
    if empty_cells:
        row, col = random.choice(empty_cells)
        return row, col

#Merging and shifting of tiles
def move_left(board):
    for row in board:
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                row[i] *= 2
                row[i + 1] = 0

        row[:] = [tile for tile in row if tile != 0] + [0]

#Identify keys pressed w/ Arrow key prefix
def get_arrow_key():
    while True:
        key = ord(msvcrt.getch())
        if key == 224: 
            key = ord(msvcrt.getch())
            if key == 75:
                return 'left'
            elif key == 77:
                return 'right'
            elif key == 80:
                return 'down'
            elif key == 72:
                return 'up'

#Transposes tiles
def transpose_board(board):
    transposed = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    return transposed

#Movement of tiles based on input from get_arrow_key(), does not work 100%
def move(board, direction):
    if direction == 'left':
        move_left(board)
    elif direction == 'right':
        board[:] = [row[::-1] for row in board]
        move_left(board)
        board[:] = [row[::-1] for row in board]
    elif direction == 'down':
        board[:] = transpose_board(board)
        board[:] = [row[::-1] for row in board]
        move_left(board)
        board[:] = [row[::-1] for row in board]
        board[:] = transpose_board(board)
    elif direction == 'up':
        board[:] = transpose_board(board)
        move_left(board)
        board[:] = transpose_board(board)

def get_highest_tile(board):
    highest_tile = max(max(row) for row in board)
    return highest_tile

# each tile, from left to right, from top to bottom, assigned id of 0 to 15
# id_to_coord() converts id to the coord of the grid
# eg id 5 -> grid[1][1]
def id_to_coord(id):
    a = math.floor(id/4)
    b = id % 4
    return [a,b]

def clear_screen():
    os.system("cls")
