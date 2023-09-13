from itertools import permutations
from bisect import bisect_right

def solution(n, weak, dist):
    dist.sort(reverse=True)
    for cnt in range(1, len(dist) + 1):
        for start in range(len(weak)):
            weak_rot = weak[start:] + [n + e for e in weak[:start]]
            for patrols in permutations(dist[:cnt]):
                pos = 0
                for reach in patrols:
                    pos = bisect_right(weak_rot, weak_rot[pos] + reach)
                if pos >= len(weak):
                    return cnt
    return -1
                    
                