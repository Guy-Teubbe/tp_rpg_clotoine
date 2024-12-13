import random
#FICHIER PRINCIPAL D'EXECUTION
#
# FILTHY WANKERZ III
# Return to Tartiflex

#Création de personnage
# Nom
# Classe
# Niveau
# Vie
# Inventaire



Objet = {"1":{"nom":"Potion de Santé","propriété":"Vie","action":"+","min":1,"max":50},
         "2":{"nom":"Poison de Vie","propriété":"Vie","action":"-","min":0,"max":15},
         "3":{"nom":"Potion de Defense","propriété":"Defense","action":"+","min":2,"max":2},
         "4":{"nom":"Poison de Faiblesse","propriété":"Defense","action":"-","min":0,"max":2}}


Inventaire1 = {"1":Objet["1"],"2":Objet["1"],"3":Objet["1"]}
Inventaire2 = {"1":Objet["1"],"2":Objet["1"],"3":Objet["2"]}

Classe = {"Nécromancien":{"Vie":"+2"},"Zoomancien":{"Defense":"+1"},"Copromancien":{"Objet":Objet["2"]}}

Personnage1 = {"Nom":"Bandmou","Classe":Classe["Nécromancien"],"Niveau":1,"Vie":12,"Inventaire":Inventaire1,"Defense":9,"XP":0}
Personnage1 = {"Nom":"Moudujon","Classe":Classe["Copromancien"],"Niveau":1,"Vie":10,"Inventaire":Inventaire2,"Defense":10,"XP":0}

#Création des  classes

#Création de l'inventaire

#passage de niveau

def monter_niveau(perso = {}):
    print(perso)
    perso["Niveau"] += 1
    perso["Vie"] += 20

monter_niveau(Personnage1)
print(Personnage1)

#attaquer

#ajouter à l'inventaire

def ajout_invent(var = {}):
    print(Objet)
    nb = input("Numéro de l'objet : ")

    place =  int(list(var.keys())[-1]) + 1

    var[place] = Objet[nb]

# ajout_invent(Inventaire1)
# print(Inventaire1)

#utilisation d'un objet
#utilisation d'un objet

def utiliserObjet(objet,personnage,cible):
    #ajouter les bénéfices de l'objet sur le personnage
        objet["propriété"]
        objet["action"]
        val = random.randint(objet["min"],objet["max"])



    #consommer l'objet de l'inventaire


