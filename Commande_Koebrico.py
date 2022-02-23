# Créé par Elève, le 20/01/2022 avec EduPython
from lycee import *
import datetime

nom= input("Bonjour, qu'elle est votre nom ? ");
prenom= input("Veuillez entrer votre prénom. ");
adresse= input("Veuillez entrer une adresse postal. ");
num_tel= input("Veuillez un numéro de téléphone pour être tenu au courant. ");

n_peinture= int(input("Chaque pot de peinture est vendu à 25€/unité, combien en voulez-vous ? "));
n_ciment= int(input("Nos sacs de ciments sont vendu à 5€ l'unité, combien en voulez-vous ? "));
n_pinceaux= int(input("Les pinceaux sont facturés à 8€ par pièce, combien en voulez-vous ? "));
n_carreaux= int(input("Pour 1 mètre carré de carreaux, le prix est de 35€, combien vous en faut-il ? "));
prix= int((n_carreaux*35)+(n_pinceaux*8)+(n_ciment*5)+(n_peinture*25))

date = datetime.datetime.now

print("\nUne remise de 5% est appliqué si votre commande est entre 100 et 300 euros, une remise de 10% est appliqué si votre commande est supérieur à 300€")

if 100 <prix :
    if 300 >prix :
        reduc= ("5%")
        prix_f= prix*0.95
    else:
        reduc=("10%")
        prix_f= prix*0.90
else:
    prix_f= prix
    reduc= ("0%")


print("\n\n\n\nVoici votre bon de commande.\n\n Votre nom :  ", nom,"\n Votre prénom : ", prenom, "\n Nombre de pots de peinture : ", n_peinture, "\n Nombre de sacs ciments : ", n_ciment, "\n Nombre de pinceaux : ", n_pinceaux, "\n Nombre de m² de carreaux : ", n_carreaux, "\n Le montant de votre commande : ", prix,"€", "\n Votre remise : ", reduc, "\n Total à payer : ", prix_f,"€", "\n La société Koebrico vous remercie", nom, prenom,". \n Vous recevrez un SMS au ", num_tel, "suivant lorsque la commande sera prête, si vous demandez alors une livraison, elle sera livré à l'adresse suivante : \n", adresse)


