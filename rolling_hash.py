class ComputeHash:

    def __init__(self, s, p, mod):
        n = len(s)
        self.hash = [0] * n
        self.inv_mod = [0] * n
        self.mod = mod
        self.p = p

        p_pow = 1
        hash_value = 0

        for i in range(n):
            c = ord(s[i]) - 97 + 1
            hash_value = (hash_value + c * p_pow) % self.mod
            self.hash[i] = hash_value
            self.inv_mod[i] = pow(p_pow, self.mod - 2, self.mod)
            p_pow = (p_pow * self.p) % self.mod

    def get_hash(self, l, r):
        if l == 0:
            return self.hash[r]
        window = (self.hash[r] - self.hash[l - 1]) % self.mod
        return (window * self.inv_mod[l]) % self.mod


class Hash:

    def __init__(self, s):
        self.hash_a = ComputeHash(s, 31, 10 ** 9 + 9)
        self.hash_b = ComputeHash(s, 37, 10 ** 9 + 7)

    def __getitem__(self, R: tuple) -> tuple:
        h1 = self.hash_a.get_hash(R[0], R[1])
        h2 = self.hash_b.get_hash(R[0], R[1])
        return h1, h2
