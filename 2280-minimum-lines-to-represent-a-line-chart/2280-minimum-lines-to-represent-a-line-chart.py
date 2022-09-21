class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        length = len(stockPrices)       
        if length==1:
            return 0

        stockPrices.sort(key = lambda x:x[0])

        count = 1
        for i in range(2,length):
            Ax,Ay = stockPrices[i]
            Bx,By = stockPrices[i-1]
            Cx,Cy = stockPrices[i-2]
            if (Ay - By)*(Bx - Cx)!=(Ax - Bx)*(By - Cy):
                count+=1

        return count