class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        sumy=0
        res=[]
        final=[]
        for i in range(len(digits)):
            sumy=sumy*10+digits[i]
        sumy=sumy+1
        while(sumy>0):
            rem=sumy%10
            res.append(rem)
            sumy=sumy//10
        final=res[::-1]
        return final

        