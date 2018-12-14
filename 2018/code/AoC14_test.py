# Advent of Code 2018: https://adventofcode.com/2018/day/13
#
# Tests

import unittest
from AoC13_classes import MineCart, Cart, Track, TrackPart

testTrack = [
'/->-\\        ',
'|   |  /----\\',
'| /-+--+-\\  |',
'| | |  | v  |',
'\\-+-/  \\-+--/',
'  \\------/   ']

testTrack2 = [
'/>-<\\  ',
'|   |  ',
'| /<+-\\',
'| | | v',
'\\>+</ |',
'  |   ^',
'  \\<->/']

class MineCartTest(unittest.TestCase):
    def test_cart(self):
        # arrange
        # act
        # assert
        self.assertTrue(True)

    def test_add_cart(self):
        # arrange
        mc = MineCart()

        # act
        mc.addCart(Cart(1,2,'^'))
        mc.addCart(Cart(3,4,'v'))
        mc.addCart(Cart(4,5,'>'))

        # assert
        self.assertEqual(mc.numCarts(),3)

    def test_cart_collision(self):
        # arrange
        mc = MineCart()

        # act
        mc.addCart(Cart(1,2,'^'))
        mc.addCart(Cart(3,4,'v'))
        mc.addCart(Cart(4,5,'>'))
        cart = Cart(3,4,'v')

        # assert
        self.assertFalse(mc.hasCollision())
        mc.addCart(cart)
        self.assertTrue(mc.hasCollided(cart))
        self.assertTrue(cart.crashed)

    def test_remove_cart(self):
        # arrange
        mc = MineCart()

        # act
        mc.addCart(Cart(1,2,'^'))
        mc.addCart(Cart(3,4,'v'))
        mc.addCart(Cart(4,5,'>'))
        mc.removeCart(3,4)

        # assert
        self.assertEqual(mc.numCarts(),2)
        self.assertEqual(mc.findCart(4,5).direction,'>')

    def test_get_cart(self):
        # arrange
        mc = MineCart()

        # act
        mc.addCart(Cart(1,2,'^'))
        mc.addCart(Cart(3,4,'v'))
        mc.addCart(Cart(4,5,'>'))

        # assert
        self.assertEqual(mc.findCart(4,5).direction,'>')
        self.assertEqual(mc.findCart(3,4).direction,'v')

    # Track testing
    
    def test_add_track(self):
        # arrange
        t = Track()

        # act
        t.addTrackPart(TrackPart(1,0,'/'))
        t.addTrackPart(TrackPart(1,1,'|'))
        t.addTrackPart(TrackPart(1,2,'|'))
        t.addTrackPart(TrackPart(1,3,'\\'))
        t.addTrackPart(TrackPart(2,3,'-'))
        
        # assert
        self.assertEqual(t.numTrackParts(),5)

    def test_move_cart(self):
        # arrange
        mc = MineCart()
        mc.track.addTrackPart(TrackPart(1,0,'/'))
        mc.track.addTrackPart(TrackPart(1,1,'|'))
        mc.track.addTrackPart(TrackPart(1,2,'|'))
        mc.track.addTrackPart(TrackPart(3,0,'\\'))
        mc.track.addTrackPart(TrackPart(2,0,'-'))
        mc.track.addTrackPart(TrackPart(3,1,'|'))
        mc.addCart(Cart(1,2,'^'))

        # act
        c = mc.getCart(0)
        mc.moveCart(0)
        self.assertEqual([c.x,c.y],[1,1])
        mc.moveCart(0)
        self.assertEqual([c.x,c.y],[1,0])
        mc.moveCart(0)
        self.assertEqual([c.x,c.y],[2,0])
        mc.moveCart(0)
        self.assertEqual([c.x,c.y],[3,0])
        mc.moveCart(0)

        # assert
        self.assertEqual([c.x,c.y],[3,1])
        self.assertEqual(c.direction, 'v')

    def test_validate_track(self):
        # arrange
        mc = MineCart()
        mc.track.addTrackPart(TrackPart(2,0,'-'))
        mc.track.addTrackPart(TrackPart(1,0,'/'))
        mc.track.addTrackPart(TrackPart(1,1,'|'))
        mc.track.addTrackPart(TrackPart(1,2,'|'))
        mc.track.addTrackPart(TrackPart(1,3,'\\'))
        mc.track.addTrackPart(TrackPart(3,0,'\\'))
        mc.track.addTrackPart(TrackPart(3,1,'|'))
        mc.track.addTrackPart(TrackPart(3,2,'|'))
        mc.track.addTrackPart(TrackPart(3,3,'/'))
        mc.track.addTrackPart(TrackPart(2,3,'-'))
        # act
        result = mc.track.validateAllTracks()
    
        # assert
        self.assertIsNone(result)

    # MineCart testing
    def test_load_track_and_carts_minecart(self):
        # arrange
        mc = MineCart()

        # act
        mc.loadTracksAndCarts(testTrack)

        # assert
        self.assertEqual(mc.numCarts(), 2)
        self.assertEqual(mc.track.numTrackParts(), 48)

    def test_find_first_collision(self):
        # arrange
        mc = MineCart()
        mc.loadTracksAndCarts(testTrack)

        # act
        result = mc.findFirstCollision()

        # assert
        self.assertEqual(result, [[7,3]])

    def test_find_last_cart(self):
        # arrange
        mc = MineCart()
        mc.loadTracksAndCarts(testTrack2)

        # act
        result = mc.findLastCart()

        # assert
        # self.assertEqual(result.print(),True)
        self.assertEqual([result.x,result.y], [6,4])

    def test_move_one_step_minecart(self):
        # arrange
        mc = MineCart()
        mc.loadTracksAndCarts(testTrack)
        # act
        mc.moveAllOneStep()
        result = []
        posMoved = [[3,0],[9,4]]

        # assert
        for c in mc.carts:
            result.append([c.x,c.y])

        self.assertEqual(result, posMoved)

    def test_move_bends_and_crossses(self):
        # arrange
        mc = MineCart()
        mc.loadTracksAndCarts(testTrack)

        # act
        mc.moveSteps(3)
        result = []
        posMoved = [[4,1],[11,4]]

        # assert
        for c in mc.carts:
            result.append([c.x,c.y])
        self.assertEqual(result, posMoved)



if __name__ == '__main__':
    unittest.main()

