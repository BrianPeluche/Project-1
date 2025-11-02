# heuristic.py
import heapq
import math

def euclidean(s, goal):
    dist = 0.0
    for idx, val in enumerate(s):
        if val == 0:
            continue
        cur_r, cur_c = divmod(idx, 3) #divosor and quotient
        goal_idx = goal.index(val)
        goal_r, goal_c = divmod(goal_idx, 3)
        dist += math.sqrt((cur_r - goal_r) **2 + (cur_c - goal_c) **2)
    return dist

def count(s,goal):
    c = 0 
    #solved_puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    for i in range(len(s)): 
        if s[i] != 0 and s[i] != goal[i]: # if it doenst match increment c += 1 return c
            c += 1
    return c
    

def a_star(problem, h_func, trace=True):
    start = problem.initial
    g_best = {start: 0}
    h0 = h_func(start, problem.goal)
    # (f, h, tie, state)
    pq = [(h0, h0, 0, start)]
    max_frontier = 1
    nodes_expanded = 0
    closed = set()
    counter = 0

    while pq:
        max_frontier = max(max_frontier, len(pq))
        f, curr_h, _, s = heapq.heappop(pq)
        if s in closed:
            continue
        closed.add(s)
        g = g_best[s]

        if trace:
            print(f'The best state to expand with  g(n) = {g} and h(n) = {curr_h} is…')
            for line in problem.grid(s):
                print(line)
            print('Expanding this node…\n')

        if problem.is_goal(s):
            print("Goal!!!")
            return g, nodes_expanded, max_frontier

        nodes_expanded += 1

        for next_state in problem.neighbors(s):
            new_g = g + 1
            if next_state not in g_best or new_g < g_best[next_state]:
                g_best[next_state] = new_g
                new_h = h_func(next_state, problem.goal)
                counter += 1
                heapq.heappush(pq, (new_g + new_h, new_h, counter, next_state))

    return -1, nodes_expanded, max_frontier