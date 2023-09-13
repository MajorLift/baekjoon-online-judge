from itertools import product
from heapq import heappush, heappop
from math import inf

def solution(maps):
    DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
    m, n = map(len, (maps, maps[0]))
    START, LEVER, END, WALL = "S", "L", "E", "X"
    def find_targets():
        output = {}
        for i, j in product(range(m), range(n)):
            if maps[i][j] in (START, LEVER, END):
                output[maps[i][j]] = (i, j)
        return output
    targets = find_targets()
    
    def dijkstra(src, dst):
        dist = {(i, j): +inf for i, j in product(range(m), range(n))}
        dist[src] = 0
        pq = [(0, src)]
        while pq:
            dist_u, (r, c) = heappop(pq)
            if (r, c) == dst:
                return dist_u
            for i, j in (map(sum, zip(d, (r, c))) for d in DIRECTIONS):
                if not (0 <= i < m and 0 <= j < n) \
                    or maps[i][j] == WALL:
                    continue
                if dist_u + 1 < dist[(i, j)]:
                    dist[(i ,j)] = dist_u + 1
                    heappush(pq, (dist_u + 1, (i, j)))
        return -1
    
    start_to_lever = dijkstra(targets[START], targets[LEVER])
    lever_to_end = dijkstra(targets[LEVER], targets[END])
    if any(e == -1 for e in (start_to_lever, lever_to_end)):
        return -1
    return start_to_lever + lever_to_end