from math import inf
from heapq import heappush, heappop
from functools import lru_cache

def solution(n, s, a, b, fares):
    adj = [[0] * (n + 1) for _ in range(n + 1)]
    for u, v, w in fares:
        adj[u][v] = adj[v][u] = w
    
    @lru_cache
    def dijkstra(src, dst):
        dist = [+inf] * (n + 1)
        dist[src] = 0
        pq = [(dist[src], src)]
        while pq:
            dist_u, u = heappop(pq)
            if u == dst:
                return dist[u]
            for v, w in enumerate(adj[u]):
                if w > 0 and dist_u + w < dist[v]:
                    dist[v] = dist_u + w
                    heappush(pq, (dist[v], v))
        return +inf
        
    return min(dijkstra(s, v) + dijkstra(v, a) + dijkstra(v, b) 
                for v in range(1, n + 1))
    