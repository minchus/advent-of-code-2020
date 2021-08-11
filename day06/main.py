
def parse_file(file_path):
    with open(file_path) as f:
        input_text = f.read()

        group_counts = []
        for line in (input_text.split("\n\n")):
            d = {c: line.count(c) for c in line if c not in "\n"}
            group_counts.append(d)

    return sum([len(x.keys()) for x in group_counts])


assert parse_file("test.txt") == 11
print(parse_file("input.txt"))
    

def parse_file2(file_path):
    with open(file_path) as f:
        input_text = f.read()

        total_common = 0
        for group in (input_text.split("\n\n")):
            list_of_sets = []
            for line in group.splitlines():
                d = {c: line.count(c) for c in line}
                list_of_sets.append(set(d.keys()))
            common = set.intersection(*list_of_sets)
            total_common += len(common)

    return total_common


assert parse_file2("test.txt") == 6
print(parse_file2("input.txt"))

