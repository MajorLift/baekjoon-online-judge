from collections import defaultdict
from functools import reduce
from operator import mul

def solution(clothes):
    hashmap = defaultdict(list)
    for item, category in clothes:
        hashmap[category].append(item)
    return reduce(mul, [len(v) + 1 for v in hashmap.values()], 1) - 1