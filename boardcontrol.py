import os, math, random

boardState = []

def initialBoard():
    # generate the empty 2d grid
    for i in range(4):
        boardState.append([])
        for j in range(4):
            boardState[i].append(" ")
    
    # create 2 tiles to begin
    for i in range(2):
        create_tile()
    
    # create 2 obstacles
    for i in range(2):
        create_obstacle()

    print_board(boardState)

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
<<<<<<< HEAD
    a = pick_emptytile()
    boardState[a[0]][a[1]] = pow(2,random.randint(1,2)) # 2^1=2; 2^2=4
=======
    empty_cells = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                empty_cells.append((i, j))
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = random.choice([2, 4])
    pass
>>>>>>> ed56c5f0562194c291e3a3e91f706e9f5e82a8a4

# create an obstacle
# obstacle values are 2^x-1 to differenciate from tiles which are 2^x
def create_obstacle():
    a = pick_emptytile()
    boardState[a[0]][a[1]] = pow(2,random.randint(5,7))-1 # value of 31, 63, 127 for testing purpose

# pick a random empty tile
def pick_emptytile():
    while True:
        a = id_to_coord(random.randint(0,15))
        if boardState[a[0]][a[1]] != " ": #if space is already occupied
            continue
        else:
            break
    return a

# each tile, from left to right, from top to bottom, assigned id of 0 to 15
# id_to_coord() converts id to the coord of the grid
# eg id 5 -> grid[1][1]
<<<<<<< HEAD
def id_to_coord(id):
    a = math.floor(id/4)
    b = id % 4
    return [a,b]

def clear_screen():
    os.system("cls")
=======
def id_to_coord():
    pass
>>>>>>> ed56c5f0562194c291e3a3e91f706e9f5e82a8a4
