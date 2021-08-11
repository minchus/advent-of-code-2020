
def parse(input_str):
    row_pos = [x for x in range(0,128)]
    for c in input_str:
        # print(row_pos)
        # print(len(row_pos))
        if c == "F":
            row_pos = row_pos[0:int(len(row_pos)/2)]
        elif c == "B":
            row_pos = row_pos[int(len(row_pos)/2):]

    col_pos = [x for x in range(0,8)]
    for c in input_str:
        if c == "L":
            col_pos = col_pos[0:int(len(col_pos)/2)]
        elif c == "R":
            col_pos = col_pos[int(len(col_pos)/2):]

    assert len(row_pos) == 1
    assert len(col_pos) == 1
    row_pos = row_pos[0]
    col_pos = col_pos[0]
    return row_pos, col_pos, row_pos * 8 + col_pos

assert parse("FBFBBFFRLR") == (44, 5, 357)
assert parse("BFFFBBFRRR") == (70, 7, 567)
assert parse("FFFBBBFRRR") == (14, 7, 119)
assert parse("BBFFBBFRLL") == (102, 4, 820)



positions = []
with open("input.txt") as f:
    for line in f.readlines():
        positions.append(parse(line.strip()))

seat_numbers = [x[2] for x in positions]
min_seat = min(seat_numbers)
max_seat = max(seat_numbers)
print(min_seat)
print(max_seat)

for x in range(min_seat, max_seat+1):
    if x not in seat_numbers:
        print(f"{x} missing")

