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

today = datetime.now()
print("Bonjour ! Aujourd'hui, nous sommes le", today.strftime("%d/%m/%Y"))

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

if today.day ==1:
    argent =+ salaire_mensuel

########################
## Main menu
########################

while True:
    action = input("Que voulez-vous faire? (Nouvelle dépense (n) / Supprimer une dépense (s) / Rajouter de l'argent (a) / Modifier une dépense (md) / Voie mes dépenses (v) / Rechercher une dépense (r) / Reste (e) / Modifier mon salaire mensuel (ms) / Quitter (q)")
    
    if action == "n":
        categorie = input("Quelle est la catégorie de votre dépense? ")
        nom = input("Quel est le nom de votre dépense? Attention, il ne faut pas que les noms se répètent ")
        montant = float(input("Quel est le montant de votre dépense? "))
        date = input("Quelle est la date de votre dépense? (jj/mm/aaaa) ")
        argent = argent - montant
        depense = {
            "nom": nom,
            "date": date,
            "categorie": categorie,
            "montant": montant
        }
        depenses.append(depense)
        donnees["depenses"]=depenses
        sauvegarde_donnees(donnees)
        print("Votre dépense a été ajoutée avec succès. Il vous reste", argent, "euros ce mois-ci.")
    
    elif action == "v":
        print("Voici la liste de vos dépenses :")
        for depense in depenses:
            print(depense)
    
    elif action == "e":
        print ("Vous avez", argent, "euros ce mois-ci.")
    
    elif action == "ms":
        salaire_mensuel = float(input("Quel est votre nouveau salaire mensuel?"))
        donnees["salaire"] = salaire_mensuel
        sauvegarde_donnees(donnees)
        print("Votre nouveau salaire est maintenant de", salaire_mensuel, "euros.")
    
    elif action == "q":
        print("Merci d'avoir utilisé notre application de finances personnelles. À bientôt !")
        break

    elif action == "s":
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

    elif action == "md":
        nom_depense = input("Quel est le nom de la depense que vous voulez modifier?")
        depense_trouvee = False
        for depense in depenses:
            if depense["nom"] == nom_depense:
                nouvelle_categorie = input("Quelle est la nouvelle catégorie de votre dépense? ")
                if nouvelle_categorie == "m":
                    nouvelle_categorie = depense["categorie"]
                nouveau_nom = input("Quel est le nouveau nom de votre dépense? Attention, il ne faut pas que les noms se répètent ")
                if nouveau_nom == "m":
                    nouveau_nom = depense["nom"]
                nouveau_montant = float(input("Quel est le nouveau montant de votre dépense? Appuyez 0 si c'est le même montant"))
                if nouveau_montant == 0:
                    nouveau_montant = depense["montant"]
                nouvelle_date = input("Quelle est la nouvelle date de votre dépense? (jj/mm/aaaa) ")
                if nouvelle_date == "m":
                    nouvelle_date = depense["date"]
                argent += depense["montant"] - nouveau_montant
                depense["categorie"] = nouvelle_categorie
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

    elif action == "r":
        nom_depense = input("Quelle dépense recherchez-vous?")
        depense_trouvee = False
        for depense in depenses:
            if depense["nom"] == nom_depense:
                print("Dépense trouvée. nom =", depense["nom"], "categorie=",depense["categorie"], "montant=",depense["montant"], "date=", depense["date"])
                depense_trouvee = True
                break
        if not depense_trouvee:
                print("Aucune dépense trouvée avec ce nom.")

    elif action == "a":
        montant_ajoute = float(input("Combien d'argent voulez-vous rajouter? "))
        argent += montant_ajoute
        print("Vous avez ajouté", montant_ajoute, "euros. Il vous reste maintenant", argent, "euros ce mois-ci.")

else :
    print("Action non reconnue. Veuillez réessayer.")   
