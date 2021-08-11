



def parse(file_path):
    with open(file_path) as f:
        input_text = f.read()

    instructions = []
    for line in input_text.splitlines():
        op, arg = line.split(" ")
        instructions.append([op, int(arg)])
    return instructions


def process(instruction_list):
    num_instructions = len(instruction_list)
    visited = set()
    position = 0
    acc = 0
    while position not in visited and position < num_instructions:
        visited.add(position)
        op, arg = instruction_list[position]
        # print(f"{op} {arg}")

        if op == "nop":
            position += 1
        elif op == "acc":
            acc += arg
            position += 1
        elif op == "jmp":
            position += arg
    return position == num_instructions, acc
    

assert process(parse("test.txt")) == (False, 5)
input_instructions = parse("input.txt")
print(process(input_instructions))


for i in range(0, len(input_instructions)):
    ins = [x[:] for x in input_instructions]
    if ins[i][0] == "nop":
        ins[i][0] = "jmp"
    elif ins[i][0] == "jmp":
        ins[i][0] = "nop"

    ret, a = process(ins)
    if ret:
        print(f"{i}, {ret}, {a}")
        

