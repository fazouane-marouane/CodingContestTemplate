import sys
from collections import namedtuple
import itertools

input = [ line.rstrip('\n').split(' ') for line in sys.stdin ]

Position = namedtuple('Position', ['lat', 'lng'], verbose=False)

from_lat, from_lng, to_lat, to_lng = map(float, input[0])
N = int(input[1][0])
my_map = map(Position._make, [ map(float, line) for line in input[2:]])
is_in_control_zone = lambda p: (
    p.lat < to_lat and
    p.lat > from_lat and
    p.lng < to_lng and
    p.lng > from_lng)
people_in_control_zone = [p for p in my_map if is_in_control_zone(p) ]

print(len(people_in_control_zone), end="")
