import re
from heapq import heappush, heappop


def main():
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


if __name__ == '__main__':
    main()
