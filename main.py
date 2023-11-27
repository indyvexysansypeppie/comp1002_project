import boardcontrol as bcon

bcon.initialBoard()

score = 0
highest_tile = 0

while True:
    # bcon.clear_screen()
    bcon.print_board()
    print("Score:", score)
    print("Highest Tile:", highest_tile)
    direction = bcon.get_arrow_key()
    bcon.move(direction)
    bcon.create_tile()