import random #import les modules
import time

#variables
hp = 20 #niveau de vie
enn_dif = 2  #difficulte de l'ennemie
num_adv = 0  #nom d'adversaire et nombre d'adversaire
victory = 0 #nombre de victoire
defeat = 0 #nombre de defaite
streak = 0 #nombre de suite de victoire

def interaction(num_adv):
    global streak, enn_dif, hp, victory, defeat #globalize les variables pour changer leurs valeurs

    print(f"Vous tombez face à face avec un adversaire de difficulté : {enn_dif}")
    print(f"""Adversaire : {num_adv}
Niveau de vie de l’usager : {hp}
Combat {num_adv} : {victory} vs {defeat}""")
    input("lancer la des en appuyant sur espace")
    time.sleep(2)
    rand = random.randint(1, 6)  #donne nombre de de
    print("\nnombre du des: " + str(rand))
    if rand >= enn_dif: #determine si le monstre ou le personnage principale gagne
        print("vous avez gagner")
        streak += 1 #augmente le nombre de suite a la victoire
        enn_dif += 1 #augmente la difficulte
        input("continuer en appuyant sur espace")
        print(f"""
        Niveau de vie : {hp} 
        Nombre de victoires consécutives : {streak}
        """)
        input('appuyer sur "espace" pour continuer')


    else:
        print("vous avez perdu")
        hp -= enn_dif #reduis le niveau de vie du personnage
        streak = 0 #recommence la suite de victoire
        if enn_dif < 2: #reduit la difficulte du monstre si la difficulte est plus grande que 2
            enn_dif -= 1
        print(f"niveau de vie: {hp}")
        if hp <= 0: #si niveau de vie est a 0 le personnage perd
            quit(f"le monstre vous a vaincu. score: {victory}")




def battle():
    global hp #change la valeur de hp globale
    print("""Que voulez-vous faire ? 
    	1- Combattre cet adversaire
    	2- Contourner cet adversaire et aller ouvrir une autre porte
    	3- Afficher les règles du jeu
    	4- Quitter la partie
    """)
    question = input("quel est votre action?") #demande l'action
    if question == "1":
        interaction(num_adv) #commence le combat contre le monstre
    elif question == "2":
        hp -= 1 #reduit le niveau de vie si joueur choisi de contourner
        if hp == 5: #si nv est trop faible le joueur perd
            quit("le monstre vous a attrapé")
        print("succes!")
    elif question == "4": #quit le programme
        quit("Merci et au revoir... ")
    else: #si joueur choisi un input qui est invalide ou choici 4 montre le tutoriel
        print("""Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.


La partie se termine lorsque les points de vie de l’usager tombent sous 0.


L’usager peut combattre (choix 1) ou éviter (choix 2) chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.

         """)
        input("entrer une input pour continuer")
        battle()
def main(): #commence les parties
    while True:
      battle()
      print("vous continuez a marcher")
      time.sleep(2)

main() #commence le jeu

