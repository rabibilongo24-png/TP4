class Noeud:
    def __init__(self, valeur, enfants=None):
        """
        Un noeud d'un arbre d'expression mathématique.

        valeur : str, int ou float — nom d'opérateur/variable (str)
                 ou constante numérique (int/float)
        enfants : liste de Noeud (les branches filles)
        """
        self.valeur = valeur
        self.enfants = enfants if enfants is not None else []

    def ajouter_enfant(self, noeud):
        """Ajoute un noeud à la liste des noeuds enfants."""
        self.enfants.append(noeud)

    def affichage_polonais(self):
        """
        Retourne une chaîne représentant l'expression en notation
        polonaise (préfixe), ex : "+ 2 y" pour add(2, y).
        """
        chaine = str(self.valeur)
        for enfant in self.enfants:
            chaine += " " + enfant.affichage_polonais()
        return chaine