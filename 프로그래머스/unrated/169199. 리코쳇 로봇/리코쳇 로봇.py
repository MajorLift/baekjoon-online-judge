from itertools import product
from math import inf
from heapq import heappush, heappop

def solution(board):
    DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
    m, n = map(len, (board, board[0]))
    (SRCi, SRCj), (DSTi, DSTj) = (-1, -1), (-1, -1)
    for i, j in product(range(m), range(n)):
        if board[i][j] == 'R':
            SRCi, SRCj = i, j
        elif board[i][j] == 'G':
            DSTi, DSTj = i, j

    pq, dist = [(0, (SRCi, SRCj))], [[+inf] * n for _ in range(m)]
    dist[SRCi][SRCj] = 0
    while pq:
        steps_u, (ui, uj) = heappop(pq)
        for dx, dy in DIRS:
            vi, vj = ui, uj
            while True:
                if not (0 <= vi < m and 0 <= vj < n) \
                    or board[vi][vj] == 'D':
                    vi -= dx
                    vj -= dy
                    break
                vi += dx
                vj += dy
            if steps_u + 1 < dist[vi][vj]:
                dist[vi][vj] = steps_u + 1
                heappush(pq, (dist[vi][vj], (vi, vj)))
                
    return dist[DSTi][DSTj] if dist[DSTi][DSTj] < +inf else -1