import random; 

dictionnaire = {
    'name' : 'HAMD', 
    2 : 4, 
    3 : [1, 2, 5]
};
for key in dictionnaire : 
    valeur = dictionnaire[key]
    # print(valeur);

def sommes (a, b, c) :
    resultat = a + b + c;
    return resultat;

def sommealeatoires (a, b) :
    aleatoiresnb1 = random.randint(1, a);
    aleatoiresnb2 = random.randint(1, b);
    value = aleatoiresnb1 + aleatoiresnb2;
    return value;

def listaleatoires (array) :
    if not array : 
        print('Tableau vide !');
    else :
        valeur_aleatoire = random.choice(ma_liste)
        return valeur_aleatoire

def operation_aleatoire(booleen, liste, mini, maxi):
    if booleen == '1' :
        if not liste : 
            print('Tableau vide !');
        else :
            valeur_aleatoire = random.choice(liste)
            return valeur_aleatoire
    elif booleen == '2' : 
        if not liste : 
            print('Tableau vide !');
        else :
            index_max = len(liste) - 1
            if index_max == maxi : 
                aleatoiresnb1 = random.randint(mini, maxi);
                aleatoiresnb2 = random.randint(mini, maxi);
                resultat = {
                    'valeur 1 : ' : aleatoiresnb1,
                    'valeur 2 : ' : aleatoiresnb2,
                    'resultat : ' : aleatoiresnb1 + aleatoiresnb2
                }
                return resultat
            elif index_max != maxi :
                aleatoiresnb1 = random.randint(mini, index_max);
                aleatoiresnb2 = random.randint(mini, index_max);
                resultat = {
                    'valeur 1 : ' : aleatoiresnb1,
                    'valeur 2 : ' : aleatoiresnb2,
                    'resultat : ' : aleatoiresnb1 + aleatoiresnb2
                }
                return resultat

ma_liste = []

# print("Remplissez la liste (appuyez sur Entrée pour terminer) :")
# while True:
#     valeur = input("Entrez une valeur : ")
#     if valeur == "":
#         break 
#     else:
#         ma_liste.append(valeur)

# print("Liste remplie :", ma_liste)

# valeur_aleatoire = listaleatoires(ma_liste)
# print("Valeur aléatoire dans la liste :", valeur_aleatoire)

# nb1 = int(input("Entrez le premier nombre : "))
# nb2 = int(input("Entrez le deuxième nombre : "))
# nb3 = float(input("Entrez le troisième nombre : "))

# result = sommes(nb1, nb2, nb3);
# resultaleatoires = sommealeatoires(nb1, nb2)
# print ([result]);
# print ('resultaleatoires');
# print ([resultaleatoires]);

# print (dictionnaire[3])

print("Choisissez une opération :")
print("1. Affichage aleatoires")
print("2. Addition aleatoires")

choix = input("Entrez le numéro de l'opération : ")

if choix == '1':
    print("Remplissez la liste (appuyez sur Entrée pour terminer) :")
    while True:
        valeur = input("Entrez une valeur : ")
        if valeur == "":
            break 
        else:
            ma_liste.append(valeur)
    print([ma_liste])
    operation = operation_aleatoire(choix, ma_liste, 0, 0);
    print([operation])
elif choix == '2':
    print("Remplissez la liste (appuyez sur Entrée pour terminer) :")
    while True:
        valeur = input("Entrez une valeur : ")
        if valeur == "":
            break 
        else:
            ma_liste.append(valeur)
    
    mini = int(input("Entrez une valeur minimale: "))
    maxi = int(input("Entrez une valeur maximale: "))
    print([ma_liste])
    operation = operation_aleatoire(choix, ma_liste, mini, maxi);
    print([operation])
else:
    print("Choix invalide. Veuillez entrer un numéro valide.")