class Node:
    def __init__(self):
        self.links = [None for _ in range(26)]
        self.flag = False

    def is_present(self, ch):
        return self.links[ord(ch) - ord("a")] is not None

    def insert(self, ch):
        self.links[ord(ch) - ord("a")] = Node()

    def next(self, ch):
        return self.links[ord(ch) - ord("a")]

    def set_end(self):
        self.flag = True

    def end(self):
        return self.flag


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for v in word:
            if not node.is_present(v):
                node.insert(v)
            node = node.next(v)
        node.set_end()

    def search(self, word: str) -> bool:
        node = self.root
        for v in word:
            if not node.is_present(v):
                return False
            node = node.next(v)
        return node.end()
