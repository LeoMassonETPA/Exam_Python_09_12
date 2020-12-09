from colorama import init
init()
from colorama import Fore, Back, Style

import random

liste_mot = ["hideux", "picole", "crayon", "fusain", "paumes", "charge", "tisser", "whisky", "chlore", "poulet"]       #Selection aleatoire du mot
mot_alea = random.choices(liste_mot)  
mot_mystere =(mot_alea[0])                                                                                             # Aucune idée de pourquoi ça marche 

proposition = input ("Votre proposition ?(6 lettres max)")

    if (proposition[0] == mot_mystere[0]):
        print (Fore.RED + proposition[0], end=" ")
    elif (proposition[0] == mot_mystere[1] or proposition[0] == mot_mystere[2] or proposition[0] == mot_mystere[3] or proposition[0] == mot_mystere[4] or proposition[0] == mot_mystere[5]):
        print (Fore.YELLOW + proposition[0], end=" ")
    else :
        print (Fore.BLUE + proposition[0], end=" ")


input ()
