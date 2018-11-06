import numpy as np

class CYKAlgo:
    def __init__(self, G):
        """ initilizes with the grammar G
        """
        self.G = G

    def membership(self, w):
        # V = generate(w)
        # if((check(V)) {
        #     return true
        # }
        # return false;
        """
        let the input be a string I consisting of n characters: a1 ... an.
        let the grammar contain r nonterminal symbols R1 ... Rr, with start symbol R1.
        let P[n,n,r] be an array of booleans. Initialize all elements of P to false.
        for each s = 1 to n
            for each unit production Rv -> as
                set P[1,s,v] = true
        for each l = 2 to n -- Length of span
            for each s = 1 to n-l+1 -- Start of span
                for each p = 1 to l-1 -- Partition of span
                    for each production Ra -> Rb Rc
                        if P[p,s,b] and P[l-p,s+p,c] then set P[l,s,a] = true
        if P[n,1,1] is true then
            I is member of language
        else
            I is not member of language
        """
        n = len(w)
        r = len(self.G.productions)
        P = dict()
        # initialization
        for s in range(n):
            for t in range(n):
                for (v, production) in self.G.productions.items():
                    P[t,s,v] = False 

        # unit production Rv -> a
        for s in range(n):
            for (v, production) in self.G.productions.items():
                if w[s] in production["terminals"]:
                    P[0,s,v] = True   
    
        # Productions A -> BC
        for l in range(1,n):
            for s in range(n-l+1):
                for p in range(l-1):
                    for (v, production) in self.G.productions.items():
                        variables = production['variables']
                        if(len(variables) > 0):
                            b,c = tuple(variables[0])
                            print("{}->{}{} ; p={} ; s={}; l={}; P[p,s,b]={}; P[l-p,s+p,c]".format(v,b,c,p,s,l, P[p,s,b], P[l-p,s+p,c]))
                            if(P[p,s,b] and P[l-p,s+p,c]):
                                P[l,s,v] = True
        # print(P)
        _,_,S = next(iter(P))
        print((n-1,0,S))
        if(P[n-1,0,S]):
            print("True")
            return True
        else:
            print("False")
            return False
            