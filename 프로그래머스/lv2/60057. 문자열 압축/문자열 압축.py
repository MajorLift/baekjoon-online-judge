def solution(s):
    s_len = len(s)
    min_len = s_len
    
    for slice_ in range(1, s_len // 2 + 1):
        pattern_cnt, last_pattern = [], ''
        for j in range(1, s_len // slice_ + 1):
            pattern = s[slice_ * (j-1) : slice_ * j]
            if last_pattern == pattern:
                pattern_cnt[-1] += 1
            else:
                pattern_cnt.append(1)
            last_pattern = pattern

        curr_len = s_len
        for cnt in [x for x in pattern_cnt if x > 1]:
            curr_len -= slice_ * (cnt - 1)
            curr_len += len(str(cnt))
        
        min_len = min(min_len, curr_len)
        
    return min_len