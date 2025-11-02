#problem.py
class Problem:

    def is_goal(self, state): # True if the given state is the goal state
        return state == self.goal

    def __init__(self, initial, goal = None, size = 3): # Create a new puzzle problem.
            self.initial = tuple(initial)
            self.size = size # how many rows/cols the board has (default is 3 or 3x3)
            if goal is None:
                # 1..(n*n-1), then 0
                self.goal = tuple(list(range(1, size * size)) + [0])
            else: # if the user gave a custom goal, store it 
                self.goal = tuple(goal) 

    def grid(self, state): # prints the table
        out = []
        for r in range(self.size):
            row = []
            for c in range(self.size):
                tile_value = state[r * self.size + c]
                if tile_value == 0:
                    row.append("b")
                else :
                    row.append(str(tile_value))
            out.append(" " + " ".join(row))  # join the row into a string like "1 2 3"
        return out

    def neighbors(self, state): #  Given a state, return all states you can reach in 1 move.
        board_size = self.size
        i = state.index(0)
        r, c = divmod(i, board_size) # r,c = row and column of blank
        result = [] # we'll collect all neighbor states here

        for row_offset, col_offset in [(-1,0), (1,0), (0,-1), (0,1)]: # (-1,0) = up, (1,0) = down, (0,-1) = left, (0,1) = right
            new_row, new_col = r + row_offset, c + col_offset
            if 0 <= new_row < board_size and 0 <= new_col < board_size: # check that the new position is still inside the board
                j = new_row * board_size + new_col
                new_board = list(state) # make a mutable copy of the board so we can swap
                new_board[i], new_board[j] = new_board[j], new_board[i] # swap the blank (at i) with the tile at j
                result.append(tuple(new_board)) # store it as a tuple (so A* can hash it)
        return result
