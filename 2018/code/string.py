# Testing string handling in Python

initial = '#..#.#..##......###...###...........'
initial = '##.#..#.#..#.####.#########.#...#.#.#......##.#.#...##.....#...#...#.##.#...##...#.####.##..#.#..#.'
patternstrings = [  '...## => #',
                    '..#.. => #',
                    '.#... => #',
                    '.#.#. => #',
                    '.#.## => #',
                    '.##.. => #',
                    '.#### => #',
                    '#.#.# => #',
                    '#.### => #',
                    '##.#. => #',
                    '##.## => #',
                    '###.. => #',
                    '###.# => #',
                    '####. => #']

patternstrings = [  '.#.#. => #',
                    '.#... => #',
                    '##### => #',
                    '#..#. => #',
                    '#...# => #',
                    '###.# => #',
                    '...## => #',
                    '#.##. => #',
                    '.#.## => #',
                    '##.#. => #',
                    # '...#. => .',
                    '..### => #',
                    '###.. => #',
                    # '##... => .',
                    # '..##. => .',
                    # '.##.# => .',
                    # '##.## => .',
                    # '.##.. => .',
                    '##..# => #',
                    # '#.#.# => .',
                    '#..## => #']

patterns = [ p.split(' => ')[0] for p in patternstrings]
print(patterns)
offset = 5
generationstring = '.'*offset+initial+'............'
count = initial.count('#')
print('{0:2d}: {1:s}'.format(0,generationstring))
for n in range(1,21):
    nextGenString ="."*len(initial)
    length = len(initial)
    potsum = 0
    first = length
    maxi = 0
    for i in range(-offset,length+offset+10):
        # print(generationstring[i-2:i+3], generationstring[i-2:i+3] in patterns)
        if i > 1-offset and i < length + 3 + offset:
            pattern = generationstring[i-2+offset:i+3+offset]
            if pattern in patterns:
                nextGenString = nextGenString[:i+offset]+'#'+nextGenString[i+1+offset:]
                count +=1
                potsum += i
                if first > i: first = i
                if maxi < i: maxi = i
            else:
                nextGenString = nextGenString[:i+offset]+'.'+nextGenString[i+1+offset:]


    nextGenString += '.' * (length - len(nextGenString))
    generationstring = nextGenString[:]
    print('{0:2d}: {1:s} - {2:2d} pots, sum {3:3d}, first: {4:2d}, index:{5:d}'.format(n,generationstring, generationstring.count('#'), potsum, first, maxi))
print(count)
