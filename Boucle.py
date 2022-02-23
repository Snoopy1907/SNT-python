from lycee import *

num1= int(input('De quel entier voulez-vous afficher la table ?\n'));
num2 = int(input('\n Combien de multiples à afficher ?\n'));
for k in range(1, num2+1) :
	print("\n",k, "*", num1, "=",k*num1);
print("\n\n========================================================\n\n			Terminé !");