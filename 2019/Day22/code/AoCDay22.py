
from AoCDay22_classes import SpaceDeck

infile = open('data/input_22.txt','r')
inputData1 = infile.readlines()

# Part 1
e = SpaceDeck(10007)
result = e.RunDeal(inputData1)
print(len(result))
print("Part 1: ", result[2019])

e.comparefiles('input_22.txt', 'output')

# Part 2
# result = w.RunAgain()
# print("Part 2: ", result)
