import numpy as np
import random

class Eight_Puzzle_Board():
    def __init__(self, n):
        self.size = n
        self.generate_board(n)

    def to_string(self):
        """
        Convert the board to a string representation.
        """
        board_str = ""
        
        for i in range(self.size):
            for j in range(self.size):
                board_str += f"{self.board[i][j]:2} "
        
            board_str += "\n"
    
        return board_str    
    def clone(self):
        """
        Create a deep copy of the board.
        """
        new_board = Eight_Puzzle_Board(self.size)
        new_board.board = np.copy(self.board)
        return new_board

    def generate_board(self, n, moves = 100):
        """
        Build a valid board by making a series of random moves.
        """
        self.board = np.arange(n * n).reshape((n, n))
        for _ in range(moves):
            possible_moves = self.get_possible_moves()
            move = random.choice(possible_moves)
            self.move_piece(move)
        
    def in_bounds(self, x, y):
        """
        Check if the given coordinates are within the bounds of the board.
        """
        return 0 <= x < self.size and 0 <= y < self.size
    
    def get_blank_tile_position(self):
        """
        Find the position of the blank tile (0) on the board.
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return (i, j)
        return None
    
    def get_possible_moves(self):
        """
        Get all possible moves.
        """
        moves = []
        x, y = self.get_blank_tile_position()   # Get the position of the blank tile
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy       # Position of adjacent tile
            if self.in_bounds(new_x, new_y):    # Check if the move is valid
                moves.append((new_x, new_y))    # Add the move to the list
        return moves
    
    def move_piece(self, piece):
        """
        Move a piece to the blank tile position.
        The piece is represented by its coordinates (x, y).
        """
        x, y = self.get_blank_tile_position()
        if self.in_bounds(piece[0], piece[1]):
            self.board[x][y], self.board[piece[0]][piece[1]] = self.board[piece[0]][piece[1]], self.board[x][y]
    
    def get_piece_correct_position(self, piece):
        """
        Get the correct position of a piece on the board.
        The piece is represented by its value.
        """
        return (piece // self.size, piece % self.size)
    
    def is_solved(self):
        """
        Check if the board is in the solved state.
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != i * self.size + j:
                    return False
        return True
    
    def get_manhattan_distance(self):
        """
        Calculate the Manhattan distance of the current board state.
        The Manhattan distance is the sum of the distances of each tile from its goal position.
        The distance is calculated as the sum of the absolute differences in the x and y coordinates.
        """
        distance = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != 0:
                    correct_x, correct_y = self.get_piece_correct_position(self.board[i][j])
                    distance += abs(i - correct_x) + abs(j - correct_y)
        return distance

    def __lt__(self, other):
        return self
    

