# Quick Union method Time Complexity expensive for larger data sets o(n)
# reference video - https://www.coursera.org/learn/algorithms-part1/lecture/ZgecU/quick-union#


class QuickUnion:
    def __init__(self, N: int):
        self.id: list[int] = []
        for i in range(0, N):
            self.id.append(i)

    def __root(self, i: int) -> int:
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p: int, q: int) -> bool:
        return self.__root(p) == self.__root(q)

    def union(self, p: int, q: int) -> None:
        i = self.__root(p)
        j = self.__root(q)
        self.id[i] = j


# qu = QuickUnion(10)
# qu.union(2, 1)
# print(qu.connected(2, 1))
# print(qu.id)

# Improvement of quick union 1 keep track of weighted of tree and always the smaller tree will go bottom
# reference video - https://www.coursera.org/learn/algorithms-part1/lecture/RZW72/quick-union-improvements


class QuickUnionWeighted:
    def __init__(self, N: int):
        self.id: list[int] = []
        self.sz: list[int] = []

        for i in range(N):
            self.id.append(i)
            self.sz.append(1)

    def __root(self, i: int) -> int:
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p: int, q: int) -> bool:
        return self.__root(p) == self.__root(q)

    def union(self, p: int, q: int) -> None:
        i = self.__root(p)
        j = self.__root(q)

        if i == j:
            return

        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]


# qu = QuickUnionWeighted(10)
# qu.union(2, 1)
# print(qu.connected(2, 1))
# print(qu.id)

# Improvement of quick union 2 kpath compression flatten the tree
# reference video - https://www.coursera.org/learn/algorithms-part1/lecture/RZW72/quick-union-improvements


class QuickUnionPathCompression:
    def __init__(self, N: int):
        self.id: list[int] = []
        self.sz: list[int] = []
        self.largest: list[int] = []

        for i in range(N):
            self.id.append(i)
            self.sz.append(1)
            self.largest.append(i)

    def __root(self, i: int) -> int:
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def connected(self, p: int, q: int) -> bool:
        return self.__root(p) == self.__root(q)

    def union(self, p: int, q: int) -> None:
        i = self.__root(p)
        j = self.__root(q)

        if i == j:
            return

        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
            self.largest[j] = max(self.largest[i], self.largest[j])
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
            self.largest[i] = max(self.largest[j], self.largest[i])

    def find(self, i: int):
        return self.largest[self.__root(i)]


qu = QuickUnionPathCompression(10)
qu.union(2, 1)
print(qu.connected(2, 1))
print(qu.id)
