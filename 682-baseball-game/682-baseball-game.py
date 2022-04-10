class Solution:
    def calPoints(self, ops: List[str]) -> int:
        n=len(ops)
        a=[]
        i=0
        while i<n:
            if ops[i]=='D':
                x=int(a.pop())
                a.append(x)
                a.append(x*2)
            elif ops[i]=='C':
                a.pop()
            elif ops[i]=="+":
                x=int(a.pop())
                y=int(a.pop())
                a.append(y)
                a.append(x)
                a.append(x+y)
            else:
                a.append(int(ops[i]))
            i+=1
        return sum(a)
