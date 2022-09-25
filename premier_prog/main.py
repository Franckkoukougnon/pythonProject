"""Premier programme
formation Python
Python Learning"""

nom = input("Quel est ton nom ? ")
age = input("Quel est votre age ? ")

# str -> int


try:
    age_prochain = int(age) + 1
except:
    print("Erreur, veuillez mettre des chiffres")
else:
    print("je suis " + nom + " et j'ai " + str(age) + " ans")
    print("l'annéé prochain vous aurez " + str(age_prochain) + " ans")
