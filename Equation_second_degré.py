from math import*

"""Ce projet permet de résoudre une équation du second degré de la forme
ax² + bx + c = 0, à partir de valeurs saisies par l’utilisateur.

L’objectif principal du projet était de mettre en pratique
les structures conditionnelles, la manipulation des entrées utilisateur
et l’utilisation de modules standards,
notamment le module math pour le calcul de la racine carrée.

Le programme commence par afficher correctement l’équation
selon les signes de a, b et c, ce qui m’a demandé de gérer
plusieurs cas conditionnels afin d’obtenir un affichage mathématique lisible.

Ensuite, il calcule le discriminant Δ et détermine le nombre de solutions
(aucune, une ou deux) en fonction de sa valeur.
"""

print("veuillez saisir les valeurs de a, b et c avec a,b,c != 0")

a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

if a != 1 :
    if b < 0 and c < 0 :
        print(str(a)+"x^2",str(b)+"x",c,"= 0")
    elif b < 0 and c > 0 :
        print(str(a)+"x^2",str(b)+"x","+",c,"= 0")
    elif b == 0 and c > 0 :
        print(str(a)+"x^2","+",c,"= 0")
    elif b == 0 and c < 0 :
        print(str(a)+"x^2",c,"= 0")
    elif b < 0 and c == 0 :
        print(str(a)+"x^2",str(b)+"x = 0")
    elif b > 0 and c == 0 :
        print(str(a)+"x^2","+",str(b)+"x = 0")
    elif b > 0 and c < 0 :
        print(str(a)+"x^2","+",str(b)+"x",c,"= 0")
    elif b > 0 and c > 0 :
        print(str(a)+"x^2","+",str(b)+"x","+",c,"= 0")
else :
    if b < 0 and c < 0 :
        print("x^2",str(b)+"x",c,"= 0")
    elif b < 0 and c > 0 :
        print("x^2",str(b)+"x","+",c,"= 0")
    elif b == 0 and c > 0 :
        print("x^2","+",c,"= 0")
    elif b == 0 and c < 0 :
        print("x^2",c,"= 0")
    elif b < 0 and c == 0 :
        print("x^2",str(b)+"x = 0")
    elif b > 0 and c == 0 :
        print("x^2","+",str(b)+"x = 0")
    elif b > 0 and c < 0 :
        print("x^2","+",str(b)+"x",c,"= 0")
    elif b > 0 and c > 0 :
        print("x^2","+",str(b)+"x","+",c,"= 0")
    
D = b*b - 4*a*c

print("D = b*b - 4*a*c","  =>   D =",D)

if D < 0 :
    print("cette équation n'a pas de solution dans lR")
elif D == 0 :
    x0 = -b/2*a
    print("=>  x0 = -b/2*a =",x0,"d'où cette équation a une unique solution :",x0)
else :
    x1 = (-b-sqrt(D))/2*a
    x2 = (-b+sqrt(D))/2*a
    print("=>  x1 = (-b-sqrt(D)) / 2*a =",x1)
    print("et  x2 = (-b+sqrt(D)) / 2*a = ",x2)
    print("d'où cette équation admet deux solution qui sont :",x1,"et",x2)





