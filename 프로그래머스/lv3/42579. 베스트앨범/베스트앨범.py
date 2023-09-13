from collections import defaultdict

def solution(genres, plays):
    hashmap = defaultdict(list)
    for i, (genre, count) in enumerate(zip(genres, plays)):
        hashmap[genre].append((i, count))
    
    genres_srt = sorted([v for v in hashmap.values()], 
                        key=lambda x: sum(e[1] for e in x), 
                        reverse=True)
    
    return [x[0] for arr in genres_srt 
            for x in sorted(arr, 
                            key=lambda e: (e[1], -e[0]), 
                            reverse=True)[:2]]