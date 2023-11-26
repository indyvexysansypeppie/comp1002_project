import os, math, random, keyboard

board = []
score = 0

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
    create_obstacle(2)

    print(f"Score: {score}",end="\n\n")
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
    # ┌─────┬─────┬─────┬─────┐
    # │     │     │     │     │
    # ├─────┼─────┼─────┼─────┤
    # │     │     │     │     │
    # ├─────┼─────┼─────┼─────┤
    # │     │     │     │     │
    # ├─────┼─────┼─────┼─────┤
    # │     │     │     │     │
    # └─────┴─────┴─────┴─────┘

    # just bad
    for i in range(4):
        for j in range(4):
            print(a[i][j],end="\t")
            print("|",end="")
        print()
        print("--------------------")

def turn():
    dir = input("play input wasd\n")

# coord of tile, direction of sliding
def slide_tile(row,col,dir):
    rowDir, colDir = 0,0
    if dir == "w": # -row
        rowDir = -1
    elif dir == "s": # +row
        rowDir = 1
    elif dir == "a": # -col
        colDir = -1
    elif dir == "d": # +col
        colDir = 1

    # keeps running as long as tile is sliding on empty tiles
    while True:
        targetVal = board[row+rowDir][col+colDir] # value of the target cell
        if row+rowDir < 0 or col+colDir < 0: # out of bounds
            break
        elif targetVal == 0: # target cell is empty
            # move the tile
            board[row+rowDir][col+colDir] = board[row][col]
            board[row][col] = 0
        elif not(isinstance(math.log2(targetVal),int)): # target cell is obstacle
            break
        elif isinstance(math.log2(targetVal),int): # target cell is tile
            if targetVal != board[row][col]: # target cell is not same value
                break
            elif targetVal == board[row][col]: # target cell is same value (merge)
                pass

# create a tile of either value 2 or 4 on an empty space
def create_tile():
    row, col = pick_emptytile()
    board[row][col] = random.choice([2, 4])
    # board[a[0]][a[1]] = pow(2,random.randint(1,2)) # 2^1=2; 2^2=4

# create an obstacle
# obstacle values are 2^x-1 to differenciate from tiles which are 2^x
def create_obstacle(n=1):
    row, col = pick_emptytile()
    power = random.sample(range(5,8),n) # no 2 obstacles have unique value
    for i in power:
        board[row][col] = pow(2,i)-1 # value of 31, 63, 127 for testing purpose

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

# each tile, from left to right, from top to bottom, assigned id of 0 to 15
# id_to_coord() converts id to the coord of the grid
# eg id 5 -> grid[1][1]
def id_to_coord(id):
    a = math.floor(id/4)
    b = id % 4
    return [a,b]

def clear_screen():
    os.system("cls")