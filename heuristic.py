# heuristic.py
import heapq
import math

def euclidean(s, goal):
    dist = 0.0
    for idx, val in enumerate(s):
        if val == 0: # skip the blank tile; we don't measure distance for it
            continue
        cur_r, cur_c = divmod(idx, 3) # divosor and quotient
        goal_idx = goal.index(val)
        goal_r, goal_c = divmod(goal_idx, 3)
        dist += math.sqrt((cur_r - goal_r) **2 + (cur_c - goal_c) **2) # d = sqrt((x - x)^2 + (y - y)^2)
    return dist

def count(s,goal): # counts how many tiles are not in the correct position
    c = 0 
    #solved_puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    for i in range(len(s)): 
        if s[i] != 0 and s[i] != goal[i]: # if it doenst match increment c += 1 return c
            c += 1
    return c
    

def a_star(problem, h_func, trace = True):
    start = problem.initial
    g_best = {start: 0} # g_best[state] will store the cheapest known cost to reach state from the start
    h0 = h_func(start, problem.goal) # Heuristic start
    pq = [(h0, h0, 0, start)] # (f, h, tie, state)
    max_frontier = 1 # we will track how big the frontier (priority queue) got
    nodes_expanded = 0
    closed = set() # states we have already expanded
    counter = 0

    while pq: # keep looping going while there are states to explore
        #Is current frontier (len(pq))the max we’ve seen  (max_frontier), update it. If not, keep the old one
        max_frontier = max(max_frontier, len(pq)) 
        f, curr_h, tiee, s = heapq.heappop(pq) # for heapq.heappush(pq, (new_g + new_h, new_h, counter, next_state)), f and tire are ignored
        if s in closed: # if we've already expanded this state, skip it
            continue
        closed.add(s) # mark this state as done
        g = g_best[s] # g value (actual cost from start to this state)
        nodes_expanded += 1 # expanding node

        if trace: # if trace is true, print what is happening
            print(f"The best state to expand with  g(n) = ",g," and h(n) = ",curr_h," is...")
            for line in problem.grid(s):
                print(line)
            print("Expanding this node…\n")

        if problem.is_goal(s): # check if we reached the goal
            print("Goal!!!")
            return g, nodes_expanded, max_frontier# return the cost to reach the goal, how many we expanded, and the frontier 

        #nodes_expanded += 1

        for next_state in problem.neighbors(s): # otherwise, look at all the states we can reach in 1 move from s
            new_g = g + 1 # moving to a neighbor costs 1 more step
            if next_state not in g_best or new_g < g_best[next_state]: # if we've never seen this neighbor or found a cheaper path to it
                g_best[next_state] = new_g # save the cheaper path
                new_h = h_func(next_state, problem.goal) # how far this neighbor is from the goal
                counter += 1
                heapq.heappush(pq, (new_g + new_h, new_h, counter, next_state)) # push the neighbor into the priority queue with its f = g + h

    return -1, nodes_expanded, max_frontier # return -1 if no solution