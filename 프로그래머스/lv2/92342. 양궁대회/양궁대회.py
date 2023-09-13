from itertools import product

def solution(n, info):
    info.reverse()
    global_max = 0
    output = [-1]
    for comb in product((True, False), repeat=11):
        peach = lion = 0
        remaining = n
        path = [0] * 11
        for i, take in enumerate(comb):
            if take:
                lion += i
                path[i] = info[i] + 1
                remaining -= path[i]
            elif info[i] > 0:
                peach += i
        if remaining < 0:
            continue
        if lion - peach > global_max:
            global_max = lion - peach
            path[0] = remaining
            output = path[:]
    output.reverse()
    return output