# Advent of Code 2018: https://adventofcode.com/2018/day/3
# #1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2

import pprint

inputData = open('../data/input3.txt','r')
testData = ['#1 @ 1,3: 4x4','#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']

data = inputData.readlines()
# data = testData

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


def patch(claim):
    id, at, pos, size = claim.replace(':','').split(' ') 
    x,y = pos.split(',')
    w,h = size.split('x')
    patches = []
    for posx in range(int(x)+1, int(x)+int(w)+1):
        for posy in range(int(y)+1,int(y)+int(h)+1):
            patches.append([posx, posy])

    return patches

rquests = dict()
requestkeys = []
maxX = 0
maxY = 0
for item in data:
    id, at, pos, size = item.replace(':','').split(' ') 
    x,y = pos.split(',')
    w,h = size.split('x')
    patches = []
    for posx in range(int(x)+1, int(x)+int(w)+1):
        for posy in range(int(y)+1,int(y)+int(h)+1):
            patches.append([posx, posy])
            if maxX < posx:
                maxX = posx
            if maxY < posy:
                maxY = posy

    rquests[id] = patches
    requestkeys.append(id)

pp = pprint.PrettyPrinter(width=180, compact=True)
# pp.pprint(rquests)
# print('Request keys:', requestkeys)

fabricSheet = []
patchCount = 0
for key, value in rquests.items():
    # print(key)
    idx = 0
    for item in value:
        if item not in fabricSheet:
            fabricSheet.append(item)
        else:
            for rkey, rvalue in rquests.items():
                if item in rvalue:
                    if rkey in requestkeys:
                        requestkeys.remove(rkey)
            patchCount +=1    
          
        idx += 1
        # print(item)
    print(key)

print('\nPart 1:', patchCount, 'square inches of fabric are within two or more claims')
print(len(fabricSheet), 'square inches of sheet requested. Sheet size is:', maxX+1, 'width by', maxY+1, 'height')

# pp.pprint(fabricSheet)
# print(requestkeys)

print('\nPart 2: Request', requestkeys, 'is the only request intact\n')



#overlap(testData[0], testData[1])
#print(matrix(testData[1]))
