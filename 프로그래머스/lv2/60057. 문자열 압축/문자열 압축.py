def solution(s):
    slen = len(s)
    minlen = slen
    
    for slice_ in range(1, slen // 2 + 1):
        patternCounts = []
        last_pattern = ""
        for j in range(1, slen // slice_ + 1):
            pattern = s[slice_ * (j-1) : slice_ * j]
            if last_pattern == pattern:
                patternCounts[-1] += 1
            else:
                patternCounts.append(1)
            last_pattern = pattern

        curlen = slen
        patternCounts = [x for x in patternCounts if x > 1]
        for count in patternCounts:
            curlen -= slice_ * (count - 1)
            curlen += len(str(count))
        if curlen < minlen:
            minlen = curlen
        
    return minlen