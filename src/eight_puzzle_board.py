import numpy as np

class Eight_Puzzle_Board():
    def __init__(self, n):
        self.size = n
        matrix = np.arange(n * n).reshape(n, n)
        self.board = np.random.permutation(matrix.ravel()).reshape(n, n)

    def to_string(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.board])
    
    def clone(self):
        new_board = Eight_Puzzle_Board(self.size)
        new_board.board = np.copy(self.board)
        return new_board

    def in_bounds(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size
    
    def get_blank_tile_position(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return (i, j)
        return None
    
    def get_possible_moves(self):
        moves = []
        x, y = self.get_blank_tile_position()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if self.in_bounds(new_x, new_y):
                moves.append((new_x, new_y))
        return moves
    
    def move_piece(self, piece):
        x, y = self.get_blank_tile_position()
        if self.in_bounds(piece[0], piece):
            self.board[x][y], self.board[piece[0]][piece[1]] = self.board[piece[0]][piece[1]], self.board[x][y]
    
    def get_piece_correct_position(self, piece):
        return (piece // self.size, piece % self.size)
    
    def is_solved(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != i * self.size + j:
                    return False
        return True
    
    def get_manhattan_distance(self):
        distance = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != 0:
                    correct_x, correct_y = self.get_piece_correct_position(self.board[i][j])
                    distance += abs(i - correct_x) + abs(j - correct_y)
        return distance
        
    

