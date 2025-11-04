#algorithm/uniformSearch.py
from puzzle.puzzleProblem import Problem

class uniformSearch:
    def __init__(self, initialState):
        self.initialState = initialState
        self.problem = Problem(initialState, cost=0)

    def uniformCostSearch(self):
        levels = [[self.initialState]]
        goalState = None

        while True:
            next_level = []
            for state in levels[-1]:
                if state.foundGoalState(state.boardSize):
                    goalState = state
                    break

                moves = self.problem.tileMoves(state)
                for _, new_state in moves:
                    next_level.append(new_state)

            if goalState is not None:
                break
            if not next_level:
                print("No solution found.")
                return None

            levels.append(next_level)

        cost = self.printSolution(goalState)
        totalNodes = sum(len(level) for level in levels)
        print("The maximum number of nodes in the queue at any one time: ", totalNodes)
        print("The depth of the goal node was ", cost)
        return
    
    def printSolution(self, currState):
        path = []
        while currState is not None and currState.prevState is not None:
            path.append(currState)
            currState = currState.prevState
        if currState is not None:
            path.append(currState)
        path.reverse()

        i = 0
        for state in path:
            if i == 0:
                print("\nStep:", i, ", Initial State")
                state.printBoard()
            else:
                print("\nStep:", i, ", Move empty tile", state.direction)
                state.printBoard()
            i += 1
        print("\nGOALL!!!!")
        print("\nTo solve this problem the search algorithm expanded a total of", i - 1, "nodes.")
        return i - 1