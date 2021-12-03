# Advent of Code 2018: https://adventofcode.com/2018/day/2

inputData = open('../data/input2.txt','r')
testData = ['abcdef','bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee','ababab']
testData2 = ['abcde','fghij', 'klmno', 'pqrst', 'fguij', 'axcye','wvxyz']

data = inputData.readlines()
#data = testData2
twos = 0
threes = 0

def hastwo(s):
    for c in s:
        if s.count(c) == 2: 
            return True
    return False

def hasthree(s):
    for c in s:
        if s.count(c) == 3:
            return True
    return False
    
def differ(s1, s2):
    diffCount = 0
    idx = 0
    result = ''
    for c in s1:
        if c == s2[idx]:
            result += c
        else:
            diffCount += 1
        idx = idx + 1
#    print('Diffcount: ', diffCount, ' result: ', result)
    if diffCount == 1:
        return result
    else:
        return ''

for id in data:
    for other in data:
        r = differ(id, other)
        if r.count('') > 2:
            print(r)
    
    lastId = id
    result = id + ' '
    if hastwo(id):
        result = result + 'Has twos '
        twos = twos + 1
    if hasthree(id):
        threes = threes + 1
        result = result + 'Has threes '

    #print(id, '- twos: ', twos, ' threes: ', threes, ' ', result)

print (twos * threes)
