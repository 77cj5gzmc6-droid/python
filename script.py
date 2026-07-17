from datetime import datetime
import json
import os

FICHIER = "/Users/joshuawhite-labbe/Desktop/finances.json"

def charger_donnees():
    if os.path.exists(FICHIER):
        with open(FICHIER, "r", encoding="utf-8") as ft:
            return json.load(ft)
    else:
        return {
            "salaire": 0,
            "depenses": []
        }

def sauvegarde_donnees(donnees):
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=4, ensure_ascii=False)

#########################
## Welcome
#########################

aujourdhui = datetime.now()
print("Bonjour ! Aujourd'hui, nous sommes le", aujourdhui.strftime("%d/%m/%Y"))

donnees = charger_donnees()
depenses = donnees["depenses"]

#########################
## Salary
#########################

if donnees["salaire"]==0:
    salaire_mensuel = float(input("Quel est votre salaire mensuel ? "))
    donnees["salaire"] = salaire_mensuel
    sauvegarde_donnees(donnees)
else:
    salaire_mensuel = donnees["salaire"]
    print("Votre salaire mensuel est de", salaire_mensuel, "euros")

########################
## Expenses
########################

argent = salaire_mensuel - sum(
    depense["montant"] for depense in depenses
)
print ( "Il vous reste", argent, "euros ce mois-ci.")

########################
## Main menu
########################

while True:
    action = input("Que voulez-vous faire? (nouvelle / supprimer / modifdep / voir / rechercher / reste / modifsalaire / quitter)")
    
    if action == "nouvelle":
        catégorie = input("Quelle est la catégorie de votre dépense? ")
        nom = input("Quel est le nom de votre dépense? Attention, il ne faut pas que les noms se répètent ")
        montant = float(input("Quel est le montant de votre dépense? "))
        date = input("Quelle est la date de votre dépense? (jj/mm/aaaa) ")
        argent = argent - montant
        depense = {
            "nom": nom,
            "date": date,
            "catégorie": catégorie,
            "montant": montant
        }
        depenses.append(depense)
        donnees["depenses"]=depenses
        sauvegarde_donnees(donnees)
        print("Votre dépense a été ajoutée avec succès. Il vous reste", argent, "euros ce mois-ci.")
    
    elif action == "voir":
        print("Voici la liste de vos dépenses :")
        for depense in depenses:
            print(depense)
    
    elif action == "reste":
        print ("Vous avez", argent, "euros ce mois-ci.")
    
    elif action == "modifsalaire":
        salaire_mensuel = float(input("Quel est votre nouveau salaire mensuel?"))
        donnees["salaire"] = salaire_mensuel
        sauvegarde_donnees(donnees)
        print("Votre nouveau salaire est maintenant de", salaire_mensuel, "euros.")
    
    elif action == "quitter":
        print("Merci d'avoir utilisé notre application de finances personnelles. À bientôt !")
        break

    elif action == "supprimer":
        nom_depense = input("Quel est le nom de la dépense que vous souhaitez supprimer? ")
        depense_trouvee = False
        for depense in depenses:
            if depense["nom"] == nom_depense:
                depenses.remove(depense)
                donnees["depenses"] = depenses
                sauvegarde_donnees(donnees)
                argent += depense["montant"]
                print("La dépense a été supprimée avec succès. Il vous reste", argent, "euros ce mois-ci.")
                depense_trouvee = True
                break
        if not depense_trouvee:
                print("Aucune dépense trouvée avec ce nom.")

    elif action == "modifdep":
        nom_depense = input("Quel est le nom de la depense que vous voulez modifier?")
        depense_trouvee = False
        for depense in depenses:
            if depense["nom"] == nom_depense:
                nouvelle_categorie = input("Quelle est la nouvelle catégorie de votre dépense? ")
                nouveau_nom = input("Quel est le nouveau nom de votre dépense? Attention, il ne faut pas que les noms se répètent ")
                nouveau_montant = float(input("Quel est le nouveau montant de votre dépense? "))
                nouvelle_date = input("Quelle est la nouvelle date de votre dépense? (jj/mm/aaaa) ")
                argent += depense["montant"] - nouveau_montant
                depense["catégorie"] = nouvelle_categorie
                depense["nom"] = nouveau_nom
                depense["montant"] = nouveau_montant
                depense["date"] = nouvelle_date
                donnees["depenses"] = depenses
                sauvegarde_donnees(donnees)
                print("La dépense a été modifiée avec succès. Il vous reste", argent, "euros ce mois-ci.")
                depense_trouvee = True
                break
        if not depense_trouvee:
                print("Aucune dépense trouvée avec ce nom.")

    elif action == "rechercher":
        nom_depense = input("Quelle dépense recherchez-vous?")
        depense_trouvee = False
        for depense in depenses:
            if depense["nom"] == nom_depense:
                print("Dépense trouvée. nom =", depense["nom"], "categorie=",depense["catégorie"], "montant=",depense["montant"], "date=", depense["date"])
                depense_trouvee = True
                break
        if not depense_trouvee:
                print("Aucune dépense trouvée avec ce nom.")

else :
    print("Action non reconnue. Veuillez réessayer.")   
