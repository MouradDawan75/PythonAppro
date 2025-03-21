# Approche procédurale: repose sur l'utilisation des paramètres et des focntions
# Approche objets: repose sur l'utilisation des classes et des objets

# Une classe est un type de données. Elle décrit la structure d'un objet.
# Elle contient 3 choses généralement:
# - Attributs - Propriétés:
# - Fonctions
# - Fonction spéciale appelée constructeur (initialisateur): qui porte le nom la classe permettant d'instancier la classe.
# Instancier une classe c'est créer un obejt à partir de cette classe

class User:

    # attribut de classe: partagé par toutes les instances
    profil = 'admin'


    # constructeur de la classe User: l'initialisateur
    # attributs d'instance: propres à chaque instance
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        print('>>>>> init..................')
        # self: mot clé qui pointe vers l'objet en cours d'utilisation

    # fonction d'instance: fonction qui concerne une instance particulière
    def afficher_nom(self):
        print(self.nom)


    # fonction de classe: elle permet de manipuler les attributs de classe
    @classmethod
    def modifier_profil(cls, nom_profil):
        #cls: pour classe -> donne accès aux attributs de classe
        cls.profil = nom_profil






#  User.__init__(u, 'DUPONT', 'Jean', 60) : code exécuté en arrière plan par python
u = User('DUPONT', 'Jean', 60)

u1 = User('NOM', 'Prenom', 25)


print(u.nom)
print(u.age)

u.afficher_nom()
u1.afficher_nom()

print(User.profil) # les attributs de classe sont accéssible via la classe

print(u.profil)
print(u1.profil)

# Méthode de classe est appelée à partir de la classe
User.modifier_profil('Manager')

print(u.profil)
print(u1.profil)


class CompteBancaire:

    banque = 'BNP'

    def __init__(self, numero, solde):
        self.numero = numero
        self.solde = solde

    
    def depot(self, montant):
        self.solde += montant


    def retrait(self, montant):
        if self.solde >= montant:
            self.solde -= montant
        else:
            print('Solde insuffisant......')

    @classmethod
    def modifier_banque(cls, nom_banque):
        cls.banque = nom_banque

    # __str__: permet de personnaliser l'affichage d'un objet. Choisir les attributs a afficher
    def __str__(self):
        return f'Numéro: {self.numero} - Solde: {self.solde}'
    
    # __eq__: vérifier l'égalité de 2 comptes
    def __eq__(self, other):
        return self.numero == other.numero


cpt1 = CompteBancaire('sdqsd145', 1500)
cpt1.depot(500)
cpt1.retrait(1000)


cpt2 = CompteBancaire('dsqd15', 5000)
print(cpt2)

cpt3 = CompteBancaire('dsqd15', 100000)

print(cpt2 == cpt3)

print(cpt2.__dict__) # converssion d'un compte en dict





