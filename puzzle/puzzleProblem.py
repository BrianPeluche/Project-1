#puzzleTurns.py
from puzzle.puzzleNode import PuzzleNode


class Problem:
    # Constructor to initialize the Problem class
    def __init__(self, initialState, cost=0):
        self.initialState = initialState
        self.cost = cost
        size = initialState.boardSize
        self.goal = list(range(1, size * size)) + [0]

    def is_goal(self, state):
        return state.board == self.goal

    def grid(self, state):
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
            return currState.emptyTilePos(size)[0] != 0
        elif direction == 'down':
            return currState.emptyTilePos(size)[0] != size - 1
        elif direction == 'left':
            return currState.emptyTilePos(size)[1] != 0
        elif direction == 'right':
            return currState.emptyTilePos(size)[1] != size - 1
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
                if newState is not None:
                    moves.append((direction, newState))
                    self.cost += 1
        return moves