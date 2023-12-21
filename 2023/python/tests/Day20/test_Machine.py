from Day20.Machine import Machine


m1 = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

m2 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""


def test_Machine():
    assert Machine(m1).modules["a"].type == "%"
    assert Machine(m1).modules["broadcaster"].subscribers == ["a", "b", "c"]
    assert Machine(m1).modules["inv"].subscribers == ["a"]
    assert Machine(m1).modules["inv"].type == "&"

    assert Machine(m1).signal(False) == (4, 8)
    assert Machine(m1).sumHighsAndLows(1000) == 32000000
    assert Machine(m2).sumHighsAndLows(1000) == 11687500

    inputData = open("../data/input20.txt", "r").read()
    assert Machine(inputData).sumHighsAndLows(1000) == 883726240

    assert Machine(inputData).minButtonPresses("rx") == 883726240
    # Brute force takes a long time
    # need to see sequences bb sources and get lcm
