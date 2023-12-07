from Day05.Almanac import Almanac

testInput = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


def test_Almanac():
    assert Almanac("").lowestLocation() == 0
    assert Almanac("seeds: 79 14 55 13").seeds == [79, 14, 55, 13]

    assert Almanac(testInput).seeds == [79, 14, 55, 13]
    assert len(Almanac(testInput).maps) == 7
    assert len(Almanac(testInput).sourceMap) == 7
    assert Almanac(testInput).sourceMap[("temperature", "humidity")].getMapped(50) == 51

    assert Almanac(testInput).getMap("seed", 79, "soil") == 81
    assert Almanac(testInput).getMap("seed", 14, "soil") == 14
    assert Almanac(testInput).getMap("seed", 55, "soil") == 57
    assert Almanac(testInput).getMap("seed", 13, "soil") == 13

    assert Almanac(testInput).getChainedMap("seed", 13, "soil") == 13
    assert Almanac(testInput).getChainedMap("seed", 13, "location") == 35
    assert Almanac(testInput).getChainedMap("seed", 55, "location") == 86
    assert Almanac(testInput).getChainedMap("seed", 79, "location") == 82

    assert Almanac(testInput).lowestLocation() == 35

    testData = open("../data/testInput05.txt", "r").read()
    assert Almanac(testData).lowestLocation() == 35

    inputData = open("../data/input05.txt", "r").read()
    assert Almanac(inputData).lowestLocation() == 621354867

def test_part2():
    
    assert Almanac("seeds: 79 14 55 13").seedRange == [(79, 14), (55, 13)]
    testData = open("../data/testInput05.txt", "r").read()
    # assert Almanac(testData).lowestSeedRangeLocation() == 46
  
    # assert Almanac(testData).lowestLocation() == 35
    
    assert Almanac(testInput).reverseMap("seed", 81, "soil") == 79
    assert Almanac(testInput).reverseMap("seed", 14, "soil") == 14
    assert Almanac(testInput).reverseMap("seed", 57, "soil") == 55
    
    assert Almanac(testInput).getChainedSource("seed", 13, "soil") == 13
    assert Almanac(testInput).getChainedSource("seed", 57, "soil") == 55
    assert Almanac(testInput).getChainedSource("seed", 35, "location") == 13
    assert Almanac(testInput).getChainedSource("seed", 86, "location") == 55
    assert Almanac(testInput).getChainedSource("seed", 82, "location") == 79
    
    # assert Almanac(inputData).lowestSeedRangeLocation() == 46
