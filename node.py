# node.py

class Node:
    def __init__(self, state, parent = None, g_cost = 0, h_cost = 0):
        self.state = state # the puzzle configuration
        self.parent = parent # the node we came from
        self.g = g_cost # cost from the start to this node
        self.h = h_cost # heuristic estimate from this node to the goal
        self.f = g_cost + h_cost # total estimated cost f(n) = g(n) + h(n)

    def __lt__(self, other):
        # lets heapq compare node objects
        return self.f < other.f