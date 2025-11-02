#heuristic.py
import heapq # proirity queue
import math
goal =  (1, 2, 3, 4, 5, 6, 7, 8, 0)

def euclidean(s):
    dist = 0.0
    for idx, val in enumerate(s):
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
            v = state[r * 3 + c] # finds number in grid
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
        if s[i] != 0 and s[i] != solved_puzzle[i]: # if it doenst match increment
            c += 1
    return c

def neighbors(state):
    N = 3
    i = state.index(0)
    r, c = divmod(i, N)
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            j = nr * N + nc
            b = list(state)
            b[i], b[j] = b[j], b[i]
            yield tuple(b)

def a_star(initial, h_func, trace = True): # 

    counter = 0
    g_best = {initial: 0}
    h0 = h_func(initial)
    pq = [(h0, h0, counter, initial)]  # (f, h, tie, state)
    max_frontier = 1
    nodes_expanded = 0
    closed = set()

    while pq:
        max_frontier = max(max_frontier, len(pq))
        f, cur_h, _, s = heapq.heappop(pq)
        if s in closed:
            continue
        closed.add(s)
        g = g_best[s]

        if trace:
            print(f'The best state to expand with  g(n) = {g} and h(n) = {cur_h} is…')
            for line in grid(s):
                print(line)
            print('Expanding this node…\n')

        if s == goal:
            print("Goal!!!")
            return g, nodes_expanded, max_frontier  # depth, expanded, maxQ

        nodes_expanded += 1

        for ns in neighbors(s):
            ng = g + 1  # unit step cost
            if ns not in g_best or ng < g_best[ns]:
                g_best[ns] = ng
                nh = h_func(ns)
                counter += 1
                heapq.heappush(pq, (ng + nh, nh, counter, ns))

    # Unsolvable or exhausted
    return -1, nodes_expanded, max_frontier