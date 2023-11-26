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
    
    # create 2 obstacles
    for i in range(2):
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

# each tile, from left to right, from top to bottom, assigned id of 0 to 15
# id_to_coord() converts id to the coord of the grid
# eg id 5 -> grid[1][1]
def id_to_coord(id):
    a = math.floor(id/4)
    b = id % 4
    return [a,b]

def clear_screen():
    os.system("cls")
