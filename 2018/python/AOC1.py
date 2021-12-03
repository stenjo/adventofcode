
inputData = open('../data/input.txt','r')
testData = [+3, +3, +4, -2, -4]
data = inputData.readlines()
#data = testData
frequency = 0
found = 0
savedFrequencies = []
while not found:
    for num in data:
        frequency = frequency + int(num)
        #print (frequency)
        if frequency in savedFrequencies:
            print ('First twice: ', frequency)
            found = 1
            break
        savedFrequencies.append(frequency)
        #print (savedFrequencies)
    
print (frequency)

