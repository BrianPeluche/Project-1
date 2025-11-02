#titlePuzzle
class PuzzleState:

    # Constructor to initialize the puzzle state
    def __init__(self, board, prevState, boardSize, direction): 
        self.board = board
        self.prevState = prevState
        self.boardSize = boardSize
        self.direction = direction

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
            return PuzzleState(newBoard, self, size, direction)
        else:
            return None
        
    # Method to display the board state
    def printBoard(self):
        size = self.boardSize
        for i in range(size):
            print(self.board[i*size:(i+1)*size])
        