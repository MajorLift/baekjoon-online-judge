from heapq import heappop, heappush

def solution(n, m, x, y, r, c, k):
    def manhattan(i, j):
        return abs(r - i) + abs(c - j)
    DIRECTIONS = {(0, 1): 'r', (1, 0): 'd', (0, -1): 'l', (-1, 0): 'u'}
    
    pq = [('', manhattan(x, y), x, y)]
    while pq:
        path, _, ui, uj = heappop(pq)
        steps = len(path)
        if (ui, uj) == (r, c):
            if steps == k:
                return path
            if (k - steps) % 2:
                break
        if manhattan(ui, uj) > k - steps:
            continue
        for (vi, vj), move in ((map(sum, zip((ui, uj), move)), move) for move in DIRECTIONS.keys()):
            if not (1 <= vi <= n and 1 <= vj <= m): 
                continue
            estimation = steps + 1 + manhattan(vi, vj)
            if estimation > k:
                continue
            heappush(pq, (path + DIRECTIONS[move], estimation, vi, vj))
    
    return "impossible"
