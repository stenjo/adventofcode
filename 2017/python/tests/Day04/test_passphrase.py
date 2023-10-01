
from Day04.passphrase import passphrase,countValidPassPhrases

def test_passphrase():
    
    assert passphrase('aa bb cc dd ee') == True
    assert passphrase('aa bb cc dd aa') == False
    assert passphrase('aa bb cc dd aaa') == True
    
    assert countValidPassPhrases(['aa bb cc dd ee', 'aa bb cc dd aa', 'aa bb cc dd aaa']) == 2
    
    inputData = open('../data/input4.txt','r')
    data = inputData.readlines()
    
    assert countValidPassPhrases(data) == 325
    
    