import heapq # proirity queue
import math
from puzzle.tilePuzzle import PuzzleState
from puzzle.puzzleTurns import Turns

goal =  (1, 2, 3, 4, 5, 6, 7, 8, 0)

def euclidean(s):
    dist = 0.0
    for idx, val in enumerate(s.board):
        if val == 0:       # skip the blank
            continue
        cur_r, cur_c = divmod(idx, 3)          # where the tile is now
        goal_idx = goal.index(val)             # where the tile should go
        goal_r, goal_c = divmod(goal_idx, 3)
        dist += math.sqrt((cur_r - goal_r)**2 + (cur_c - goal_c)**2)
    return dist

def grid(state): # outputs the grid
    
    out = []
    for r in range(3):
        row = []
        for c in range(3):
            v = state.board[r * 3 + c] # finds number in grid
            if v == 0: # if 0 found then add b
                row.append("b")
            else: # turn number into string
                row.append(str(v))
        out.append(" " + " ".join(row)) # join the number strings
    return out

def count(s):
    c = 0
    solved_puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    for i in range (9):
        if s.board[i] != 0 and s.board[i] != solved_puzzle[i]: # if it doenst match increment
            c += 1
    return c

def a_star(initial, h_func, trace = True): # 
    # Convert initial tuple to PuzzleState if needed
    if isinstance(initial, tuple):
        initial_state = PuzzleState(list(initial), None, 3, None)
    else:
        initial_state = initial
    
    # Create Turns helper for move generation
    turns = Turns(initial_state, cost=0)

    counter = 0
    g_best = {tuple(initial_state.board): 0}
    h0 = h_func(initial_state)
    pq = [(h0, h0, counter, initial_state)]  # (f, h, tie, state)
    max_frontier = 1
    nodes_expanded = 0
    closed = set()

    while pq:
        max_frontier = max(max_frontier, len(pq))
        f, cur_h, _, s = heapq.heappop(pq)
        board_tuple = tuple(s.board)
        if board_tuple in closed:
            continue
        closed.add(board_tuple)
        g = g_best[board_tuple]

        if trace:
            print(f'The best state to expand with  g(n) = {g} and h(n) = {cur_h} is…')
            for line in grid(s):
                print(line)
            print('Expanding this node…\n')

        if s.foundGoalState(3):  # 3x3 puzzle
            print("\nGOALL!!!!")
            print("\nTo solve this problem the search algorithm expanded a total of", nodes_expanded, "nodes.")
            print("The maximum number of nodes in the queue at any one time: ", max_frontier)
            print("The depth of the goal node was ", g)
            return

        nodes_expanded += 1

        for _, ns in turns.tileMoves(s):
            if ns is None:
                continue
            board_tuple = tuple(ns.board)
            ng = g + 1  # unit step cost
            if board_tuple not in g_best or ng < g_best[board_tuple]:
                g_best[board_tuple] = ng
                nh = h_func(ns)
                counter += 1
                heapq.heappush(pq, (ng + nh, nh, counter, ns))

    # Unsolvable or exhausted
    print("No solution found.")
    return None