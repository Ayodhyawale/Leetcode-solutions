class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        f=-1
        for i in nums:
            if i not in d:
                d[i]=1
            else: d[i]+=1
        for i in d:
            if d[i]>(len(nums)//2):
                f=i
                break
        return f
                
        