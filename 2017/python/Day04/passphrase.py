
def passphrase(phrase):
    parts = phrase.split(' ')
    for i in range(len(parts)):
        if parts[i] in parts[i+1:]:
            return False
    
    return True

def countValidPassPhrases(phrases):
    count = 0
    for phrase in phrases:
        if passphrase(phrase.strip()):
            count += 1
            
    return count