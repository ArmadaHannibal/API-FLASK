# class Article:
#     def __init__(self, nom, quantite, price, rayon):
#         self.nom = nom
#         self.quantite = quantite
#         self.price = price
#         self.rayon = rayon

#     def afficher_details(self):
#         print(f"Nom: {self.nom}, Quantite: {self.quantite}, Prix: {self.price}€, Rayon: {self.rayon}")


# Article1 = Article("Piece", 30, 15, "A-B-Voiture")
# Article1.afficher_details()

# Article2 = Article("Cart", 25, 18, '2B-5-Voiture')
# Article2.afficher_details()

class Voiture:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def avancer(self):
        self.x += 1
        print(f'+')
    
    def reculer(self):
        self.y -= 1
        # print(f'Reculer: -')


liste = [];
voiture = Voiture(1, 1)
count = 0

for _ in range(11):
    liste.append(voiture.avancer())
    count +=1

if count == 11:
    for _ in range(11):
        voiture.reculer()

print(liste)
