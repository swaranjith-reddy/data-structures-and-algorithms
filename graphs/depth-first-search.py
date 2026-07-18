class G:
    def __init__(self, n):
        self.n = n
        print("Enter adjacency matrix:")
        self.a = [list(map(int, input().split())) for _ in range(n)]
        self.v = [0] * n

    def dfs(self, x):
        print(x + 1, end=" ")
        self.v[x] = 1

        for i in range(self.n):
            if self.a[x][i] == 1 and self.v[i] == 0:
                self.dfs(i)


# Driver Code
n = int(input("Enter number of nodes: "))
g = G(n)

print("DFS Traversal:")
g.dfs(0)   # Start from node 0
