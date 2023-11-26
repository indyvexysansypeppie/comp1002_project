import boardcontrol as bcon

bcon.initialBoard()

score = 0
highest_tile = 0

while True:
    print_board(board)
    print("Score:", score)
    print("Highest Tile:", highest_tile)
    direction = get_arrow_key()
    move(board, direction)
