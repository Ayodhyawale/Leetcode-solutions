class Solution:
    def trap(self, A: List[int]) -> int:
        i, j = 0, len(A) - 1
        left_max, right_max = A[i], A[j]
        res = 0
        while i < j:
            left_max = max(left_max, A[i])
            right_max = max(right_max, A[j])
            if left_max < right_max:
                res += left_max - A[i]
                i += 1
            else:
                res += right_max - A[j]
                j -= 1
        return res
                