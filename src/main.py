from eight_puzzle_board import Eight_Puzzle_Board
from eight_puzzle_IA import Solve
import time

def main():
    n = 3  # Size of the board (3x3 for the 8-puzzle)
    puzzle_board = Eight_Puzzle_Board(n)

    # Print the initial state of the board
    print("Initial Board:")
    print(puzzle_board.to_string())

    # Solve the puzzle
    moves = Solve(puzzle_board)

    # Print the solution
    if moves is not None:
        print(f"Solution found! Moves: {len(moves)}")
        input("Press Enter to see the solution step by step...")
        for move in moves:
            print("\033[H\033[J", end="")  # Clear the console
            puzzle_board.move_piece(move)
            print(puzzle_board.to_string())
            time.sleep(1.2)  # Optional: Add a delay to visualize the moves            
    else:
        print("No solution found.")





main()