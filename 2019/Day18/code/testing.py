'''
Iterate over all the key value pairs in dictionary and call the given
callback function() on each pair. Items for which callback() returns True,
add them to the new dictionary. In the end return the new dictionary.
'''
def filterTheDict(dictObj, callback):
    newDict = dict()
    # Iterate over all the items in dictionary
    for (key, value) in dictObj.items():
        # Check if item satisfies the given condition then add to new dict
        if callback((key, value)):
            newDict[key] = value
    return newDict
 
def main():
 
    dictOfNames = {
       7 : 'sam',
       8: 'john',
       9: 'mathew',
       10: 'riti',
       11 : 'aadi',
       12 : 'sachin'
    }
 
    print('Original Dictionary : ')
    print(dictOfNames)
 
    print('*** Filter a Dictionary by conditions by Iterating over elements ***')
 
    print('Filter a Dictionary by conditions on keys')
 
    newDict = dict()
    # Iterate over all the items in dictionary and filter items which has even keys
    for (key, value) in dictOfNames.items():
       # Check if key is even then add pair to new dictionary
       if key % 2 == 0:
           newDict[key] = value
 
    print('Filtered Dictionary : ')
    print(newDict)
 
    # Filter a dictionary to keep elements only whose keys are even
    newDict = filterTheDict(dictOfNames, lambda elem : elem[0] % 2 == 0)
 
    print('Filtered Dictionary : ')
    print(newDict)
 
    # Filter a dictionary to keep elements only whose values are string of length 6
    newDict = filterTheDict(dictOfNames, lambda elem: len(elem[1]) == 6)
 
    print('Filtered Dictionary : ')
    print(newDict)
 
    print('*** Filter a Dictionary by filter()***')
 
    # Filter dictionary by keeping elements whose keys are divisible by 2
    newDict = dict(filter(lambda elem: elem[0] % 2 == 0, dictOfNames.items()))
 
    print('Filtered Dictionary : ')
    print(newDict)
 
    # Filter dictionary by keeping elements whose values are string of length 6
    newDict = dict(filter(lambda elem: len(elem[1]) == 6,dictOfNames.items()))
 
    print('Filtered Dictionary : ')
    print(newDict)
 
    print('*** Filter a Dictionary by Dict Comprehension ***')
 
    # Filter dictionary by keeping elements whose keys are divisible by 2
    newDict = { key:value for (key,value) in dictOfNames.items() if key % 2 == 0}
 
    print('Filtered Dictionary : ')
    print(newDict)
 
    # Filter dictionary by keeping elements whose values are string of length 6
    newDict = {key: value for (key, value) in dictOfNames.items() if len(value) == 6 }
 
    print('Filtered Dictionary : ')
    print(newDict)
 
 
if __name__ == '__main__':
  main()