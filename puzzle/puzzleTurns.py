from puzzle.tilePuzzle import PuzzleState

class Turns:
    # Constructor to initialize the Turns class
    def init(self, initialState):
        self.initialState = initialState

    # Method to check possible moves from the current state
    def possibleMoves(self, currState, direction):
        size = currState.boardSize
        if direction == 'up':
            if currState.emptyTilePos(size)[0] == 0:
                return False
            else:
                return True
        elif direction == 'down':
            if currState.emptyTilePos(size)[0] == size-1:
                return False
            else:
                return True
        elif direction == 'left':
            if currState.emptyTilePos(size)[1] == 0:
                return False
            else:
                return True
        elif direction == 'right':
            if currState.emptyTilePos(size)[1] == size-1:
                return False
            else:
                return True

    # Method to generate all possible tile moves from the current state
    def tileMoves(self, currState):
        moves = []
        size = currState.boardSize
        directions = ['up', 'down', 'left', 'right']
        for direction in directions:
            if self.possibleMoves(currState, direction, size):
                newState = currState.moveTile(direction, size)
                moves.append((direction, newState))
        return moves