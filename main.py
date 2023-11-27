import boardcontrol as bcon

bcon.initialBoard()

score = 0
highest_tile = 0

while True:
    try:
        if highest_tile == 2048:
            print("You won")
            break

        bcon.breakObstacle()
        bcon.clear_screen()
        bcon.print_board()
        print("Score:", score)
        print("Highest Tile:", highest_tile)
        direction = bcon.get_arrow_key()
        bcon.move(direction)
        bcon.create_tile()
        score = bcon.pass_score()
        highest_tile = bcon.pass_highest_tile()
        
    except TypeError:
        print("Out of Blocks!")
        break