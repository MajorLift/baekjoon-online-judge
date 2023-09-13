from sys import setrecursionlimit
setrecursionlimit(10**4)

class UnionFind:
    def __init__(self):
        self.root = dict()
    
    def find(self, x):
        if x not in self.root:
            self.root[x] = x + 1
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

def solution(k, room_number):
    return tuple(map(UnionFind().find, room_number))
