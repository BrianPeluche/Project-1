class puzzleState:

    # Constructor to initialize the puzzle state
    def init(self, board, emptyTile, numMoves, prevState, boardSize): 
        self.board = board
        self.emptyTile = emptyTile
        self.numMoves = numMoves
        self.prevState = prevState
        self.boardSize = boardSize

    # Method to find the position of the empty tile (0)
    def findEmptyTile(self):
        self.board.index(0)
        return self.board.index(0)
    
    # Method to get the (row, col) position of the empty tile
    def emptyTilePos(self, size):
        row = self.emptyTile // size
        col = self.emptyTile % size
        return (row, col)
    
    # Method to check if the current state is the goal state
    def foundGoalState(self, size):
        numTiles = size * size
        goalState = list(range(1, numTiles)) + [0]
        return self.board == goalState
    
    # Method to move the empty tile in a specified direction
    def moveTile(self, direction, size):
        row, col = self.emptyTilePos()
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
            newBoard[self.emptyTile], newBoard[newEmptyTile] = newBoard[newEmptyTile], newBoard[self.emptyTile]
            return puzzleState(newBoard, newEmptyTile, self.numMoves + 1, self, size)
        else:
            return None
        
        