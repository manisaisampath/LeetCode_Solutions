class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result=[]
        string=[]
        def backtrack(opened,closed):
            if opened==closed==n:
                result.append("".join(string))
                return 
            if opened<n:
                string.append("(")
                backtrack(opened+1,closed)
                string.pop()
            if closed<opened:
                string.append(")")        
                backtrack(opened,closed+1)
                string.pop()
        backtrack(0,0)
        return result