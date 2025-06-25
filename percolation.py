import random
import math

BLOCKED = "B"
OPEN = "O"


class UnionFind:
    def __init__(self, N):
        self.id = list(range(N))
        self.sz = [1] * N

    def __root(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]  # Path compression
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.__root(p) == self.__root(q)

    def union(self, p, q):
        i = self.__root(p)
        j = self.__root(q)

        if i == j:
            return

        # Weighted union
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]


class Percolation:
    def __init__(self, n: int):
        if n <= 0:
            raise ValueError("n must be greater than 0")

        self.n = n
        self.total_open_sites = 0
        self.grid = [[BLOCKED for _ in range(n)] for _ in range(n)]

        self.virtual_top = n * n
        self.virtual_bottom = n * n + 1

        self.uf = UnionFind(n * n + 2)

    def __to_index(self, row, col):
        return row * self.n + col

    def __validate(self, row, col):
        if row < 0 or row >= self.n or col < 0 or col >= self.n:
            raise ValueError("Index out of bounds")

    def open(self, row: int, col: int):
        self.__validate(row, col)

        if not self.is_open(row, col):
            self.grid[row][col] = OPEN
            self.total_open_sites += 1
            index = self.__to_index(row, col)

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < self.n and 0 <= new_col < self.n:
                    if self.is_open(new_row, new_col):
                        neighbor_index = self.__to_index(new_row, new_col)
                        self.uf.union(index, neighbor_index)

            if row == 0:
                self.uf.union(index, self.virtual_top)
            if row == self.n - 1:
                self.uf.union(index, self.virtual_bottom)

    def is_open(self, row: int, col: int) -> bool:
        self.__validate(row, col)
        return self.grid[row][col] == OPEN

    def is_full(self, row, col):
        self.__validate(row, col)
        return self.uf.connected(self.__to_index(row, col), self.virtual_top)

    def number_of_open_sites(self):
        return self.total_open_sites

    def percolates(self) -> bool:
        return self.uf.connected(self.virtual_top, self.virtual_bottom)

    def display(self):
        for i in range(self.n):
            row_str = ""
            for j in range(self.n):
                if self.grid[i][j] == BLOCKED:
                    row_str += "B "
                elif self.is_full(i, j):
                    row_str += "F "
                else:
                    row_str += "O "
            print(row_str)
        print()


class PercolationStats:
    def __init__(self, n, trials):
        if n <= 0 or trials <= 0:
            raise ValueError("n and trials must be > 0")
        self.n = n
        self.trials = trials
        self.thresholds = []

        for _ in range(trials):
            perc = Percolation(n)
            while not perc.percolates():
                row = random.randint(0, n - 1)
                col = random.randint(0, n - 1)
                if not perc.is_open(row, col):
                    perc.open(row, col)
            threshold = perc.number_of_open_sites() / (n * n)
            self.thresholds.append(threshold)

    def mean(self) -> float:
        return sum(self.thresholds) / self.trials

    def stddev(self) -> float:
        m = self.mean()
        return math.sqrt(sum((x - m) ** 2 for x in self.thresholds) / (self.trials - 1))

    def confidence_lo(self) -> float:
        return self.mean() - 1.96 * self.stddev() / math.sqrt(self.trials)

    def confidence_hi(self) -> float:
        return self.mean() + 1.96 * self.stddev() / math.sqrt(self.trials)


if __name__ == "__main__":
    p = Percolation(5)
    p.open(0, 2)
    p.open(1, 2)
    p.open(2, 2)
    p.open(3, 2)
    p.open(4, 2)

    p.display()
    print("Does it percolate?", p.percolates())
    print("Number of open sites:", p.number_of_open_sites())

    n = 200
    trials = 100
    stats = PercolationStats(n, trials)
    print("\nMonte Carlo Simulation Results:")
    print("mean =", stats.mean())
    print("stddev =", stats.stddev())
    print("95% confidence interval =", (stats.confidence_lo(), stats.confidence_hi()))
