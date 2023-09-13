def solution(n, m, x, y, queries):
    DIRECTIONS = (-1, 1, -1, 1)
    LIMITS = (m, m, n, n)
    BOUNDS = (0, m, 0, n)
    corners = [y, y + 1, x, x + 1]

    for command, dx in reversed(queries):
        reverse = command ^ 1
        corners[reverse] += DIRECTIONS[reverse] * dx
        corners[reverse] = min(max(corners[reverse], 0), LIMITS[reverse])

        if corners[command] != BOUNDS[command]:
            corners[command] += DIRECTIONS[reverse] * dx
            corners[command] = min(max(corners[command], 0), LIMITS[command])

        if any(corners[i] == BOUNDS[i ^ 1] for i in range(4)):
            return 0

    return (corners[1] - corners[0]) * (corners[3] - corners[2])