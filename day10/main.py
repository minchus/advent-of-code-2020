from collections import Counter


def parse(file_path):
    with open(file_path) as f:
        return [int(x) for x in f.read().splitlines()]

def process(input_list):
    s = sorted(input_list)
    s = [0] + s + [s[-1] + 3]
    counter = Counter(s[i+1] - n for i, n in enumerate(s[:-1]))
    return counter


def process2(input_list):
    s = sorted(input_list)
    s = [0] + s + [s[-1] + 3]
    dag = dict([(x, {y for y in range(x+1, x+4) if y in s}) for x in s])

    M = {}
    def dfc(D, v):
        if v in M:
            return M[v]
        elif D[v]:
            M[v] = sum(dfc(D, x) for x in D[v])
            return M[v]
        else:
            return 1
    return dfc(dag,0)

test1 = process(parse("test1.txt"))
assert test1[1] == 7
assert test1[3] == 5

test2 = process(parse("test2.txt"))
assert test2[1] == 22
assert test2[3] == 10

part1 = process(parse("input.txt"))
print(part1)
print(part1[1]*part1[3])

assert process2(parse("test1.txt")) == 8
assert process2(parse("test2.txt")) == 19208
print(process2(parse("input.txt")))
