from eight_puzzle_board import Eight_Puzzle_Board

def main():
    # Create an instance of the Eight_Puzzle_Board class
    n = 3  # Size of the board (3x3 for the 8-puzzle)
    puzzle_board = Eight_Puzzle_Board(n)

    # Print the initial state of the board
    print("Initial Board:")
    print(puzzle_board.to_string())

main()