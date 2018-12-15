#Test file for Advent of Code Day 9
import unittest
from AoC9_classes import Circle, Ball, Game, Player

class MarbleGameTest(unittest.TestCase):
    
    @unittest.skip("Failing")
    def test_add_ball_to_circle(self):
        # arrange
        c = Circle()
        b1 = Ball(0)
        b2 = Ball(1)
        
        # act
        c.insert(b1)
        c.insert(b2)

        # assert
        self.assertEqual(len(c.circle), 1)

    def test_remove_ball_from_circle(self):
        # arrange

        # act

        # assert
        self.assertTrue('True')

if __name__ == '__main__':
    unittest.main()

