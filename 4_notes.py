# Créé par Elève, le 20/01/2022 avec EduPython
from lycee import *

print("Bonjour, veuillez entrer 4 notes pour calculer votre moyenne.");
a = int(input("Votre première note :"));
b = int(input("Votre seconde note :"));
c = int(input("Votre troisième note :"));
d = int(input("Votre quatirème note :"));

f = (a+b+c+d)/4
print("Voici votre moyenne :", f);

if f >10 :
    if f >12 :
        if f >14 :
            print("Bravo !")
        else: print("Bon travail !")
    else: print("C'est correct !")
else: print("Attention, il y a du progrès à faire.")