from itertools import product

def calc(pr, v):
    for c in pr:
        if c == "1":
            v += 2
        elif c == "2":
            v *= 3
    return v

def konetz(b, e, l):
    for t in range(1, l + 1):
        space = ["12"] * l
        for j in product(*space):
            proga = "".join(j)
            result = calc(proga, b)
            if result == e:
                return proga
    return None

if __name__ == '__main__':
    pr = konetz(1, 31, 5)
    if pr != None:
        print(pr)


