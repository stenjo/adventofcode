# Advent of Code 2019: https://adventofcode.com/2019/day/14
# 
# 
import math, re
import numpy as np


class NanoFactory():
    
    reactions = []
    chemicals = {}

    def __init__(self, reactions):
        super().__init__()
        self.reactions = reactions
        self.MapChemicals()

    def CalculateOre(self, fuel, chem):
        chemicals = self.GetChemicalsRequired(fuel, chem)
        done = False
        while done == False:
            for c in list(chemicals):
                if 'ORE' == c:
                    continue

                newChems = self.GetChemicalsRequired(chemicals[c], c)
                chemicals = self._add_dicts(chemicals, newChems)

            done = True
            for c in self.chemicals:
                if self.chemicals[c]['updated'] == False:
                    if c in chemicals:
                        del chemicals[c]
                else:
                    done = False
            done = done
            for c in self.chemicals:
                self.chemicals[c]['updated'] = False

        return chemicals['ORE']

    # recursive
    def GetAmount(self, amnt, chem):
        chems = self.GetChemicalsRequired(amnt,chem)
        sum=0
        for c in chems:
            if c != 'ORE':
                sum += self.GetAmount(chems[c]*amnt, c)
            else:
                multiplier = math.ceil(amnt/self.chemicals[chem]['amount'])
                sum += chems[c]*multiplier
        return sum

    def _add_dicts(self, dicta, dictb):

        for item in dictb:
            if item not in dicta:
                dicta[item] = dictb[item]
            else:
                dicta[item] += dictb[item]
    
            if item in self.chemicals:
                self.chemicals[item]['updated'] = True

        return dicta

    def GetChemicalsRequired(self, amount, chem):
        newChemicals = {}
        if chem == 'ORE':
            return newChemicals

        required = self.chemicals[chem]
        amt = required['amount']
        multiplier = math.ceil(amount/amt)
        for c in required['source']:
            newChemicals[c] = required['source'][c]*multiplier

        return required['source']

    def MapChemicals(self):

        for r in self.reactions:
            chem, amount, chemdict = self.SplitReaction(r)
            self.chemicals[chem] = {'amount': amount, 'updated': False, 'source': chemdict}
       

    def SplitReaction(self, reaction):
        source, dest = reaction.split('=>')
        dest_amnt, dest_chem = dest.strip().split(' ')
        chems = {}
        for s in source.strip().split(','):
            amount, chem = s.strip().split(' ')
            chems[chem.strip()] = int(amount)

        return (dest_chem, int(dest_amnt), chems)

