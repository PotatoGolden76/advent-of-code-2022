priority = {}

for i in range(ord('z') - ord('a') + 1):
    priority[chr(ord('a')+i)] = 1 + i
    priority[chr(ord('A')+i)] = 27 + i

def p1():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        s = 0
        for pack in lines:
            h1 = pack[:len(pack)//2]
            h2 = pack[len(pack)//2:]
            for c in h1:
                if c in h2:
                    s += priority[c]
                    break
        print(s)
            
def p2():   
    with open("input.txt", "r") as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]
        s = 0
        lines = [lines[i:i+3] for i in range(0, len(lines), 3)]
        for group in lines:
            for c in group[0]:
                if c in group[1] and c in group[2]:
                    s += priority[c]
                    break
        print(s)

if __name__ == "__main__":
    p1()
    p2()