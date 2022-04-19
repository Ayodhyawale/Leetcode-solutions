class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs)==1: return strs[0]
        s=strs[0]
        m=float("inf")
        for i in range(1,len(strs)):
            c,j,k=0,0,0
            while j<len(s) and k<len(strs[i]):
                if s[j]==strs[i][k]:
                    c+=1
                else:
                    break
                j+=1
                k+=1
            m=min(m,c)
        return s[:m]
                    
        