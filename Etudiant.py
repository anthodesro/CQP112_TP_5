# Anthony Desrochers, Julien Lemieux, Amélie Larcher, Maude Beauregard

import os
from interface import Interface

#Variables
clear = lambda: os.system('cls')

class Etudiant:
        def __init__(self):
            self.cip = 0
            self.nom = ""
            self.date = ""
            self.adresse = ""
            self.cours = Cours()

class Cours:
        def __init__(self):
            self.lst_cours = []

        def add_cours(self,add_cours):
            self.lst_cours.append(add_cours)

        def supp_cours(self,supp_cours):
            try:
                self.lst_cours.remove(supp_cours)
            except ValueError:
                pass

class Database:
    def save(self, listeEtudiant):
        for etudiant in listeEtudiant:
            with open(".\etudiants\%s.txt" % etudiant.cip, "w+") as fichier_etudiant:
                fichier_etudiant.write("CIP : " + str(etudiant.cip) + "\n")
                fichier_etudiant.write("Nom : " + str(etudiant.nom) + "\n")
                fichier_etudiant.write("Date : " + str(etudiant.date) + "\n")
                fichier_etudiant.write("Adresse : " + str(etudiant.adresse) + "\n")
                fichier_etudiant.write("Liste de cours : " + str(etudiant.cours.lst_cours) + "\n")
            print("Étudiant #" + etudiant.cip + " sauvgarder\n")
        return

interface = Interface()
lst_etudiant = []
database = Database()

while True:
    option1 = interface.ask("Choisir une option (Nouveau (n), MAJ (m) ou Quitter (q)) : ")
    clear()
    if option1 == "n":
        etudiant = Etudiant()

        etudiant.cip = interface.ask("Enter un CIP : ")
        etudiant.nom = interface.ask("Enter un nom : ")
        etudiant.date = interface.ask("Enter une date de naissance : ")
        etudiant.adresse = interface.ask("Enter une adresse : ")

        lst_etudiant.append(etudiant)

        clear()

        pass

    if option1 == "m":
        while True:
            CIP = interface.ask("Entrer le CIP de l'étudiant :  ")

            for etudiant in lst_etudiant:
                if(etudiant.cip == CIP):
                    while True:
                        option2 = interface.ask("Choisir une option (Ajouter (a), Retirer (r) ou Terminer (t)) : ")
                        clear()
                        if option2 == "a":
                            print(etudiant.cours.lst_cours)
                            etudiant.cours.add_cours(interface.ask("Enter un cours à ajouter : "))
                            clear()
                            pass

                        if option2 == "r":
                            print(etudiant.cours.lst_cours)
                            etudiant.cours.supp_cours(interface.ask("Enter un cours à retirer : "))
                            clear()
                            pass

                        if option2 == "t":
                            clear()
                            break
            break

    if option1 == "q":

        database.save(lst_etudiant)

        break