from Wordlist import *  # Permet d'importer les univers.
from tkinter import *  # Import de tkinter

#Fonction globale utilisant les autres fonctions pour permettre d'afficher le nom final généré
def randomgen():
    if (univers.get() != "Univers"):

        # Appel de la fonction choix_univer
        nom_univers, prenom_univers = choix_univers()

        # Appel de la fonction de génération de nom
        nom_genere=randomgen_nom(nom_univers)
        prenom_genere = randomgen_prenom(prenom_univers)

        # Affichage du nom généré
        nom_gen.set("%s %s" % (nom_genere, prenom_genere))

    else:
        nom_gen.set("Pas d'univers selectionne")





#Fonction permettant de générer un prénom en fonction de l'univers selectionné
def randomgen_prenom(prenom_univers):
    prenom = Prenom.get()
    prenom_genere = wordlist[prenom_univers][prenom[2].upper()]
    return prenom_genere


#Fonction permettant de générer un nom en fnction de l'univers selectionné
def randomgen_nom(nom_univers):
    nom = Nom.get()
    nom_genere = wordlist[nom_univers][nom[0].upper()]
    return nom_genere



#Fonction permettant de définir t'univers choisi sur le menu dans les variables necessaires a la géneration du nom
def choix_univers():
    nom_univers = "%s_nom" % (univers.get())
    prenom_univers = "%s_prenom" % (univers.get())
    return nom_univers,prenom_univers






#Initialisation fenêtre
fenetre = Tk()
fenetre.title("Générateur de nom")


#Déclaration des variables de text
Prenom = StringVar()   #prenom saisi
Prenom.set('Prenom')

Nom = StringVar()  #nom saisi
Nom.set('Nom')

nom_gen = StringVar()   #nom final généré
nom_gen.set(' ')

menu_univers = ('game_of_thrones', 'star_wars', 'warcraft') #liste des univers pour le menu
univers = StringVar()
univers.set("Univers")

#Zone de text pour la saisie du nom de l'utilisateur
input_Nom = Entry(fenetre, textvariable=Nom)
input_Nom.grid(column=2, row=3, padx=10,pady=10, ipady=20)

#Zone de text pour la saisie du prenom de l'utilisateur
input_Prenom = Entry(fenetre, textvariable=Prenom)
input_Prenom.grid(column=3, row=3, padx=10,pady=10, ipady=20)

#Bouton permettant de générer le nom et prénom
button_Chiffrer = Button(fenetre, text="Générer !", command=randomgen)
button_Chiffrer.grid(row=4, column=3, padx=15,pady=30, ipady=10)

#Menu déroulant avec les différent univers
select_universe = OptionMenu(fenetre, univers, *menu_univers)
select_universe.grid(row=4, column = 2, padx=15,pady=5, ipady=10)

#Zone de sortie
lab_res = Label(fenetre, textvariable=nom_gen)
lab_res.grid(column=3, row=7, padx=10,pady=10, ipady=20)

fenetre.mainloop()
