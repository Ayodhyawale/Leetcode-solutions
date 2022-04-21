class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        # traverse the string to find the longest palindromic substring
        for i in range(len(s)):
            # start from two word
            cur = self.helper(s, i, i+1)
            if len(cur) > len(res): 
                res = cur
            # start from single word
            cur = self.helper(s, i, i)
            if len(cur) > len(res): 
                res = cur
        return res
    
    # function to return the longest palindromic substring
    def helper(self, s, left_pos, right_pos):
        while left_pos >= 0 and right_pos < len(s) and s[left_pos] == s[right_pos]:
            left_pos -= 1
            right_pos += 1
        return s[left_pos+1:right_pos]