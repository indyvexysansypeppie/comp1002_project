import os, math

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

    # just bad
    for i in range(4):
        for j in range(4):
            print(a[i][j],end="\t")
            print("|",end="")
        print()
        print("--------------------")

# create a tile of either value 2 or 4 on an empty space
def create_tile():
    pass

# create an obstacle
def create_obstacle():
    pass

# each tile, from left to right, from top to bottom, assigned id of 0 to 15
# id_to_coord() converts id to the coord of the grid
# eg id 5 -> grid[1][1]
def id_to_coord():
    pass