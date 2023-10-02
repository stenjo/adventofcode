
def countSteps(codes):
    pointer = 0
    steps = 0
        
    while pointer < len(codes) and pointer >= 0:
        next = codes[pointer]
        codes[pointer] += 1
        pointer += next
        steps += 1
        
    return steps

def countSteps_decrease(codes):
    pointer = 0
    steps = 0
        
    while pointer < len(codes) and pointer >= 0:
        next = codes[pointer]
        if codes[pointer] >= 3:
            codes[pointer] -= 1
        else:
            codes[pointer] += 1
            
        pointer += next
        steps += 1
        
    return steps