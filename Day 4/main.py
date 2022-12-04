def p1():
    count = 0
    with open("input.txt", "r") as f:
        pairs = f.readlines()
        pairs = [x.strip().split(",") for x in pairs]
        pairs = [[x[0].split("-"), x[1].split("-")] for x in pairs]

        for pair in pairs:
            if int(pair[0][0]) <= int(pair[1][0]) and int(pair[0][1]) >= int(pair[1][1]):
                count += 1
                continue
            if int(pair[0][0]) >= int(pair[1][0]) and int(pair[0][1]) <= int(pair[1][1]):
                count += 1
                continue
    print(count)


def p2():
    count = 0
    with open("input.txt", "r") as f:
        pairs = f.readlines()
        pairs = [x.strip().split(",") for x in pairs]
        pairs = [[x[0].split("-"), x[1].split("-")] for x in pairs]

        for pair in pairs:
            if (int(pair[0][0]) >= int(pair[1][0]) and int(pair[0][0]) <= int(pair[1][1])) or \
                (int(pair[0][1]) >= int(pair[1][0]) and int(pair[0][1]) <= int(pair[1][1])) or \
                (int(pair[1][0]) >= int(pair[0][0]) and int(pair[1][0]) <= int(pair[0][1])) or \
                (int(pair[1][1]) >= int(pair[0][0]) and int(pair[1][1]) <= int(pair[0][1])):
                count += 1
    print(count)


if __name__ == "__main__":
    p1()
    p2()
