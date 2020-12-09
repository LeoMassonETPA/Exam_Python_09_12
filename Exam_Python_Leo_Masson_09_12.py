from colorama import init
init()
from colorama import Fore, Back, Style

import random

liste_mot = ["hideux", "picole", "crayon", "fusain", "paumes", "charge", "tisser", "whisky", "chlore", "poulet"]       #Sélection aléatoire du mot
mot_alea = random.choices(liste_mot)  
mot_mystere =(mot_alea[0])

print ("Bienvenue sur ce jeu de Motus !")


victoire = False
tour = 0


while (victoire == False or tour < 9):

    proposition = input ("Votre proposition ?(6 lettres max)")

    if(proposition[0] == mot_mystere[0]):
        print (Fore.RED + proposition[0], end=" ")
    elif(proposition[0] == mot_mystere[1] or proposition[0] == mot_mystere[2] or proposition[0] == mot_mystere[3] or proposition[0] == mot_mystere[4] or proposition[0] == mot_mystere[5]):
        print (Fore.YELLOW + proposition[0], end=" ")
    else:
        print (Fore.BLUE + proposition[0], end=" ")

    if(proposition[1] == mot_mystere[1]):
        print (Fore.RED + proposition[1], end=" ")
    elif(proposition[1] == mot_mystere[0] or proposition[1] == mot_mystere[2] or proposition[1] == mot_mystere[3] or proposition[1] == mot_mystere[4] or proposition[1] == mot_mystere[5]):
        print (Fore.YELLOW + proposition[1], end=" ")
    else:
        print (Fore.BLUE + proposition[1], end=" ")
    
    if(proposition[2] == mot_mystere[2]):
        print (Fore.RED + proposition[2], end=" ")
    elif(proposition[2] == mot_mystere[0] or proposition[2] == mot_mystere[1] or proposition[2] == mot_mystere[3] or proposition[2] == mot_mystere[4] or proposition[2] == mot_mystere[5]):
        print (Fore.YELLOW + proposition[2], end=" ")
    else:
        print (Fore.BLUE + proposition[2], end=" ")

    if(proposition[3] == mot_mystere[3]):
        print (Fore.RED + proposition[3], end=" ")
    elif(proposition[3] == mot_mystere[0] or proposition[3] == mot_mystere[1] or proposition[3] == mot_mystere[2] or proposition[3] == mot_mystere[4] or proposition[3] == mot_mystere[5]):
        print (Fore.YELLOW + proposition[3], end=" ")
    else:
        print (Fore.BLUE + proposition[3], end=" ")
    
    if(proposition[4] == mot_mystere[4]):
        print (Fore.RED + proposition[4], end=" ")
    elif(proposition[4] == mot_mystere[0] or proposition[4] == mot_mystere[1] or proposition[4] == mot_mystere[2] or proposition[4] == mot_mystere[3] or proposition[4] == mot_mystere[5]):
        print (Fore.YELLOW + proposition[4], end=" ")
    else:
        print (Fore.BLUE + proposition[4], end=" ")
    
    if(proposition[5] == mot_mystere[5]):
        print (Fore.RED + proposition[5], end=" ")
    elif(proposition[5] == mot_mystere[0] or proposition[5] == mot_mystere[1] or proposition[5] == mot_mystere[2] or proposition[5] == mot_mystere[3] or proposition[5] == mot_mystere[4]):
        print (Fore.YELLOW + proposition[5], end=" ")
    else:
        print (Fore.BLUE + proposition[5], end=" ")
    
    if (proposition == mot_mystere):
        victoire = True
    tour += 1
    print(Style.RESET_ALL)
    


    

input ()
