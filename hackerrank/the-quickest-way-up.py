#!/bin/python3

# snakes and ladders DP solution

inin = lambda: [ map(int, input().split()) for _ in range(int(input())) ]

def shortest():
    cost = [0] + [999] * 99
    jumps = { s - 1: e - 1 for s, e in inin() + inin () }
    i = 1
    while i < 100:
        p = [ cost[j] for j in range(max(0, i-6), i)
              if cost[j] != None and j not in jumps ]
        if not p: # unreachable
            cost[i] = None
            i += 1
            continue
        cost[i] = min(min(p) + 1, cost[i])
        if i in jumps:
            j = jumps[i]
            if cost[i] < cost[j]:
                cost[j] = cost[i]
                i = min(i+1, j)
                continue
        i += 1
    return cost[99] if cost[99] else -1

for _ in range(int(input())):
    print(shortest())
