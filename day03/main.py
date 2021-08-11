

def parse_input(input_text, move_right, move_down):
    tree_count = 0
    for line_number, line in enumerate(input_text.splitlines()):

        if line_number % move_down > 0:
            continue

        pos = (int(line_number / move_down) * move_right) % len(line)
        line_array = list(line)
        line_array[pos] = "o"
        print(str(pos) + ": " + "".join(line_array))
        if line[pos] == "#":
            tree_count += 1
    return tree_count


with open("test.txt") as f:
    test_text = f.read()
assert parse_input(test_text, 1, 1) == 2
assert parse_input(test_text, 3, 1) == 7
assert parse_input(test_text, 5, 1) == 3
assert parse_input(test_text, 7, 1) == 4
assert parse_input(test_text, 1, 2) == 2

with open("input.txt") as f:
    input_text = f.read()
part_1_count = parse_input(input_text, 3, 1)
print(f"part 1: {part_1_count}")

part_2_count = (
        parse_input(input_text, 1, 1) *
        parse_input(input_text, 3, 1) *
        parse_input(input_text, 5, 1) *
        parse_input(input_text, 7, 1) *
        parse_input(input_text, 1, 2)
)
print(f"part 2: {part_2_count}")

