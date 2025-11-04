#tilePuzzle.py
class PuzzleNode:
    # Constructor to initialize the puzzle node with A* search properties
    def __init__(self, board, prevState=None, boardSize=3, direction=None, g_cost=0, h_cost=0): 
        self.board = board
        self.prevState = prevState
        self.boardSize = boardSize
        self.direction = direction
        # A* search properties
        self.g = g_cost  # cost from start to this node
        self.h = h_cost  # heuristic estimate to goal
        self.f = g_cost + h_cost  # total estimated cost

    def __lt__(self, other):
        # For heapq comparison in A* search
        return self.f < other.f

    # Method to find the position of the empty tile (0)
    def findEmptyTile(self):
        return self.board.index(0)

    # Method to get the (row, col) position of the empty tile
    def emptyTilePos(self, size):
        row = self.findEmptyTile() // size
        col = self.findEmptyTile() % size
        return (row, col)
    
    # Method to check if the current state is the goal state
    def foundGoalState(self, size):
        numTiles = size * size
        goalState = list(range(1, numTiles)) + [0]
        return self.board == goalState
    
    # Method to move the empty tile in a specified direction
    def moveTile(self, direction, size):
        row, col = self.emptyTilePos(size)
        newRow, newCol = row, col

        if direction == 'up':
            newRow -= 1
        elif direction == 'down':
            newRow += 1
        elif direction == 'left':
            newCol -= 1
        elif direction == 'right':
            newCol += 1
        else:
            return None

        if 0 <= newRow < size and 0 <= newCol < size:
            newEmptyTile = newRow * size + newCol
            newBoard = self.board[:]
            newBoard[self.findEmptyTile()], newBoard[newEmptyTile] = newBoard[newEmptyTile], newBoard[self.findEmptyTile()]
            return PuzzleNode(newBoard, self, size, direction)
        else:
            return None
        
    # Method to display the board state
    def printBoard(self):
        size = self.boardSize
        for i in range(size):
            row = self.board[i*size:(i+1)*size]
            print(" ".join(map(str, row)))
        