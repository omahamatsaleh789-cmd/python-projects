from datetime import datetime

"""Ce projet concernait un système de gestion de notes d’étudiants. 
L’objectif principal est de permettre l’ajout d’étudiants, l’enregistrement de leurs notes, 
le calcul des moyennes et l’affichage des résultats. 
Le projet utilisait des listes et des dictionnaires pour stocker les données, 
ainsi que des fonctions pour structurer le code. 
"""

etudiants = [{
    "id": 1,
    "nom": "Etudiant_1",
    "notes": [11, 18, 17, 10, 15]
},
{
    "id": 2,
    "nom": "Etudiant_2",
    "notes": [12, 13, 5, 4, 19]
},
{
    "id": 3,
    "nom": "Etudiant_3",
    "notes": [9.5, 13.5, 12, 16, 13]
},
{
    "id": 4,
    "nom": "Etudiant_4",
    "notes": [8, 15, 19, 12, 14]
},
{
    "id": 5,
    "nom": "Etudiant_5",
    "notes": [13, 18, 19, 12, 20]
},
{
    "id": 6,
    "nom": "Etudiant_6",
    "notes": [12, 15, 20, 10, 5]
}]


def ecrire_historique(message):
    with open("resultats.txt", "a") as f:
        f.write(message + "\n")


def afficher_etudiants (etudiants) :
    for i in etudiants :
        print (i["id"], "- nom :", i["nom"],". Notes :", i["notes"])


def calculer_moyenne (notes) :
    long = len (notes)
    note = 0
    if notes :
        for i in notes :
            note += i
        return note / long
    return None 


def moyenne_etudiant(etudiants, id_etudiant) :
    for i in etudiants :
        if i["id"] == id_etudiant :
            moyen = calculer_moyenne (i["notes"])
            
            date_heure = datetime.now().strftime("%Y-%m-%d %H:%M")
            message = f"[{date_heure}] Nom : {i['nom']} | Moyenne : {moyen}"
            ecrire_historique(message)

            print("La moyen de", i["nom"], "est :",moyen)


def ajouter_note(etudiants, id_etudiant, note) :
    for i in etudiants :
        if i["id"] == id_etudiant and 0 <= note <= 20 :
            return i["notes"].append(note)
    return print("veuillez entrez une note compris entre 0 et 20 ")


if __name__ == "__main__":

    choix = ""

    while choix != "4":
        print("\n===== MENU =====")
        print("1. Afficher les étudiants")
        print("2. Calculer la moyenne d’un étudiant")
        print("3. Ajouter une note")
        print("4. Quitter")

        choix = input("Votre choix (1-4) : ")
        
        
        if choix == "1" :
            afficher_etudiants (etudiants)
            
        elif choix == "2" :
            id_etudiant = int(input("Vueillez entrez l'id de l'etudiant : "))
            moyenne_etudiant(etudiants, id_etudiant)
            
        elif choix == "3" :
            id_etudiant = int(input("ID de l'étudiant : "))
            note = int(input("La note : "))
            ajouter_note(etudiants, id_etudiant, note)
        
        elif choix == "4" :
            print("Au revoir")

        else:
            print("Choix invalide")
        







                 

