#problem.py
class Problem:

    def is_goal(self, state):
        return state == self.goal

    def __init__(self, initial, goal = None, n = 3):
            self.initial = tuple(initial)
            self.n = n
            if goal is None:
                # 1..(n*n-1), then 0
                self.goal = tuple(list(range(1, n * n)) + [0])
            else:
                self.goal = tuple(goal)

    def grid(self, state):
        out = []
        for r in range(self.n):
            row = []
            for c in range(self.n):
                v = state[r * self.n + c]
                if v == 0:
                    row.append("b")
                else :
                    row.append(str(v))
            out.append(" " + " ".join(row))
        return out

    def neighbors(self, state):
        N = self.n
        i = state.index(0)
        r, c = divmod(i, N)
        result = [] 
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                j = nr * N + nc
                b = list(state)
                b[i], b[j] = b[j], b[i]
                result.append(tuple(b))
        return result
