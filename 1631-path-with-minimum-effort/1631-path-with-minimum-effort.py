class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        m, n = len(heights), len(heights[0])
        
        def in_box(r, c, m=m, n=n):
            
            return r >= 0 and r < m and c >=0 and c < n
        
        h = []
        heappush(h, (0,(0,0)))
        costs = [[math.inf for _ in range(n)] for _ in range(m)]
        costs[0][0] = 0
        while h:
            cost, (r, c) = heappop(h)
            if (r,c) == (m-1, n-1):
                return cost
            
            for step in [(1,0),(0,-1),(-1,0),(0,1)]:
                i = r + step[0]
                j = c + step[1]
                if in_box(i, j):
                    if costs[i][j] == math.inf:
                        heappush(h, (max(cost,  abs(heights[i][j] - heights[r][c])), (i,j)))
                        costs[i][j] = abs(heights[i][j] - heights[r][c])
                    elif costs[i][j] > abs(heights[i][j] - heights[r][c]):
                        costs[i][j] = abs(heights[i][j] - heights[r][c])
                        heappush(h, (max(cost,  abs(heights[i][j] - heights[r][c])), (i,j)))
                        
        return 0