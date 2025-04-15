from eight_puzzle_board import Eight_Puzzle_Board
import heapq

def Solve(puzzle_board: Eight_Puzzle_Board):
    """
    Solve the 8-puzzle using the A* algorithm and return the moves needed to solve the puzzle.
    """
    heap = []         # Priority queue for A* algorithm based on f(n)
    visited = set()   # Set to keep track of visited states

    # Push the initial state into the heap
    # heap elements: (f(n), board, g(n), moves)

    heapq.heappush(heap, (puzzle_board.get_manhattan_distance(), puzzle_board, 0, []))  
    visited.add(puzzle_board.to_string())
    
    while heap:
        (f_n, current_board, g_n, moves) = heapq.heappop(heap)
        
        if current_board.is_solved():   # Check if the current board is the goal state
            return moves                # Return the moves to reach the goal state

        for move in current_board.get_possible_moves():     # Get all possible moves
            new_board = current_board.clone()               
            new_board.move_piece(move)                      # Make the move
            if new_board.to_string() not in visited:        # Check if the new board state has been visited
                visited.add(new_board.to_string())
                h_n = new_board.get_manhattan_distance()
                # Push the new state into the heap with f(n) = g(n) + h(n)
                heapq.heappush(heap, (g_n + 1 + h_n, new_board, g_n + 1, moves + [move]))   