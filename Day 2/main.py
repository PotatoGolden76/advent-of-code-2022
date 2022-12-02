score_map = {
    "X": 1,
    "Y": 2,
    "Z": 3
}
win_map = {
    "A": "Z",
    "B": "X",
    "C": "Y",
    "X": "C",
    "Y": "A",
    "Z": "B"
}

correspondence_map = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}


def p1():
    score = 0
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for round in lines:
            r = round.strip().split(" ")

            score += score_map[r[1]]
            if r[1] == correspondence_map[r[0]]:
                # print("Draw")
                score += 3
                continue
            if r[1] == win_map[r[0]]:
                # print("Loss")
                score += 0
                continue
            # print("Win")
            score += 6
    return score


def p2():
    score = 0
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for round in lines:
            r = round.strip().split(" ")

            match r[1]:
                case 'X':
                    # print("Loss")
                    score += score_map[win_map[r[0]]]
                case 'Y':
                    # print("Draw")
                    score += 3 + score_map[correspondence_map[r[0]]]
                case 'Z':
                    # print("Win")
                    score += 6 + score_map[[x for x in win_map if win_map[x] == r[0]][0]]
    return score


if __name__ == "__main__":
    print(p1())
    print(p2())
