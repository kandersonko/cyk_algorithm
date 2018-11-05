from grammar import Grammar


def main():
    G = Grammar("S->AB|a;A->BB|a;B->AB|C|b;C->c;D->D")
    print(G.rules)
    print(G.productions)
    
    # cykAlgo = CYKAlgo(G)
    # if(cykAlgo.membership(w)){
    #     print "w is in G"
    # } else {
    #     print "w is not in G"
    # }

if __name__ == '__main__':
    main()