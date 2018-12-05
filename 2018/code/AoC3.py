# Advent of Code 2018: https://adventofcode.com/2018/day/3
# #1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2


inputData = open('../data/input3.txt','r')
testData = ['#1 @ 1,3: 4x4','#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
testData2 = ['abcde','fghij', 'klmno', 'pqrst', 'fguij', 'axcye','wvxyz']

#data = inputData.readlines()
data = testData
#data = testData2

def overlap(patch1, patch2):
    #range()
    a = patch1.replace(':','').split(' ')
    matrix = [a[2].split(','),a[3].split('x')]
    b = patch2.split(' ')
    print (matrix)

def matrix(s):
    l = s.replace(':','').split(' ')    
    m = [l[2].split(','), l[3].split('x')]
    r = [ range((int)(m[0][0]),(int)(m[0][1])), range((int)(m[1][0])*1000, (int)(m[1][1])*1000)]
    o = []
    #print(range((int)(m[0][0])+1,(int)(m[0][0])+(int)(m[1][0])))
    for h in range(((int)(m[0][1])+1)*1000, ((int)(m[1][1])+1)*1000, 1000):
        # print(h)
        for w in range((int)(m[0][0])+1,(int)(m[0][0])+(int)(m[1][0])+1):
            #print(w)
            o.append(w+h)
    return o

# Python program to illustrate the intersection 
# of two lists using set() method 
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

   
squares =[]
overlapCounter = 0
for item in data:
    m = matrix(item)
    sq = intersection(m,squares)
    if sq != [] :
        overlapCounter += len(sq)
    squares = list(set(squares + m))
    
#     print('      m: ', m)
#     print('     sq: ', sq)
#     print('squares: ', squares)

# print (overlapCounter)

def patch(claim):
    id, at, pos, size = claim.replace(':','').split(' ') 
    x,y = pos.split(',')
    w,h = size.split('x')
    patches = []
    for posx in range(int(x)+1, int(x)+int(w)+1):
        for posy in range(int(y)+1,int(y)+int(h)+1):
            patches.append([posx, posy])

    return patches

fabricSheet = dict()
rquests = dict()
requestkeys = []
for item in data:
    id, at, pos, size = item.replace(':','').split(' ') 
    x,y = pos.split(',')
    w,h = size.split('x')
    patches = []
    for posx in range(int(x)+1, int(x)+int(w)+1):
        for posy in range(int(y)+1,int(y)+int(h)+1):
            patches.append([posx, posy])
    rquests[id] = patches
    requestkeys.append(id)

# print(rquests)
# print(requestkeys)

for key, value in rquests.items():
    print(key)
    idx = 0
    for item in value:
        if item not in fabricSheet.items():
            fabricSheet[str(key)+':'+str(idx)]=item
        else:
            if key in requestkeys:
                requestkeys.remove(key)
        idx += 1
        # print(item)


print(fabricSheet)
print(requestkeys)

# print('Part 1: Guard', guard, 'is most frequently asleep at', asleepAtTime, 'minutes of the midnight hour')



#overlap(testData[0], testData[1])
#print(matrix(testData[1]))
