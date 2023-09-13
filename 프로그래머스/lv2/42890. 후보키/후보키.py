from itertools import combinations

def solution(relation):
    n, m = map(len, (relation, relation[0]))
    
    candidates = set()
    for j in range(1, m + 1):
        for keys in combinations(range(m), j):
            records = set([tuple(relation[i][key] 
                                 for key in keys) 
                           for i in range(n)])
            
            if len(records) == n \
                and not any(set(candidate) < set(keys) 
                            for candidate in candidates):
                candidates.add(keys)
    
    return len(candidates)
            
