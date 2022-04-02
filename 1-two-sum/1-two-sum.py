class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in dict:
                return [dict[remaining], i]
            dict[v] = i
        return []
        