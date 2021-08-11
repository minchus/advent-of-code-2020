


def parse(file_path):
    with open(file_path) as f:
        input_text = f.read()
    num_list = []
    for line in input_text.splitlines():
        num_list.append(int(line))
    return num_list


def check_list(number_list, x):
    number_set = set(number_list)
    for n in number_set:
        if x - n in number_set:
            return True
    return False

def process(number_list, preamble_length):
    for pos in range(preamble_length, len(number_list)):
        prev_numbers = number_list[pos - preamble_length:pos]
        check = number_list[pos]
        # print(prev_numbers, check)
        if not check_list(prev_numbers, check):
            return check
    return -1

test_input = parse("test.txt")
assert process(test_input, 5) == 127

actual_input = parse("input.txt")
part1_result = process(actual_input, 25)
print(part1_result)


def part2(number_list, check):
    for x in range(0, len(number_list)):
        for y in range(x, len(number_list)):
            if sum(number_list[x:y]) == check:
                return min(number_list[x:y]) + max(number_list[x:y])

assert part2(test_input, 127) == 62
print(part2(actual_input, part1_result))
