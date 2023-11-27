import os, math, random, msvcrt

board = []
score = 0
highest_tile = 0

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

    # print(f"Score: {score}",end="\n\n")
    # print_board()

def print_board():
    # board format:
    # ┌─────┬─────┬─────┬─────┐
    # │     │     │     │     │
    # ├─────┼─────┼─────┼─────┤
    # │     │     │     │     │
    # ├─────┼─────┼─────┼─────┤
    # │     │     │     │     │
    # ├─────┼─────┼─────┼─────┤
    # │     │     │     │     │
    # └─────┴─────┴─────┴─────┘
    
    i=0
    print("┌─────┬─────┬─────┬─────┐")
    while True:
        print("│",end="")
        for j in range(4):
            prefix, suffix = "", ""
            
            if board[i][j] == 0:
                print("     ",end="")
            
            elif math.ceil(math.log2(board[i][j])) != math.floor(math.log2(board[i][j])): # obstacle
                spaceFix = 5-len(str(board[i][j]))-2
                if spaceFix != 0:
                    for k in range(math.floor(spaceFix/2)): prefix+=" "
                    for k in range(math.ceil(spaceFix/2)): suffix+=" "
                print(f"{prefix}[{board[i][j]}]{suffix}",end="")
            
            else: # tiles
                spaceFix = 5-len(str(board[i][j]))
                if spaceFix != 0:
                    for k in range(math.floor(spaceFix/2)): prefix+=" "
                    for k in range(math.ceil(spaceFix/2)): suffix+=" "
                print(f"{prefix}{board[i][j]}{suffix}",end="")

            print("│",end="")
        print()
        i+=1
        if i > 3:
            break
        print("├─────┼─────┼─────┼─────┤")
    print("└─────┴─────┴─────┴─────┘")


# region turn()
# def turn():
    # dir = get_arrow_key()
    # move(dir)
    # print_board()
# endregion

# coord of tile, direction of sliding
# !!!!!!!!!defunct!!!!!!!!!
# region slide_tile()
# def slide_tile(row,col,dir):
    # rowDir, colDir = 0,0
    # if dir == "up": # -row
    #     rowDir = -1
    # elif dir == "down": # +row
    #     rowDir = 1
    # elif dir == "left": # -col
    #     colDir = -1
    # elif dir == "right": # +col
    #     colDir = 1

    # # keeps running as long as tile is sliding on empty tiles
    # while True:
    #     targetVal = board[row+rowDir][col+colDir] # value of the target cell
    #     if row+rowDir < 0 or col+colDir < 0: # out of bounds
    #         break
    #     elif targetVal == 0: # target cell is empty
    #         # move the tile
    #         board[row+rowDir][col+colDir] = board[row][col]
    #         board[row][col] = 0
    #     elif not(isinstance(math.log2(targetVal),int)): # target cell is obstacle
    #         break
    #     elif isinstance(math.log2(targetVal),int): # target cell is tile
    #         if targetVal != board[row][col]: # target cell is not same value
    #             break
    #         elif targetVal == board[row][col]: # target cell is same value (merge)
    #             board[row+rowDir][col+colDir] = board[row][col]
    #             break
# endregion

# create a tile of either value 2 or 4 on an empty space
def create_tile():
    row, col = pick_emptytile()
    board[row][col] = random.choice([2, 4])
    # board[a[0]][a[1]] = pow(2,random.randint(1,2)) # 2^1=2; 2^2=4

# create an obstacle
# obstacle values are 2^x-1 to differenciate from tiles which are 2^x
def create_obstacle(n=1):
    power = random.sample(range(5,8),n) # no 2 obstacles have unique value
    for i in power:
        row, col = pick_emptytile()
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

#Merging and shifting of tiles
def move_left():
    output=[]
    global board,score,highest_tile
    for row in board:
        splitRow = [[]]
        obstacles = {}
        n=0
        for i in range(4): # check each cell in row
            if row[i] == 0: # skip over 0s
                continue
            elif math.ceil(math.log2(row[i])) != math.floor(math.log2(row[i])): # check if value != 2^x aka obstacle
                n+=1
                obstacles[i]=row[i]
                # print(obstacles)
                splitRow.append([])
                continue
            splitRow[n].append(row[i])

        # print(splitRow)

        outputRow = []
        i=0
        while True:
            tileCount = 0 # count no of tiles in that split list
            if splitRow[i] != []: # empty lists are discarded
                for j in splitRow[i]:

                    # sliding
                    outputRow.append(j)
                    tileCount += 1
                    
                    # merging
                    # should also increase score & break obstacle here
                    if (tileCount >= 2) and (outputRow[-1] == outputRow[-2]): # if there are >2 tiles and both tiles are same value
                        outputRow[-2] *= 2
                        outputRow[-1] = 0
                        tileCount-1

                        score += outputRow[-2]
                        if(outputRow[-2] >= highest_tile):
                            highest_tile = outputRow[-2]
            i+=1
            if i == len(splitRow):
                break
            # spaces = next(iter(obstacles)) # retrieve index of obstacle
            # for j in range(spaces-tileCount): outputRow.append(0)
            # outputRow.append(obstacles[spaces])

            obsIDs = list(obstacles.keys()) # get list of the obstacles' indexes
            for j in range(obsIDs[i-1]-len(outputRow)): outputRow.append(0) # fill in empty spaces between tile & obstacles
            outputRow.append(obstacles[obsIDs[i-1]])

        for k in range(4-len(outputRow)): outputRow.append(0)
        output.append(outputRow)
    board=output.copy()

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
def move(direction):
    if direction == 'left':
        move_left()
    elif direction == 'right':
        board[:] = [row[::-1] for row in board]
        move_left()
        board[:] = [row[::-1] for row in board]
    elif direction == 'down':
        board[:] = transpose_board(board)
        board[:] = [row[::-1] for row in board]
        move_left()
        board[:] = [row[::-1] for row in board]
        board[:] = transpose_board(board)
    elif direction == 'up':
        board[:] = transpose_board(board)
        move_left()
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

def pass_score():
    global score
    return score

def pass_highest_tile():
    global highest_tile
    return highest_tile