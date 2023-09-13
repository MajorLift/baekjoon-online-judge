class Node:
    def __init__(self, up=None, down=None):
        self.deleted = False
        self.up, self.down = up, down

def solution(n, k, cmd):
    UP, DOWN, CUT, UNDO = "U", "D", "C", "Z"
    cmds = [e.split(" ") for e in cmd]
    
    state = [Node(i - 1, i + 1) for i in range(n)]
    state[0].up = state[-1].down = None
    history = []
    curr = k
    
    for cmd in cmds:
        if cmd[0] is UP:
            for _ in range(int(cmd[1])):
                curr = state[curr].up
        elif cmd[0] is DOWN:
            for _ in range(int(cmd[1])):
                curr = state[curr].down
        elif cmd[0] is CUT:
            history.append(curr)
            state[curr].deleted = True
            prev, nxt = state[curr].up, state[curr].down
            if prev is not None:
                state[prev].down = nxt
            if nxt:
                state[nxt].up = prev
                curr = nxt
            else:
                curr = prev
        elif cmd[0] is UNDO:
            last = history.pop()
            state[last].deleted = False
            prev, nxt = state[last].up, state[last].down
            if prev:
                state[prev].down = last
            if nxt:
                state[nxt].up = last
                
    return "".join("X" if e.deleted else "O" for e in state)