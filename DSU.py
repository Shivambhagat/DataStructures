class DisjointSet:

    def __init__(self, n):
        self.parent = [-1 for _ in range(n + 1)]

    def find(self, s):
        if self.parent[s] == -1:
            return s
        self.parent[s] = self.find(self.parent[s])
        return self.parent[s]

    def merge(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)
        self.parent[x_set] = y_set
