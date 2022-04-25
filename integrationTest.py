import unittest 
from unittest.mock import patch
from pokemonBattle import *
from Enemies import * 

#Integration Tests
#Used mock to mock user input for testing 

class testGame(unittest.TestCase):
    def setUp(self):
        self.game = runGame() 

    @patch('__builtins__.input') 
    def test_chooseyourstarter(self, m_input):
        m_input.side_effect = [1, 2, 3]
        self.game.chooseyourstarter()

    @patch('__builtins__.input') 
    def test_chimchar(self, m_input):
        m_input.side_effect = [1, 2, 3, 8]
        self.game.chimchar()

    @patch('__builtins__.input') 
    def test_piplup(self, m_input):
        m_input.side_effect = [1, 2, 3, 8]
        self.game.piplup()

    @patch('__builtins__.input') 
    def test_turtwig(self, m_input):
        m_input.side_effect = [1, 2, 3, 8]
        self.game.turtwig()

if __name__ == "__main__":
    unittest.main()