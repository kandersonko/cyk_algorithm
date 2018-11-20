import numpy as np


class CYKAlgo:
    def __init__(self, G):
        """ initilizes with the grammar G
        """
        self.G = G

    def membership(self, w):
        B = dict()
        X = dict()
        V = [i for i in self.G.productions.keys()]
        for k,v in enumerate(self.G.productions.keys()):
            X[v]=k
        n = len(w)
        r = len(X)
        # initialize all items in B to false
        for i in range(n):
            for j in range(n):
                for k in range(r):
                    B[i, j, k] = False

        # production A->a
        for i in range(n):
            for j,v in enumerate(X):
                if w[i] in self.G.productions[v]["terminals"]:
                    B[i, i, j] = True

        # production A -> BC
        for i in range(1, n):
            for L in range(n-i+1):
                R = L + i - 1
                for M in range(L+1, R):
                    for v in range(r):
                        P=self.G.productions[V[v]]
                        variables = P["variables"]
                        if(len(variables)):
                            b, c = tuple(variables[0])
                            s, t = X[b],X[c]
                            if(B[L, M-1, s] and B[M, R, t]):
                                B[L, R, v] = True

        r = n-1
        for i in range(r):
            if(B[r, n-1, i]):
                return True
        return False