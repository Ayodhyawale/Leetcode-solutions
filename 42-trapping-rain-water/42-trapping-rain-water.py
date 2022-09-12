class Solution:
    def trap(self, A: List[int]) -> int:
        i, j = 0, len(A) - 1
        left, right = A[i], A[j]
        res = 0
        while i < j:
            left = max(left, A[i])
            right = max(right, A[j])
            if left < right:
                res += left - A[i]
                i += 1
            else:
                res += right - A[j]
                j -= 1
        return res
                