
# Classe mère
class Animal:

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age


    def emettre_son(self):
        print("Son de l'animal")


# Classe fille:

class Chat(Animal):
    
    def __init__(self, nom, age, couleur):
        # super(): pointe vers la classe supérieure
        super().__init__(nom,age)
        self.couleur = couleur

    def dormir(self):
        print('dormir.....')

    # Une classe fille peur surcharger (overload: modifier) les fonctions définies dans la classe

    def emettre_son(self):
        print('Miauller..................')

a = Animal('Nom_animal', 5)
a.emettre_son()

# La classe définie définie une structure de base pour les classes filles. Contient les éléments communs aux autres classes
# Une classe via l'héritage, récupère tous les éléments de la classe mère
# Une classe fille en plus des attributs définis dans la classe, elle peut avoir des attributs qui lui sont spécifiques
# Une classe fille en plus des fonctions définies dans la classe, elle peut avoir des fonctions qui lui sont spécifiques
# Une classe fille peut en cas de besoin surcharger les fonctions définies dans la classe mère
c = Chat('chat', 3, 'gris')
c.emettre_son()