# Quick find method Time Complexity o(n*2)
# reference video - https://www.coursera.org/learn/algorithms-part1/lecture/EcF3P/quick-find


class QuickFind:
    def __init__(self, N: int):
        self.id: list[int] = []
        for i in range(0, N):
            self.id.append(i)

    def connected(self, p: int, q: int) -> bool:
        return self.id[p] == self.id[q]

    def union(self, p: int, q: int) -> None:
        pId = self.id[p]
        qId = self.id[q]

        for i in range(0, len(self.id)):
            if self.id[i] == pId:
                self.id[i] = qId


uf = QuickFind(10)
uf.union(2, 4)
print(uf.id)
print(uf.connected(2, 4))
