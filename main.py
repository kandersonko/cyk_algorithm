from grammar import Grammar
from CYKAlgo import CYKAlgo


def main():
    G = Grammar("S->AB;A->BB|a;B->AB|b")
    print(G.rules)
    print(G.productions)

    w = "aabbb"
    cykAlgo = CYKAlgo(G)
    cykAlgo.membership(w)

    # cykAlgo = CYKAlgo(G)
    # if(cykAlgo.membership(w)){
    #     print "w is in G"
    # } else {
    #     print "w is not in G"
    # }


if __name__ == '__main__':
    main()
