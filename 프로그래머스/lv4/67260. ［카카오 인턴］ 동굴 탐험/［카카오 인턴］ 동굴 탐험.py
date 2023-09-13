from collections import deque

def solution(n, path, order):
    adj = [[] for _ in range(n)]
    for u, v in path:
        adj[u].append(v)
        adj[v].append(u)
    nxt, prev = {}, {}    
    for u, v in order:
        nxt[u] = v
        prev[v] = u
        if v == 0:
            return False
        if u == 0:
            nxt[u] = None

    NO, YES, WAIT = range(3)
    visited = [YES] + [NO] * (n - 1)
    queue = deque([0])
    while queue:
        curr = queue.popleft()
        if curr == nxt.get(prev.get(curr)):
            visited[curr] = WAIT
            continue
        for node in adj[curr]:
            if visited[node] != NO:
                continue
            queue.append(node)
            visited[node] = YES
            if node in nxt:
                if visited[nxt[node]] == WAIT:
                    queue.append(nxt[node])
                    visited[nxt[node]] = YES
                nxt[node] = None

    return all(visited)
