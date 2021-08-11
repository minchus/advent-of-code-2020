import re

valid_count_1 = 0
valid_count_2 = 0
with open("input.txt") as f:
    for line in f.readlines():
        r = re.match(r'(\d+)-(\d+)\s(.):\s(.+)', line.strip())
        num1 = int(r.group(1))
        num2 = int(r.group(2))
        letter = r.group(3)
        password = r.group(4)

        count = password.count(letter)
        if count >= num1 and count <= num2:
            valid_count_1 += 1


        matches = 0
        if num1 <= len(password) and password[num1 - 1] == letter:
            matches += 1

        if num2 <= len(password) and password[num2 - 1] == letter:
            matches += 1

        if matches == 1:
            valid_count_2 += 1

print(f"valid_count_1={valid_count_1}")
print(f"valid_count_2={valid_count_2}")

