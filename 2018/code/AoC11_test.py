#Test file for Advent of Code Day 11
import unittest
from AoC11 import FuelCells

class FuelcellTest(unittest.TestCase):

    fuelCells = ''
    
    def setUp(self):
        self.fuelCells = FuelCells(8)

    def test_calc_power_level_single(self):
        # arrange
        test = [[3,5,8],[122,79,57],[217,196,39],[101,153,71]]
        result=[]
        # act
        for t in test:
            self.fuelCells.GridSerialNo = t[2]
            result.append(self.fuelCells.calPowerLevel(t[0],t[1]))
            

        # assert
        self.assertEqual(result, [4, -5, 0, 4])

    def test_get_power_level_single(self):
        # arrange
        test = [[3,5,8,4],[122,79,57,-5],[217,196,39,0],[101,153,71,4]]
        calc= []
        get = []
        ref =[]
        # act
        for t in test:
            self.fuelCells.initialize(t[2])
            calc.append(self.fuelCells.calPowerLevel(t[0],t[1]))
            get.append(self.fuelCells.getPowerLevel(t[0],t[1]))
            ref.append(t[3])

        # assert
        self.assertEqual(calc, get)
        self.assertEqual(calc, ref)

    def test_matrix_total_power(self):
        # arrange
        m = [ [
                [4,3,1],
                [4,3,2],
                [4,4,4]  
              ],[
                [4,3,3],
                [3,3,3],
                [3,4,4]  
              ]
            ]
        result = []
        # act
        for g in m:
            result.append(self.fuelCells.totalPower(1,1,g))

        # assert
        self.assertEqual(result,[29,30])

    def test_total_power_grid(self):
        # arrange
        test = [[33,45,18],[21,61,42]]
        result=[]
        
        #act
        for t in test:
            self.fuelCells.initialize(t[2])
            self.fuelCells.print3x3(t[0],t[1], self.fuelCells.Map)
            result.append(self.fuelCells.totalPower(t[0],t[1], self.fuelCells.Map))

        # assert
        self.assertEqual(result, [29, 30])


if __name__ == '__main__':
    unittest.main()
