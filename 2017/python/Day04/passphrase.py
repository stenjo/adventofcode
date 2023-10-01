
def isValid(phrase):
    parts = phrase.split(' ')
    for i in range(len(parts)):
        if parts[i] in parts[i+1:]:
            return False
    
    return True

def countValidPassPhrases(phrases):
    count = 0
    for phrase in phrases:
        if isValid(phrase.strip()):
            count += 1
            
    return count

def sortString(str):
    return ''.join(sorted(str))

def isAnagram(first, second):
    return sortString(first) == sortString(second)

def hasAnagram(phrase):
    parts = phrase.strip().split(' ')
    for i in range(len(parts)):
        for j in range(len(parts[i+1:])):
            if isAnagram(parts[i], parts[i+j+1]):
                return True
    
    return False    

def countValidWithoutAnagrams(phrases):
    count = 0
    for phrase in phrases:
        if isValid(phrase) and hasAnagram(phrase) == False:
            count += 1
            
    return count