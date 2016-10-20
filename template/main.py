import sys
from collections import namedtuple
import itertools

input = [ line.rstrip('\n').split(' ') for line in sys.stdin ]

N = int(input[0][0])

result = N+1

print(result)
