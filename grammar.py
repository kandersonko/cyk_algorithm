class Grammar(object):

    def __init__(self, G):
        """ __init__ takes a string G
            and parses parses the productions into an array of productions 
        """
        self.rules = G.split(';');
        self.productions = dict()
        for rule in self.rules:
            startVar = rule.split('->')[0]
            varSet = rule.split("->")[1]
            variables = [x for x in varSet.split('|') if x.isupper()]
            terminals = [x for x in varSet.split('|') if x.islower()]
            self.productions[startVar] = {"variables": variables, "terminals": terminals}

