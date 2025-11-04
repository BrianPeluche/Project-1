# heuristic.py
import heapq
import math
from puzzle.puzzleNode import PuzzleNode
from puzzle.puzzleProblem import Problem

def euclidean(state, problem):
    # Calculate Euclidean distance heuristic
    dist = 0.0
    goal = problem.goal
    for idx, val in enumerate(state.board):
        if val == 0:  # skip the blank tile; we don't measure distance for it
            continue
        cur_r, cur_c = divmod(idx, state.boardSize) # divisor and quotient
        goal_idx = goal.index(val)
        goal_r, goal_c = divmod(goal_idx, state.boardSize)
        dist += math.sqrt((cur_r - goal_r) **2 + (cur_c - goal_c) **2) # Euclidean distance
    return dist

def count(state, problem): # count how many tiles are not in the correct position
    """Count misplaced tiles heuristic"""
    c = 0
    goal = problem.goal
    for i in range(len(state.board)):
        if state.board[i] != 0 and state.board[i] != goal[i]:
            c += 1
    return c

def uniform_cost(state, problem):
    return 0

def a_star(initial_state, h_func, trace=True):
    # Set up initial state and Problem helper
    problem = Problem(initial_state)
    
    # Initialize A* search
    g_best = {tuple(initial_state.board): 0} # g_best[state] will store the cheapest known cost to reach state from the start
    h0 = h_func(initial_state, problem)
    initial_state.g = 0
    initial_state.h = h0
    initial_state.f = h0
    
    pq = [(h0, h0, 0, initial_state)]
    max_frontier = 1 # we will track how big the frontier (priority queue) got
    nodes_expanded = 0
    closed = set()
    counter = 0

    while pq: # keep looping going while there are states to explore
        max_frontier = max(max_frontier, len(pq))
        f, curr_h, _, s = heapq.heappop(pq)
        board_tuple = tuple(s.board)
        
        if board_tuple in closed: # if we've already expanded this state, skip it
            continue
            
        closed.add(board_tuple) # mark this state as done
        g = g_best[board_tuple] # g value (actual cost from start to this state)

        if problem.is_goal(s): # check if we reached the goal
            print("\nGOALL!!!!")
            print("\nTo solve this problem the search algorithm expanded a total of", nodes_expanded, "nodes.")
            print("The maximum number of nodes in the queue at any one time: ", max_frontier)
            print("The depth of the goal node was ", g)
            return

        if trace: # if trace is true, print what is happening
            print(f"The best state to expand with g(n) = {g} and h(n) = {curr_h} is...")
            for line in problem.grid(s):
                print(line)
            print("Expanding this node...\n")
            nodes_expanded += 1 # expanding node

        for _, next_state in problem.tileMoves(s): # otherwise, look at all the states we can reach in 1 move from s
            if next_state is None: # invalid move, no next state
                continue
                
            board_tuple = tuple(next_state.board)
            new_g = g + 1 # moving to a neighbor costs 1 more step
            
            if board_tuple not in g_best or new_g < g_best[board_tuple]: # if this path to neighbor is cheaper, save the path
                g_best[board_tuple] = new_g
                next_state.g = new_g
                next_state.h = h_func(next_state, problem) # how far this neighbor is from the goal
                next_state.f = new_g + next_state.h
                counter += 1
                heapq.heappush(pq, (next_state.f, next_state.h, counter, next_state)) # push the neighbor into the priority queue with its f = g + h

    print("No solution found.")
    return -1, nodes_expanded, max_frontier # return -1 if no solution