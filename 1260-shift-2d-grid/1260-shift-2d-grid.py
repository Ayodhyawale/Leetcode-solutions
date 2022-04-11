class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        def posToVal(r,c):
            return r*n+c
        def valToPos(v):
            return [v//n,v%n]
        
        res=[[0]*n for i in range(m)]
        for r in range(m):
            for c in range(n):
                newval=(posToVal(r,c)+k)%(m*n)
                nr,nc=valToPos(newval)
                res[nr][nc]=grid[r][c]
        return res