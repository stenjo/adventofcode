from Day10.Tile import Tile


def test_Tile():
    assert Tile(1, 2, "|").pipe == "|"
