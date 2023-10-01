
from Day04.passphrase import isValid,countValidPassPhrases, isAnagram, hasAnagram, countValidWithoutAnagrams

def test_passphrase():
    
    assert isValid('aa bb cc dd ee') == True
    assert isValid('aa bb cc dd aa') == False
    assert isValid('aa bb cc dd aaa') == True
    
    assert countValidPassPhrases(['aa bb cc dd ee', 'aa bb cc dd aa', 'aa bb cc dd aaa']) == 2
    
    inputData = open('../data/input4.txt','r')
    data = inputData.readlines()
    
    assert countValidPassPhrases(data) == 325
    
    
def test_isAnagram():
    assert isAnagram('abcde', 'ecdab') == True
    assert isAnagram('abcde', 'ecddb') == False
    
def test_hasAnagram():
    assert hasAnagram('abcde fghij') == False
    assert hasAnagram('abcde xyz ecdab') == True
    assert hasAnagram('a ab abc abd abf abj') == False
    assert hasAnagram('oiii ioii iioi iiio') == True
    
def test_countValidWithoutAnagrams():
    inputData = open('../data/input4.txt','r')
    data = inputData.readlines()
    
    assert countValidWithoutAnagrams(data) == 119