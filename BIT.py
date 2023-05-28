from math import log2
 
 
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
 
    def upper_bound(self, v):
        curr, prev_sm = 0, 0
        for i in range(int(log2(self.n)), -1, -1):
            if self.a[curr + (1 << i)] + prev_sm < v:
                curr += (1 << i)
                prev_sm += self.a[curr]
        return curr + 1
