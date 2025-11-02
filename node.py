# node.py

class Node:
    def __init__(self, state, parent = None, g = 0, h = 0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        # lets heapq compare nodes
        return self.f < other.f