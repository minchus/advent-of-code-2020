




def parse(file_path):
    with open(file_path) as f:
        lines = []
        input_text = f.read()
        for line in input_text.splitlines():
            lines.append(list(line))
    return lines

def pretty_print(d):
    for line in d:
        print("".join(map(str, line)))
    print("\n")

def get_next(d):
    adj_count = get_counts(d)
    next_vals = []
    for row in range(0, len(d)):
        vals = []
        for col in range(0, len(d[0])):
            cur = d[row][col]
            if cur == ".":
                vals.append(".")
            elif cur == "L" and adj_count[row][col] == 0:
                vals.append("#")
            elif adj_count[row][col] >= 4:
                vals.append("L")
            else:
                vals.append(cur)
        next_vals.append(vals)
    return next_vals

def get_counts(d):
    return [[count_adjacent(d, row, col) for col in range(len(d[0]))] for row in range(len(d))]

def count_adjacent(d, row, col):
    count = 0
    row_count = len(d)
    col_count = len(d[0])
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            r = row + x
            c = col + y
            if r < 0 or c < 0 or r == row_count or c == col_count or (x == 0 and y == 0):
                continue
            if d[r][c] == "#":
                count += 1
    return count

def count_occupied(d):
    count = 0
    for row in range(0, len(d)):
        for col in range(0, len(d[0])):
            if d[row][col] == "#":
                count += 1
    return count

def part1(d):
    while True:
        d_count = count_occupied(d)
        n = get_next(d)
        n_count = count_occupied(n)
        if d_count == n_count:
            return d_count
        d=n


test_input = parse("test.txt")
assert part1(test_input) == 37

part1_input = parse("input.txt")
print(part1(part1_input))
