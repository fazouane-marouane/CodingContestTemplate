import sys
from collections import namedtuple
from itertools import (
    accumulate,
    chain
)

input = [ line.rstrip('\n').split(' ') for line in sys.stdin ]

N = int(input[0][0])

heights = list(map(lambda x: int(x[0]), input[1: N+1]))

def visibleTowersCount(tab):
    maxs = chain([0], accumulate(tab, lambda acc, curr: acc if acc == curr else max(acc, curr)))
    tab_acc = zip(tab, maxs)
    return len([v for v, m in tab_acc if v > m])

result =[]
for k in range(0, N):
    left = list(reversed(heights[0:k]))
    right = heights[k+1:N]
    left_result = visibleTowersCount(left)
    right_result = visibleTowersCount(right)
    result.append(str( left_result + right_result ))

print(' '.join(result), end='')
