class Island:

    def __init__(self, N, M, matrix):
        self.n = N
        self.m = M
        self.matrix = matrix

        # Creating matrix filled with 0's
        self.visited = [[0 for _ in range(M)] for _ in range(N)]

    def DFS(self, x, y):

        # Checking coordinates
        if (x < 0 or x >= self.n) or (y < 0 or y >= self.m) or (self.matrix[x][y] != 1 or self.visited[x][y] == 1):
            return

        # Marking point as visited
        self.visited[x][y] = 1

        # Down
        self.DFS(x - 1, y)
        # Right
        self.DFS(x, y + 1)
        # Up
        self.DFS(x + 1, y)
        # Left
        self.DFS(x, y - 1)

    def counting_islands(self):
        num_islands = 0

        for i in range(self.n):
            for j in range(self.m):
                if (self.matrix[i][j] == 1) and (not self.visited[i][j]):

                    # Starting the DFS in order to find all connected islands to the point
                    self.DFS(i, j)
                    num_islands += 1

        return num_islands


print("Input:")

N, M = list(map(int, input().split(" ")))
matrix = [list(map(int, input().split(" "))) for _ in range(N)]

# Creating object of Island class
island = Island(N, M, matrix)

# Time Complexity - O(n*m), Space Complexity - O(n*m)
res = island.counting_islands()
print(f"Output: {res}")
