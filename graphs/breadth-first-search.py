class G:
    def __init__(self, n):
        self.n = n
        print("Enter adjacency matrix:")
        self.a = [list(map(int, input().split())) for _ in range(n)]
        self.v = [0] * n

    def bfs(self):
        q = [0] * 100   # Queue using array
        front = -1
        rear = -1

        # Start from node 0
        rear += 1
        q[rear] = 0
        self.v[0] = 1

        print("BFS Traversal:")

        while front != rear:
            front += 1
            x = q[front]
            print(x + 1, end=" ")

            for i in range(self.n):
                if self.a[x][i] == 1 and self.v[i] == 0:
                    rear += 1
                    q[rear] = i
                    self.v[i] = 1


# Driver Code
n = int(input("Enter number of nodes: "))
g = G(n)
g.bfs()
