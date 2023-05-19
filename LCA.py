# import RMQ in here

class LCA:
    def __init__(self, root, graph):
        self.time = [-1] * len(graph)
        self.path = [-1] * len(graph)
        self.dist = [-1] * len(graph)
        P = [-1] * len(graph)
        self.dist[root] = 0
        t = -1
        dfs = [root]
        while dfs:
            node = dfs.pop()
            self.path[t] = P[node]
            self.time[node] = t = t + 1
            for nei in graph[node]:
                if self.time[nei] == -1:
                    P[nei] = node
                    self.dist[nei] = self.dist[P[nei]] + 1
                    dfs.append(nei)
        self.rmq = RangeQuery(self.time[node] for node in self.path)

    def __call__(self, a, b):
        if a == b:
            return a
        a = self.time[a]
        b = self.time[b]
        if a > b:
            a, b = b, a
        return self.path[self.rmq.query(a, b)]
    
    def getDist(self, a, b):
        return self.dist[a] + self.dist[b] - 2 * self.dist[self.__call__(a, b)]
