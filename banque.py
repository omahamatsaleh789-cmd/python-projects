from datetime import datetime

"""Ce projet est un mini système bancaire. 
Il simulait la gestion de comptes avec des fonctionnalités telles que 
la création de comptes, les dépôts, les retraits, le blocage de comptes 
et l’enregistrement des opérations dans un fichier. 
Ce projet utilise des fonctions , des boucles, des conditions, 
ainsi que la gestion des fichiers et le module datetime. 
"""

comptes = [
    {"id": 1, "nom": "Client_1", "solde": 1345.53, "actif": True},
    {"id": 2, "nom": "Client_2", "solde": 4364.54, "actif": True},
    {"id": 3, "nom": "Client_3", "solde": 43544.2, "actif": False},
    {"id": 4, "nom": "Client_4", "solde":45346.5, "actif": True},
    {"id": 5, "nom": "Client_5", "solde": 615644.54, "actif": True},
    ]


def ecrire_historique(message):
    with open("operations.txt", "a") as f:
        f.write(message + "\n")


def afficher_comptes(comptes) :
    for compte in comptes :
        if compte["actif"] :
            print(f'{compte["id"]} - {compte["nom"]}, solde : {compte["solde"]}, activité : actif')
        else :
            print(f'{compte["id"]} - {compte["nom"]}, solde : {compte["solde"]}, activité : non actif')


def rechercher_compte(comptes, id_compte) :
    for id in comptes :
        if id["id"] == id_compte :
            if id["actif"] :
                return f'{id["id"]} - {id["nom"]}, solde : {id["solde"]}, activité : actif'
            else :
                return f'{id["id"]} - {id["nom"]}, solde : {id["solde"]}, activité : non actif'
    return None


def depot(comptes, id_compte, montant) :
    if montant <= 0 :
        print("montant invalide (> 0)")
        return
    
    for compte in comptes :
        if not compte["actif"] :
            print("cette compte n'est pas actif")
        elif compte["id"] == id_compte :
            solde = compte["solde"] + montant
            
            date_heure = datetime.now().strftime("%Y-%m-%d %H:%M")
            message = f"[{date_heure}] Dépôt : {montant} | Compte : {compte['nom']} | solde : {solde}"
            ecrire_historique(message)
            
            print("montant ajoutée avec succès")
            return solde
            
        
    print("Compte introuvable")
            
            
def retrait(comptes, id_compte, montant) :
    for compte in comptes :
        if montant > compte["solde"] :
            print("solde insuffisant")
        elif not compte["actif"] :
            print("cette compte n'est pas actif")
        elif compte["id"] == id_compte :
            solde = compte["solde"] - montant
            
            date_heure = datetime.now().strftime("%Y-%m-%d %H:%M")
            message = f"[{date_heure}] Retrait : {montant} | Compte : {compte['nom']} | solde : {solde}"
            ecrire_historique(message)
            
            print("montant retirer avec succès")
            return solde
                
    print("Compte introuvable")
    
    
def bloque(comptes, id_compte) :
    for compte in comptes :
        if compte["id"] == id_compte :
            return compte["actif"] == False
            
def debloque(comptes, id_compte) :
    for compte in comptes :
        if compte["id"] == id_compte :
            return compte["actif"] == True


if __name__ == "__main__":

    choix = ""

    while choix != "5":
        print("\n===== MENU =====")
        print("1. Afficher les comptes")
        print("2. Dépôt")
        print("3. Retrait")
        print("4. Bloquer / Débloquer un compte")
        print("5. Quitter")

        choix = input("Votre choix (1-5) : ")

        if choix == "1":
            afficher_comptes(comptes)

        elif choix == "2":
            id_compte = int(input("ID de compte : "))
            montant = int(input("Montant : "))
            depot(comptes, id_compte, montant)

        elif choix == "3":
            id_compte = int(input("ID de compte : "))
            montant = int(input("Montant : "))
            retrait(comptes, id_compte, montant)
            
        elif choix == "4":
            bloquer_deploquer = (input("1. Bloquer | 2. Déploquer : "))
            if bloquer_deploquer == "1" :
                id_compte = int(input("ID de compte : "))
                bloque(comptes, id_compte)
                
            elif bloquer_deploquer == "2" :
                id_compte = int(input("ID de compte : "))
                debloque(comptes, id_compte)
                
        elif choix == "5":
            print("Au revoir")

        else:
            print("Choix invalide")

