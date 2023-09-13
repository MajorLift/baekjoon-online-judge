def solution(land):
    prev = [max(land[0][:j] + land[0][j+1:]) for j in range(4)]
    for row in land[1:]:
        curr = [0] * 4
        for j in range(4):
            curr[j] = row[j] + prev[j]
        prev = [max(curr[:k] + curr[k+1:]) for k in range(4)]
    return max(curr)