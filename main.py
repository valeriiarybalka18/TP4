from noeud import Noeud
f1=Noeud(2)
f2=Noeud("y")
add=Noeud("+", [f1,f2])
f=Noeud("exp", [add])
print(f.__repr__)
print(f.evaluer({"exp":3}))