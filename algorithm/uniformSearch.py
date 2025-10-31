from puzzle.tilePuzzle import PuzzleState
from puzzle.puzzleTurns import Turns

class uniformSearch:
    def __init__(self, initialState):
        self.initialState = initialState

    def moves(self, currState, puzzleMoves):
        return puzzleMoves + self.puzzleTurns.tileMoves(currState)
    
    def uniformCostSearch(self):
        puzzleMoves = []
        currState = self.initialState
        while not currState.foundGoalState(currState.boardSize):
            puzzleMoves = self.moves(currState, puzzleMoves)
            currState = puzzleMoves.index(currState + 1)
        self.printSolution(currState)
        return currState
    
    def printSolution(self, currState):
        path = []
        while currState is not None and currState.prevState is not None:
            path.append(currState)
            currState = currState.prevState
        if currState is not None:
            path.append(currState)
        path.reverse()

        i = 1
        for state in path:
            print("\nStep:", i, ", Move empty tile", state.direction)
            state.printBoard()
            i += 1