import random
import copy

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



Objet = {"1":{"Nom":"Potion de Santé","propriété":"Vie","action":"+","min":1,"max":50},
         "2":{"Nom":"Poison de Vie","propriété":"Vie","action":"-","min":0,"max":15},
         "3":{"Nom":"Potion de Defense","propriété":"Defense","action":"+","min":2,"max":2},
         "4":{"Nom":"Poison de Faiblesse","propriété":"Defense","action":"-","min":0,"max":2}}


Inventaire1 = {"1":Objet["1"],"2":Objet["1"],"3":Objet["1"]}
Inventaire2 = {"1":Objet["1"],"2":Objet["1"],"3":Objet["2"]}

Classe = {"Nécromancien":{"Nom":"Nécromancien","Vie":"+2"},"Zoomancien":{"Nom":"Zoomancien","Defense":"+1"},"Copromancien":{"Nom":"Zoomancien","Objet":Objet["2"]}}

Personnage1 = {"Nom":"Bandmou","Classe":Classe["Nécromancien"]["Nom"],"Niveau":1,"Vie":12,"Inventaire":Inventaire1,"Defense":9,"XP":0}
Personnage2 = {"Nom":"Moudujon","Classe":Classe["Copromancien"]["Nom"],"Niveau":1,"Vie":10,"Inventaire":Inventaire2,"Defense":10,"XP":0}


#Création des  classes

#Création de l'inventaire

#passage de niveau

def monter_niveau(perso = {}):
    print(perso)
    perso["Niveau"] += 1
    perso["Vie"] += 20



#attaquer
def afficherPerso(perso):
     print(f"{perso["Nom"]}\n-Classe: {perso["Classe"]}\n-Niveau: {perso["Niveau"]}\n-Vie: {perso["Vie"]}\n-Defense: {perso["Defense"]}\n-XP: {perso["XP"]}\n\nINVENTAIRE\n{perso["Inventaire"]}")


########################
#ajouter à l'inventaire#
########################
def ajout_invent(var = {}):
    print(Objet)
    nb = input("Numéro de l'objet : ")

    place =  int(list(var.keys())[-1]) + 1

    var[place] = Objet[nb]

# ajout_invent(Inventaire1)
# print(Inventaire1)


#############################
#Recalculer Index Inventaire#
#############################
def recalculerIndexInventaire(inventaire,cle):
    i = int(cle)+1
    #for i in range(int(cle)+1,4):
    index = copy.copy(len(inventaire)+1)

    while i <= index:

        itemDecale = inventaire[str(i)]


        inventaire[str(int(i)-1)] = itemDecale

        del inventaire[str(i)]
        i += 1

            


########################
#utilisation d'un objet#
########################
def utiliserObjet(objet,cible,inventaire,cle):
    #ajouter les bénéfices de l'objet sur le personnage
        prop = objet["propriété"]
        action = objet["action"]
        val = random.randint(objet["min"],objet["max"])

        
        if action == "+":
            print(f"{objet["Nom"]} va ajouter {val} pts de {prop} à {cible["Nom"]}")
            cible[prop] += val
        else:
            print(f"{objet["Nom"]} va retirer {val} pts de {prop} à {cible["Nom"]}")
            cible[prop] -= val

    #retirer de l'inventaire
        del inventaire[cle]

        recalculerIndexInventaire(inventaire,cle)
    
        



def executionPrg():
     
    monter_niveau(Personnage1)
    afficherPerso(Personnage1)
    input(">")
    utiliserObjet(Objet["1"],Personnage1,Inventaire1,"1")
    input(">")

    afficherPerso(Personnage1)
    input(">")
    #recalculerIndexInventaire(Inventaire1)


executionPrg()