
number_list = []
with open("input.txt") as f:
    for line in f.readlines():
        number_list.append(int(line.strip()))


import itertools
for a, b in itertools.combinations(number_list, 2):
    if a + b == 2020:
        print(f"Result1: {a}*{b}={a * b}")

for a, b, c in itertools.combinations(number_list, 3):
    if a + b +c == 2020:
        print(f"Result2: {a}*{b}*{c}={a * b * c}")










