from collections import defaultdict
from math import inf
from functools import lru_cache

def solution(sales, links):
    sales = [0] + sales
    adj = defaultdict(list)
    for u, v in links:
        adj[u].append(v)

    @lru_cache
    def dfs(node):
        if node not in adj:
            return (sales[node], 0)
        cnt = leave_cnt = 0
        min_val, min_diff = 0, +inf
        for child in adj[node]:
            take, leave = dfs(child)
            min_val += min(take, leave)
            cnt += 1
            if leave < take:
                leave_cnt += 1
                min_diff = min(min_diff, take - leave)

        return (
            sales[node] + min_val, 
            min_val + (min_diff if cnt == leave_cnt else 0)
        )

    return min(dfs(1))
