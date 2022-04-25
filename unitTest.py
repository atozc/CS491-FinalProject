import unittest
from Enemies import *
from pokemonBattle import * 

#unit tests suite 

#unit tests for functions 

#Tests pokemonBattle.py file
class testPokemonBattle(unittest.TestCase):
    def test_chooseyourstarter(self):
        self.assertEqual(chooseyourstarter(), {'name': 'Chimchar', 'HP': 44, 'Attack': 58, 'Defense': 44})

    #can't test print statements
    def test_introduction(self): 
        pass

    def test_isPokemonAlive(self, pokemon):
        pokemon = chimchar
        isPokemonAlive(chimchar)
        self.assertEqual(isPokemonAlive(pokemon), pokemon['HP'])

    def test_chimchar(self, enemy):
        enemyhealth = 50
        defended = 5
        enemy = generatePokemon()
        self.assertEqual(chimchar(enemy), int(enemyhealth) - defended)

    def test_piplup(self, enemy):
        enemyhealth = 50
        defended = 5
        enemy = generatePokemon()
        self.assertEqual(piplup(enemy), int(enemyhealth) - defended)

    def test_turtwig(self, enemy):
        enemyhealth = 50
        defended = 5
        enemy = generatePokemon()
        self.assertEqual(turtwig(enemy), int(enemyhealth) - defended)

    def test_move(self, pokemon, enemy): 
        pokemon = pokemon['name'] == 'Chimchar'
        self.assertEqual(move(pokemon, enemy), chimchar(enemy))

#Test Enemies.py file
class test_Enemies(unittest.TestCase):
    #can't test random output
    def test_generatePokemon(self):
        pass
    
    #can't test random output
    def test_encounter(self):
        pass

    def test_damageDone(self, enemy, pokemon):
        resultingHP = 7
        self.assertEqual(damageDone(enemy, pokemon), resultingHP)
    
if __name__ == '__main__':
    unittest.main()
    print("Everything Passed.")