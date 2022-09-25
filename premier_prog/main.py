"""Premier programme
formation Python
Python Learning"""

nom = input("Quel est ton nom ? ")
age = input("Quel est votre age ? ")

# str -> int
age_prochain = int(age) + 1

print(type(age))
print(type(nom))
print("je suis " + nom + " et j'ai " + str(age) +" ans")
print("l'an prochain vous aurez " + str(age_prochain) + " ans")