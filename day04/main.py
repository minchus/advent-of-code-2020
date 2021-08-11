import re

def year_valid(input_str, min_year, max_year):
    try:
        input_int = int(input_str)
        if input_int >= min_year and input_int <= max_year:
            return True
        return False
    except:
        return False
assert year_valid("2002", 1920, 2002) == True
assert year_valid("2003", 1920, 2002) == False
assert year_valid("abc", 1920, 2002) == False
assert year_valid("1", 1920, 2002) == False


def hgt_valid(input_str):
    try:
        unit = input_str[-2:]
        value = int(input_str[:-2])
        if unit == "cm":
            if value < 150 or value > 193:
                return False
        else:
            if value < 59 or value > 76:
                return False
        return True
    except:
        return False
assert hgt_valid("60in") == True
assert hgt_valid("190cm") == True
assert hgt_valid("190in") == False
assert hgt_valid("60") == False


def hcl_valid(input_str):
    if not re.match(r'#[0-9a-f]{6}', input_str):
        return False
    return True
assert hcl_valid("#123abc") == True
assert hcl_valid("#123abz") == False
assert hcl_valid("123abc") == False
        

def ecl_valid(input_str):
    if input_str in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        return True
    return False
assert ecl_valid("brn") == True
assert ecl_valid("wat") == False


def pid_valid(input_str):
    if not re.match(r'^[0-9]{9}$', input_str):
        return False
    return True
assert pid_valid("000000001") == True
assert pid_valid("0123456789") == False


def part1_is_valid(x):
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    return set(x.keys()).issuperset(required_fields)


def part2_is_valid(x):
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    if not set(x.keys()).issuperset(required_fields):
        return False

    if not year_valid(x["byr"], 1920, 2002):
        return False

    if not year_valid(x["iyr"], 2010, 2020):
        return False

    if not year_valid(x["eyr"], 2020, 2030):
        return False
    
    if not hgt_valid(x["hgt"]):
        return False

    if not hcl_valid(x["hcl"]):
        return False

    if not ecl_valid(x["ecl"]):
        return False

    if not pid_valid(x["pid"]):
        return False

    return True


def parse(input_text, valid_fn):
    count = 0
    lines = input_text.split("\n\n")
    for line in lines:
        doc = {}
        for pair in line.split():
            fields = pair.split(":")
            doc[fields[0]] = fields[1]

        if valid_fn(doc):
            count += 1

    return count

    

with open("test.txt") as f:
    test_count = parse(f.read(), part1_is_valid)
assert test_count == 2

with open("input.txt") as f:
    part1_count = parse(f.read(), part1_is_valid)
print(part1_count)

with open("input.txt") as f:
    part2_count = parse(f.read(), part2_is_valid)
print(part2_count)

