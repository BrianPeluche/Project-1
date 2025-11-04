#puzzleTurns.py
from puzzle.tilePuzzle import PuzzleState


class Turns:
    # Constructor to initialize the Turns class
    def __init__(self, initialState, cost=0, goal=None):
        self.initialState = initialState
        self.cost = cost
        # If no goal specified, use default 8-puzzle goal
        if goal is None:
            size = initialState.boardSize
            self.goal = list(range(1, size * size)) + [0]
        else:
            self.goal = goal

    def is_goal(self, state):
        """Check if state matches goal configuration"""
        return state.board == self.goal

    def grid(self, state):
        """Display state as grid with 'b' for blank"""
        out = []
        for r in range(state.boardSize):
            row = []
            for c in range(state.boardSize):
                v = state.board[r * state.boardSize + c]
                row.append("b" if v == 0 else str(v))
            out.append(" " + " ".join(row))
        return out

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
        else:
            return False

    # Method to generate all possible tile moves from the current state
    def tileMoves(self, currState):
        moves = []
        size = currState.boardSize
        directions = ['up', 'down', 'left', 'right']
        for direction in directions:
            if self.possibleMoves(currState, direction):
                newState = currState.moveTile(direction, size)
                newState.prevState = currState
                moves.append((direction, newState))
                self.cost += 1
        return moves