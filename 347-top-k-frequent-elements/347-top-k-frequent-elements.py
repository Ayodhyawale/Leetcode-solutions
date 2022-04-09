class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] = d[num] + 1
        arr= sorted(d, key = d.get,reverse = True)
        return arr[:k]
            
        