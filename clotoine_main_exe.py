import random
import copy
import os
import keyboard

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

def ecran(vide=False,titre="",sousTitre="",centreHaut="",gaucheHaut="",droiteHaut="",centreBas="",gaucheBas="",droiteBas=""):

    if sousTitre == None or sousTitre == "": sousTitre == "        "
    if centreHaut == None or centreHaut == "": centreHaut == "        "
    if gaucheHaut == None or gaucheHaut == "": gaucheHaut == "        "
    if droiteHaut == None or droiteHaut == "": droiteHaut == "        "
    if centreBas == None or centreBas == "": centreBas == "        "
    if gaucheBas == None or gaucheBas == "": gaucheBas == "        "
    if droiteBas == None or droiteBas == "": droiteBas == "        "
    if titre == None or titre == "": titre == "        "

    if vide != True:
        print(f"                               {centreHaut}                                      ")
        print(f" {gaucheHaut}                                                       {droiteHaut} ")
        print(f"                                                                                 ")
        print(f"                                                                                 ")
        print(f"                                 {titre}                                         ")
        print(f"                               {sousTitre}                                       ")
        print(f"                                                                                 ")
        print(f" {gaucheBas}                                                         {droiteBas} ")
        print(f"                               {centreBas}                                       ")


    else:
        print("                                                                                  ")
        print("                                                                                  ")
        print("                                                                                  ")
        print("                                                                                  ")
        print("                                                                                  ")
        print("                                                                                  ")
        print("                                                                                  ")
        print("                                                                                  ")
        print("                                                                                  ")

def credits():
    ecran(False,"Edition Bignou","Trululu")
    os.system('cls')
    ecran(False,"Turboflette Studio","Ze Trululu Enterprise")
    os.system('cls')
    ecran(False,"FILTHY WANKERZ III","Call of Tartiflex")

def menu():
    print("Menu")



Objet = {"1":{"Nom":"Potion de Santé","propriété":"Vie","action":"+","min":1,"max":50},
         "2":{"Nom":"Poison de Vie","propriété":"Vie","action":"-","min":0,"max":15},
         "3":{"Nom":"Potion de Defense","propriété":"Defense","action":"+","min":2,"max":2},
         "4":{"Nom":"Poison de Faiblesse","propriété":"Defense","action":"-","min":0,"max":2}}


Inventaire1 = {"1":Objet["1"],"2":Objet["1"],"3":Objet["1"]}
Inventaire2 = {"1":Objet["1"],"2":Objet["1"],"3":Objet["2"]}

Classe = {"Nécromancien":{"Nom":"Nécromancien","Vie":"+2"},"Zoomancien":{"Nom":"Zoomancien","Defense":"+1"},"Copromancien":{"Nom":"Zoomancien","Objet":Objet["2"]}}

Personnage1 = {"Nom":"Bandmou","Classe":Classe["Nécromancien"]["Nom"],"Niveau":1,"Vie":12,"Inventaire":Inventaire1,"Defense":9,"XP":0}
Personnage2 = {"Nom":"Moudujon","Classe":Classe["Copromancien"]["Nom"],"Niveau":1,"Vie":10,"Inventaire":Inventaire2,"Defense":10,"XP":0}



###################
#passage de niveau# TEST UNITAIRE OK
###################
def monter_niveau(perso = {}):
    afficherPerso(perso)
    perso["Niveau"] += 1
    perso["Vie"] += 20



#attaquer

def attaque(perso1 = {}, perso2 = {}):
    # degats1 = 10 * perso1["Niveau"]
    # degats2 = 10 * perso2["Niveau"]

    while perso1["Vie"] > 0 or perso2["Vie"] > 0:
        degats1 = random.randint(1,6)
        degats2 = random.randint(1,6)
        perso2["Vie"] -= degats1
        if perso2["Vie"] <= 0 :     
            perso2["Vie"] = 0 
            print(f"{perso2["Nom"]} perd {degats1} PV. -  PV restants : {perso2["Vie"]} - Attaque fatale\n")
            break
        print(f"{perso2["Nom"]} perd {degats1} PV. -  PV restants : {perso2["Vie"]} \n")
        
        perso1["Vie"] -= degats2
        if perso1["Vie"] <= 0 : 
            perso1["Vie"] = 0
            print(f"{perso1["Nom"]} perd {degats2} PV. -  PV restants : {perso1["Vie"]} - Attaque fatale\n")
            break
        print(f"{perso1["Nom"]} perd {degats2} PV. -  PV restants : {perso1["Vie"]}\n")

    if perso1["Vie"] == 0 :
        print(f"{perso1["Nom"]} est mort.")
    elif perso2["Vie"] == 0 :
        print(f"{perso2["Nom"]} est mort.")




######################
#afficher fiche perso# TEST UNITAIRE OK
######################
def afficherPerso(perso):
     print(f"{perso["Nom"]}\n-Classe: {perso["Classe"]}\n-Niveau: {perso["Niveau"]}\n-Vie: {perso["Vie"]}\n-Defense: {perso["Defense"]}\n-XP: {perso["XP"]}\n\nINVENTAIRE\n{perso["Inventaire"]}")


########################
#ajouter à l'inventaire# TEST UNITAIRE OK
########################
def ajout_invent(var = {}):
    print(Objet)
    nb = input("Numéro de l'objet : ")

    place =  int(list(var.keys())[-1]) + 1

    var[place] = Objet[nb]



#############################
#Recalculer Index Inventaire# TEST UNITAIRE OK
#############################
def recalculerIndexInventaire(inventaire,cle):
    i = int(cle)+1

    index = copy.copy(len(inventaire)+1)

    while i <= index:

        itemDecale = inventaire[str(i)]


        inventaire[str(int(i)-1)] = itemDecale

        del inventaire[str(i)]
        i += 1

            


########################
#utilisation d'un objet# TEST UNITAIRE OK
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
     
     credits()

     menu()
#     monter_niveau(Personnage1)
#     afficherPerso(Personnage1)
#     input(">")
#     utiliserObjet(Objet["1"],Personnage1,Inventaire1,"1")
#     input(">")

#     afficherPerso(Personnage1)
#     input(">")
#     recalculerIndexInventaire(Inventaire1)

#     attaque(Personnage1, Personnage2)


executionPrg()