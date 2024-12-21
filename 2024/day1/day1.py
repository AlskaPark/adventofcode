def puzzle_1():
    import re
    from heapq import heappush, heappop

    l, r = [], []
    with open('input.txt') as f:
        for line in f:
            lnum, rnum = re.findall(r'(\d+)', line)
            heappush(l, int(lnum))
            heappush(r, int(rnum))

        acc = 0
        while l and r:
            acc += abs(heappop(l) - heappop(r))

    print(acc)


def puzzle_2():
    import re
    from collections import Counter

    c = Counter()
    l, r = [], []
    with open('input.txt') as f:
        for line in f:
            lnum, rnum = re.findall(r'(\d+)', line)
            l.append(int(lnum))
            c.update({int(rnum): 1})

    sim = 0
    for lnum in l:
        sim += lnum * c[lnum]

    print(sim)


if __name__ == '__main__':
    # puzzle_1()
    puzzle_2()
