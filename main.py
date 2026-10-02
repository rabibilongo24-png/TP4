from noeud import Noeud

# exp(2+y) : la racine est "exp", son enfant est "+", dont les enfants sont 2 et "y"
noeud_2 = Noeud(2)
noeud_y = Noeud("y")
noeud_plus = Noeud("+", [noeud_2, noeud_y])
noeud_exp = Noeud("exp", [noeud_plus])

print(noeud_exp.affichage_polonais())   # attendu : "exp + 2 y"
