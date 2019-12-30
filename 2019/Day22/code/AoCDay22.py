#
#
#


from AoCDay22_classes import SpaceDeck

infile = open('data/input_22.txt','r')
inputData1 = infile.readlines()

# Part 1
e = SpaceDeck(10007)
result = e.RunDeal(inputData1)
print("Part 1: ", result.index(2019))

# Part 2
e = SpaceDeck(119315717514047)
result = e.GetCardAtPosOnDeck(inputData1, 2020, 101741582076661)
print("Part 2: ", result)
