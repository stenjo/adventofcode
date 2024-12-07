import sys


def inbounds(map, r, c):
    return 0 <= c < len(map[0]) and 0 <= r < len(map)


def walk_path(map, d, pos):
    path = set()
    r, c = pos
    while True:
        path.add((r, c))
        map[r][c] = d
        dR, dC = moves[d]
        next_r, next_c = r + dR, c + dC
        if not inbounds(map, next_r, next_c):
            break
        while map[next_r][next_c] == "#":
            d = rotate[d]
            map[r][c] = d
            dR, dC = moves[d]
            next_r, next_c = r + dR, c + dC
        r, c = next_r, next_c
    return path


def check_loop(map, d, pos):
    obstacles = set()
    r, c = pos
    while True:
        dR, dC = moves[d]
        next_r, next_c = r + dR, c + dC
        if not inbounds(map, next_r, next_c):
            break
        while map[next_r][next_c] in ["#", "O"]:
            if ((d, r, c)) in obstacles:
                return True
            else:
                obstacles.add((d, r, c))
            d = rotate[d]
            dR, dC = moves[d]
            next_r, next_c = r + dR, c + dC
        r, c = next_r, next_c
    return False


data = open(sys.argv[1]).read().strip()
map = []
for i, row in enumerate(data.split("\n")):
    _row = list(row)
    map.append(_row)
    if ("^") in _row:
        start = (i, _row.index("^"))

rotate = {"^": ">", ">": "v", "v": "<", "<": "^"}
moves = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

path = walk_path(map, "^", start)
print(f"Part 1: {len(path)}")

p2 = 0
for r, c in path:
    new_map = [row[:] for row in map]
    new_map[r][c] = "O"
    if check_loop(new_map, "^", start):
        p2 += 1
print(f"Part 2: {p2}")