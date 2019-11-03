import unittest
from Generateur_de_nom import * #Permet d'importer le fichier principale
from Univers import * #Permet d'importer les univers 


class TestGenerateurDeNom(unittest.TestCase):


    def test_choix_univer(self):
        self.assertEqual(choix_univers(), ("star_wars_nom","star_wars_prenom"))

    def test_transformation_ASCII(self):
        #test des resultats avec nom=Corentin, prenom=Renquet, univers=Star wars
        self.assertEqual(randomgen_nom("star_wars_nom"),("Padawan"))
        self.assertEqual(randomgen_nom("star_wars_prenom"), ("Solo"))