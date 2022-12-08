from collections import Counter

line = ""
with open("input.txt", "r") as f:
    line = f.readline().strip()



def p1():
    for i in range(len(line)-3):
        # print(line[i:i+4])
        if len(Counter(line[i:i+4])) == len(line[i:i+4]):
            print(i+4)
            break
def p2():
    for i in range(len(line)-13):
        # print(line[i:i+4])
        if len(Counter(line[i:i+14])) == len(line[i:i+14]):
            print(i+14)
            break
    
if __name__ == "__main__":
    p1() 
    p2() 
