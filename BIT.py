class BIT:
    def __init__(self, n):
        self.n = n + 1
        self.a = [0] * self.n

    def update(self, i, val):
        while i < self.n:
            self.a[i] += val
            i += (i & (-i))

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.a[i]
            i -= (i & (-i))
        return s
