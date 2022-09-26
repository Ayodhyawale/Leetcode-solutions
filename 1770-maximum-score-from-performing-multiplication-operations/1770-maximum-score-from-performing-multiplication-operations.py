class Solution:
    def maximumScore(self, nums: List[int], multi: List[int]) -> int:
        memo = {}
        def solve(b,e,i):
            if i >= len(multi):
                return 0
            if (b,e,i) in memo:
                return memo[(b,e,i)]
            if e < 0:
                e = b
            if b >= len(nums):
                b = e
            x = max(solve(b+1,e,i+1)+nums[b]*multi[i],solve(b,e-1,i+1)+nums[e]*multi[i])
            memo[(b,e,i)] = x
            return x
        return solve(0,len(nums)-1,0)        