class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        maxy=""
        for i in range(1,len(str2)+1):
            new=str2[:i]
            val1=len(str1)//len(new)
            val2=len(str2)//len(new)
            if new*val1==str1 and new*val2==str2:
                if len(new)>len(maxy):
                    maxy=new
        return maxy



        