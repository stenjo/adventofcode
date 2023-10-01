# Advent of Code 2017: https://adventofcode.com/2017/day/1
# 
# 

def max_min_difference(row):
    r = row.split('\t')
    a = []
    sum = 0
    
    for j in range(len(r)):
        a.append(int(r[j].strip()))
    sum += max(a) - min(a)
    
    return sum

def spreadsheet_checksum(spreadsheet):
    sum = 0
    
    for i in range(len(spreadsheet)):
        sum += max_min_difference(spreadsheet[i])
        
    return sum

def evenly_divisible(spreadsheet):
    data = []
    for i in range(len(spreadsheet)):
        r = spreadsheet[i].split('\t')
        a = []
        for j in range(len(r)):
            a.append(int(r[j].strip()))
        data.append(sorted(a[:]))

    sum = 0
    for row in data:
        for i in range(len(row)):
            for j in range(len(row)):
                if (i != j) and (row[i]%row[j] == 0):
                    sum += int(row[i]/row[j])
                
    return sum