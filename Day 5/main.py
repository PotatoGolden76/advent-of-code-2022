
stacks = []
instructions = []
stack_nr = 0

def read_state():
    with open("input.txt", "r") as f:
        buffer = []
        line = f.readline()
        while line != "\n":
            buffer.append(line[:-1])
            line = f.readline()
        
        stack_nr = int(buffer[-1][-2])
        for _ in range(stack_nr):
            stacks.append([])

        for i in range(len(buffer[-1])):
            if buffer[-1][i].isdigit():
                for j in range(len(buffer)-2, -1, -1):
                    if i <= len(buffer[j]):
                        if buffer[j][i] != " ":
                            stacks[int(buffer[-1][i])-1].append(buffer[j][i])

        for i in f.readlines():
            t = i.strip().split(" ")
            instructions.append([int(t[1]), int(t[3])-1, int(t[5])-1])

def p1():
    for ins in instructions:
        for _ in range(ins[0]):
            stacks[ins[2]].append(stacks[ins[1]].pop())
    out = ""
    for s in stacks:
        out += s[-1]
    print(out)

def p2():
    for ins in instructions:
        buffer = []
        for _ in range(ins[0]):
            buffer.append(stacks[ins[1]].pop())
        stacks[ins[2]].extend(reversed(buffer))
    out = ""
    for s in stacks:
        out += s[-1]
    print(out)


if __name__ == "__main__":
    read_state()
    # p1()
    p2()
