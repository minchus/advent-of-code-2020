import re

def parse(text):
    bag_dict = {}
    for line in text.splitlines():
        bag_type = line.split("bags contain")[0].strip()
        bag_contents = line.split("bags contain")[1].strip()

        inner_dict = {}
        for bag in bag_contents.split(","):
            ret = re.match(r"(\d+) (.+) bag", bag.strip())
            if ret:
                inner_bag = ret.group(2)
                count = int(ret.group(1))
                inner_dict[inner_bag] = count
        bag_dict[bag_type] = inner_dict
    # print(bag_dict)
    return bag_dict


def contains_shiny_gold(bag_type, bag_dict):
    if bag_type == "shiny gold":
        return True

    bag_contents = bag_dict[bag_type]
    if len(bag_contents) > 0:
        for bag, count in bag_contents.items():
            if contains_shiny_gold(bag, bag_dict):
                return True
    return False


def count_bags_within(bag_type, bag_dict):
    bag_contents = bag_dict[bag_type]
    num_bags_inside = 0
    if len(bag_contents) > 0:
        for bag, count in bag_contents.items():
            num_bags_inside += count + count * count_bags_within(bag, bag_dict)
        return num_bags_inside
    return 0



with open("test.txt") as f:
    input_text = f.read()
bag_dict = parse(input_text)
assert contains_shiny_gold("bright white", bag_dict) == True
assert contains_shiny_gold("muted yellow", bag_dict) == True
assert contains_shiny_gold("dark orange", bag_dict) == True
assert contains_shiny_gold("light red", bag_dict) == True
assert contains_shiny_gold("dark olive", bag_dict) == False
assert contains_shiny_gold("vibrant plum", bag_dict) == False
assert contains_shiny_gold("faded blue", bag_dict) == False
assert count_bags_within("shiny gold", bag_dict) == 32
    

with open("input.txt") as f:
    input_text = f.read()
bag_dict = parse(input_text)

counter = 0
for bag in bag_dict.keys():
    if bag == "shiny gold":
        continue
    elif contains_shiny_gold(bag, bag_dict):
        counter += 1
print(counter)

print(count_bags_within("shiny gold", bag_dict))
