class Solution:
    def candy(self, arr: List[int]) -> int:
        n=len(arr)
        r=[1]*n
        l=[1]*n
        Sum=0
    
        for i in range(1,n):
            if arr[i-1]<arr[i]:
                r[i]=r[i-1]+1
    
        for i in range(n-2,-1,-1):
            if arr[i+1]<arr[i]:
                l[i]=l[i+1]+1
    
        for i in range(n):
            Sum+=max(l[i],r[i])
        return Sum
        