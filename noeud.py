class Noeud:
    """Ce code est fait pour classer puis pour casser les couilles et donc cordialement suce moi valeriia"""
    OPERATEURS_BINAIRES = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }

    OPERATEURS_UNAIRES = {
        "exp": __import__("math").exp,
        "log": __import__("math").log,
        "sin": __import__("math").sin,
        "cos": __import__("math").cos,
    }

    def __init__(self, valeur, enfants=None):
        self.valeur=valeur
        self.enfants=enfants if enfants is not None else []

    def ajouter_enfant(self, noeud):
        self.enfants.append(noeud)

    def __repr__(self):
        if not self.enfants:
            return str(self.valeur)
        else :
            exp=[]
            for e in self.enfants:
                exp.append(repr(e))
            return str(self.valeur)+" ".join(exp)

    def evaluer(self, dict):
        if isinstance(self.valeur,(int,float)) :
            return self.valeur
        elif isinstance(self.valeur,str):
            if self.valeur not in dict:
                raise ValueError(f"aucune valeur fournie")
            return float(dict[self.valeur])
        
        res= [enfant.evaluer(dict) for enfant in self.enfants]
        


    