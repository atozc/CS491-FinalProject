import unittest
from Enemies import *
from pokemonBattle import * 

#unit tests suite 

#unit tests for functions 
class testPokemonBattle(unittest.TestCase):
    def test_chooseyourstarter(self):
        self.assertEqual(chooseyourstarter(), {'name': 'Chimchar', 'HP': 44, 'Attack': 58, 'Defense': 44})

    def test_introduction(self): 
        pass

    #def test_isPokemonAlive(self, pokemon):
        #pokemon = chimchar
        #isPokemonAlive(chimchar)
        #self.assertEqual(isPokemonAlive(pokemon), pokemon['HP'])

    #def test_chimchar(self, enemy):
        #enemyhealth = 50
        #defended = 5
        #enemy = generatePokemon()
        #self.assertEqual(chimchar(enemy), int(enemyhealth) - defended)

    #def test_move(self, pokemon, enemy): 
        #pokemon = pokemon['name'] == 'Chimchar'
        #self.assertEqual(move(pokemon, enemy), chimchar(enemy))

@unittest.skip("can't test random")
class test_Enemies(unittest.TestCase):
    pass
    
#if __name__ == '__main__':
unittest.main()