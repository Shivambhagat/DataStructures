from math import log2


class RangeQuery:
    def __init__(self, a, func=min):
        self.n = len(a)
        self.func = func
        self.st = [[0 for _ in range(self.n + 1)] for _ in range(20)]

        self.st[0] = a.copy()
        for i in range(1, self.n + 1):
            j = 0
            while j + (1 << i) <= self.n:
                self.st[i][j] = self.func(self.st[i - 1][j], self.st[i - 1][j + (1 << (i - 1))])
                j += 1

    def query(self, L, R):
        i = int(log2(R - L + 1))
        return self.func(self.st[i][L], self.st[i][R - (1 << i) + 1])
