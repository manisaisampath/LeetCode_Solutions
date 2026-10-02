class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        seen=set()
        while(n>1):
            sum=0
            if n in seen:
                return False
            seen.add(n)
            while(n>0):
                rem=n%10
                sum+=rem*rem
                n=n//10
            if sum==1:
                return True
            n=sum
        return False
            
            
        