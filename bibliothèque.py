from datetime import datetime



livres = [
    {"id": 1, "titre": "python", "auteur": "serpent", "disponible": True},
    {"id": 2, "titre": "css", "auteur": "html_5", "disponible": True},
    {"id": 3, "titre": "html", "auteur": "html_5", "disponible": True},
    {"id": 4, "titre": "c++", "auteur": "c#", "disponible": False},
    {"id": 5, "titre": "java", "auteur": "javace", "disponible": True},
]


def ecrire_historique(message):
    with open("historique.txt", "a") as f:
        f.write(message + "\n")


def afficher_livres(livres):
    for livre in livres:
        etat = "disponible" if livre["disponible"] else "emprunté"
        print(livre["id"], "-", livre["titre"], "-", livre["auteur"], ":", etat)


def rechercher_livre(livres, titre):
    for livre in livres:
        if livre["titre"] == titre:
            return livre
    return None


def emprunter_livre(livres, id_livre):
    for livre in livres:
        if livre["id"] == id_livre:
            if livre["disponible"]:
                livre["disponible"] = False

                date_heure = datetime.now().strftime("%Y-%m-%d %H:%M")
                message = f"[{date_heure}] Livre emprunté : {livre['titre']}"
                ecrire_historique(message)

                print("Livre emprunté :", livre["titre"])
            else:
                print("Livre déjà emprunté")
            return
    print("Livre introuvable")


def rendre_livre(livres, id_livre):
    for livre in livres:
        if livre["id"] == id_livre:
            livre["disponible"] = True

            date_heure = datetime.now().strftime("%Y-%m-%d %H:%M")
            message = f"[{date_heure}] Livre rendu : {livre['titre']}"
            ecrire_historique(message)

            print("Livre rendu :", livre["titre"])
            return
    print("Livre introuvable")


if __name__ == "__main__":

    choix = ""

    while choix != "5":
        print("\n===== MENU =====")
        print("1. Afficher les livres")
        print("2. Rechercher un livre")
        print("3. Emprunter un livre")
        print("4. Rendre un livre")
        print("5. Quitter")

        choix = input("Votre choix (1-5) : ")

        if choix == "1":
            afficher_livres(livres)

        elif choix == "2":
            titre = input("Titre du livre : ")
            livre = rechercher_livre(livres, titre)
            if livre:
                print(livre)
            else:
                print("Livre non trouvé")

        elif choix == "3":
            id_livre = int(input("ID du livre : "))
            emprunter_livre(livres, id_livre)

        elif choix == "4":
            id_livre = int(input("ID du livre : "))
            rendre_livre(livres, id_livre)

        elif choix == "5":
            print("Au revoir")

        else:
            print("Choix invalide")
