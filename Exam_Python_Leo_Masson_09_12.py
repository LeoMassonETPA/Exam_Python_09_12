from colorama import init
init()
from colorama import Fore, Back, Style

import random

liste_mot = ["hideux", "picole", "crayon", "fusain", "paumes", "charge", "tisser", "whisky", "chlore", "poulet"]

mot_mystere = random.choices(liste_mot)
print (liste_mot)
print(mot_mystere)

input ()