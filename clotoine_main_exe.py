import random
#FICHIER PRINCIPAL D'EXECUTION

#Création de personnage
# Nom
# Classe
# Niveau
# Vie
# Inventaire
Objet = {"Potion de Soin":{"propriété":"Vie","action":"+","min":1,"max":50},"Poison de Vie":{"propriété":"Vie","action":"-","min":0,"max":15}}


Inventaire1 = {"1":Objet["Potion de Soin"],"2":Objet["Potion de Soin"],"3":Objet["Potion de Soin"]}
Inventaire2 = {"1":Objet["Potion de Soin"],"2":Objet["Potion de Soin"],"3":Objet["Poison de Vie"]}

Classe = {"Nécromancien":{},"Zoomancien":{},"Copromancien":{}}
Personnage1 = {"Nom":"Bandmou","Classe":Classe["Nécromancien"],"Niveau":1,"Vie":10,"Inventaire":Inventaire1,"Defense":9,"XP":0}
Personnage1 = {"Nom":"Moudujon","Classe":Classe["Copromancien"],"Niveau":1,"Vie":10,"Inventaire":Inventaire2,"Defense":11,"XP":0}

#Création des  classes

#Création de l'inventaire

#passage de niveau

#attaquer

#ajouter à l'inventaire

#utilisation d'un objet