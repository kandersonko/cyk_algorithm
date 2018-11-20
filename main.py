from grammar import Grammar
from CYKAlgo import CYKAlgo


def main():

    # G = Grammar("S->AB|XB;T->AB|XB;X->AT;A->a;B->b")
    # w="aaabb"

    print("Welcome to the CYK Interactive algorithm!")

    command = "y"
    while(command == "y"):
        grammar_text = input("Enter the grammar in CNF form (E.g. S->AB|a;A->a;B->b): ")
        if grammar_text == "": break 
        G = Grammar(grammar_text.strip())

        w = input("Enter the string to check: ")

        cykAlgo = CYKAlgo(G)
        if (cykAlgo.membership(w.strip())):
            print("The string w=\"{}\" is in grammar G!".format(w))
        else:
            print("The string w=\"{}\" is not in grammar G!".format(w))
        
        command = input("Continue the program (y/n)?: ")
    print("Bye!")


if __name__ == '__main__':
    main()
