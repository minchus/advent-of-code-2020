from collections import defaultdict



def get_pos_tuple(line):
    col = 0
    row = 0
    it = iter(range(0, len(line)))
    for i in it:

        if line[i] == 'e':
            col += 2
        elif line[i] == 'w':
            col -= 2
        elif line[i] == 'n' and line[i+1] == 'e':
            col += 1
            row += 1
            _ = next(it)
        elif line[i] == 'n' and line[i+1] == 'w':
            col -= 1
            row += 1
            _ = next(it)
        elif line[i] == 's' and line[i+1] == 'e':
            col += 1
            row -= 1
            _ = next(it)
        elif line[i] == 's' and line[i+1] == 'w':
            col -= 1
            row -= 1
            _ = next(it)
    return col, row


def get_adjacent(pos):
    return [(pos[0]+1, pos[1]+1),
            (pos[0]-1, pos[1]+1),
            (pos[0]+2, pos[1]),
            (pos[0]-2, pos[1]),
            (pos[0]+1, pos[1]-1),
            (pos[0]-1, pos[1]-1)]


def get_all_tiles(tile_list):
    ret = []
    for pos in tile_list:
        ret.extend(get_adjacent(pos))
        ret.append(pos)
    return ret


moves = defaultdict(int)
with open("input.txt") as f:
#with open("test.txt") as f:
    for line in f.readlines():
        line = line.strip()
        position = get_pos_tuple(line)
        moves[position] += 1
            
black_tiles = set()
for k, v in moves.items():
    if v % 2 != 0:
        black_tiles.add(k)
print(f"black_count = {len(black_tiles)}")

num_days = 100
for _ in range(0,num_days):
    all_tiles = get_all_tiles(black_tiles)
    flip_to_white = set()
    flip_to_black = set()
    for tile in all_tiles:
        if tile in black_tiles:
            black_count = 0
            for adjacent_tile in get_adjacent(tile):
                if adjacent_tile in black_tiles:
                    black_count += 1
            if black_count == 0 or black_count > 2:
                flip_to_white.add(tile)

        else:
            black_count = 0
            for adjacent_tile in get_adjacent(tile):
                if adjacent_tile in black_tiles:
                    black_count += 1
            if black_count == 2:
                flip_to_black.add(tile)

    black_tiles = flip_to_black.union(black_tiles - flip_to_white)

print(f"black_count after {num_days} days = {len(black_tiles)}")
        

