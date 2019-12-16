

from AoC16_classes import FFT

infile = open('data/input_16.txt','r')
inputData1 = infile.readline().strip()

pattern = [0, 1, 0, -1]
s = FFT(pattern, inputData1)
result = s.RunPhase(100)

# Part 1:
print('Part1:', result)
