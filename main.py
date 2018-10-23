def main():
    G = Grammar("s->AB|a;A->BB|a;B->AB|b")
    cykAlgo = CYKAlgo(G)
    if(cykAlgo.membership(w)){
        print "w is in G"
    } else {
        print "w is not in G"
    }

if __name__ == '__main__':
    main()